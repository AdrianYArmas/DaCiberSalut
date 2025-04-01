import streamlit as st
st.set_page_config(layout="wide")  # Cambiar de wide a centered
# Usar CSS para ajustar el alto de la pantalla
st.markdown("""
    <style>
        .main {
            height: 100vh;
            display: flex;
            flex-direction: column;

        }
            
        .block-container {
            flex: 1;
            overflow-y: auto;
            padding: 1rem;
        }
            
        .st-emotion-cache-t1wise {
            padding-left: 5%;
            padding-right: 5%;
        }
            
        img {
            max-height: 50vh;
            object-fit: cover;
        } 
    
        .st-emotion-cache-ocsh0s {
            background-color: #1f77b4;
            color: whitesmoke;
        }
            
        .st-emotion-cache-ocsh0s:hover {
            background-color: whitesmoke ;
            border-color: #1f77b4;
            color: #1f77b4;
        }
        
        .st-emotion-cache-rjm97v{
            background-color: #1f77b4;
            color: whitesmoke;
        }
        
        .st-emotion-cache-rjm97v:hover{
            background-color: whitesmoke ;
            border-color: #1f77b4;
            color: #1f77b4;
        }
        
        .st-emotion-cache-ocsh0s:focus:not(:active) {
            background-color: #1f77b4;
            border-color: whitesmoke;
            color: whitesmoke;
        }
        
    </style>
""", unsafe_allow_html=True)

import torch
import torch.nn as nn
import torchvision.transforms as transforms
import timm
import torch.nn.functional as F
from PIL import Image
import os
import pandas as pd
import matplotlib.pyplot as plt

# Configuración
IMG_SIZE = 768
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
FILTER_CLASSES = ["histology", "other"]
CLASSIFIER_CLASSES = ["colon_aca", "colon_n", "lung_aca", "lung_n", "lung_scc"]

# Transformación
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Cargar modelo verificador
@st.cache_resource
def load_filter_model():
    model = timm.create_model("resnet18", pretrained=False)
    num_features = model.get_classifier().in_features
    model.fc = nn.Linear(num_features, 2)
    model.load_state_dict(torch.load("histology_filter_model.pth", map_location=DEVICE))
    model.eval()
    return model

# Cargar modelo clasificador principal
@st.cache_resource
def load_classifier_model():
    model = timm.create_model("efficientnet_b4", pretrained=False)
    num_features = model.classifier.in_features
    model.classifier = nn.Linear(num_features, len(CLASSIFIER_CLASSES))
    model.load_state_dict(torch.load("efficientnet_b4_colon_lung.pth", map_location=DEVICE))
    model.eval()
    return model

filter_model = load_filter_model()
classifier_model = load_classifier_model()

# Interfaz
#st.title("Clasificador de Cáncer con Verificación Histológica")
st.markdown("<h1 style='font-size: 20x;'>Clasificador de Cáncer con Verificación Histológica</h1>", unsafe_allow_html=True)
st.write("Sube una imagen. El sistema verificará si es histológica y, si lo es, la clasificará entre tipos de cáncer de colon y pulmón.")

uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key="unique")

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    image_inferface = image.resize((100, 100))
    #st.image(image,caption=uploaded_file.name)
    # Organizar los elementos con dos columnas
    col1, col2 = st.columns([1, 1])  # Imagen en la columna 1 (más pequeña), predicción en columna 2 (más grande)
    
    with col1:
        # Mostrar la imagen con tamaño ajustado y sin scroll
        col3,col4 = st.columns([5,1])
        with col3:
            st.image(image,caption=uploaded_file.name, use_container_width=True)

    with col2:
        input_tensor = transform(image).unsqueeze(0).to(DEVICE)
        
        with torch.no_grad():
            output = filter_model(input_tensor)
            probs = F.softmax(output, dim=1)
            pred = torch.argmax(probs, dim=1).item()
            confidence = probs[0, pred].item()

        if FILTER_CLASSES[pred] == "histology":
            st.success(f"✔️ Histológica ({confidence * 100:.2f}%)")
            
            with torch.no_grad():
                output = classifier_model(input_tensor)
                probs = F.softmax(output, dim=1)[0].cpu().numpy()
                pred_idx = probs.argmax()
            
            # Predicción con color dinámico (verde o rojo)
            pred_class = CLASSIFIER_CLASSES[pred_idx]
            color = 'green' if pred_class in ['colon_n', 'lung_n'] else 'crimson'

            st.markdown(f"""
                <div style='background-color:{color}; padding:10px; border-radius:5px; cursor: default; pointer-events: none; margin-bottom: 20px;'>
                    <h2 style='color:white; font-size:20px; text-align:center; margin: 0; padding: 0;'><b>Predicción: {pred_class}</b></h2>
                </div>
            """, unsafe_allow_html=True)
            
            # Mostrar los porcentajes con barras de progreso
            df = pd.DataFrame({"Clase": CLASSIFIER_CLASSES, "Probabilidad (%)": (probs * 100).round(2)})
            
            for i, row in df.iterrows():
                probabilidad = round(row['Probabilidad (%)'], 3)  
                formatted_probabilidad = f"{probabilidad:.2f}"
                st.write(f"{row['Clase']}: {formatted_probabilidad}%")
                st.progress(int(probabilidad))

        else:
            st.error(f"❌ No es una imagen histológica ({confidence * 100:.2f}%)")