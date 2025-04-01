- [Español](#menú-en-español)
- [English](#menu-in-english)
  
# DaCiberSalut: Predicción de Cáncer de Colon y Pulmón
## Introducción 
DaCiberSalut es una herramienta desarrollada para la predicción de cáncer de colon y pulmón mediante el análisis de imágenes de histología. Este proyecto es el resultado de una colaboración entre Centro de Excelencia IES El Rincón - Gran Canaria, Institut Tecnològic de Barcelona (ITB), y CIFP Los Gladiolos - Santa Cruz de Tenerife.

## Objetivo
El objetivo de esta aplicación es proporcionar un modelo basado en Inteligencia Artificial que permita detectar posibles indicadores de cáncer en imágenes de tejidos, facilitando el diagnóstico médico. La aplicación utiliza redes neuronales profundas para analizar las imágenes histológicas y proporcionar una predicción.

## Menú en Español 
1. [Descarga](#Descarga)
   * [Descarga manual](#Descarga-manual)
   * [Descarga por comandos](#Descarga-por-comandos)
2. [Instalación](#Instalación)
   * [Instalación Automática](#Instalación-automática)
   * [Instalación Manual](#Instalación-manual)
3. [Uso](#Uso)
4. [Estructura del Proyecto](#Estructura-del-proyecto)
5. [Tecnologías Utilizadas](#Tecnologías-utilizadas)
6. [Colaboradores](#Colaboradores)
7. [Enlace al Proyecto](#Enlace-al-proyecto)

## Descarga
### Descarga manual
Descargar manualmente o clonar el proyecto.
para descargar manualmente debes acceder al [github del proyecto](https://github.com/AdrianYArmas/DaCiberSalut), dar click al botón verde que pone código y descargar como zip:

![Descarga zip](https://github.com/user-attachments/assets/756304f6-fba2-44e4-95b4-6a02826303b0)

Una vez descargada aparecerá en la carpeta descargas o en un desplegable en la esquina superior derecha del navegador:

![Carpeta .zip descargada](https://github.com/user-attachments/assets/bcf795a5-6e36-4950-9f79-979cb45ddd05)

Previo a su ejecución debes extraer la carpeta que se encuentra en ".zip", dando click derecho sobre ella con el ratón > extraer todo, y seleccionando la ruta donde quiera tener la aplicación.

![Vista de extraer todo](https://github.com/user-attachments/assets/bf04ae82-31bb-482e-b491-4ea249d51331)

### Descarga por comandos
Si deseas descargar el proyecto mediante el cmd, deberás ir a la ruta en la que quiera tener la aplicación, por ejemplo el escritorio:
```bash
  cd C:\Users\Su-nombre-de-usuario\Desktop\
```

Y ahi debe hacer un git clone:
```bash
  git clone https://github.com/AdrianYArmas/DaCiberSalut.git
```

## Instalación
### instalación automática 
Para facilitar la instalación del proyecto, puedes ejecutar el archivo Ejecutable.bat dentro de la carpeta del proyecto. Esto instalará todos los requisitos automáticamente y pondrá en marcha la aplicación.

![Ejecutable.bat](https://github.com/user-attachments/assets/5ff96d37-bdb4-4552-9222-2132adbe142c)

Y una vez se cierra esta ventana, parará la ejecución de la aplicación. Esta instrucción queda reflejada mediante un mensaje rojo en la misma ventana:

![Prueba-mensaje-usuario-cerrado](https://github.com/user-attachments/assets/941a9576-1b61-41f6-9098-f9dd5b680164)

### instalación manual 
Si prefieres instalar el proyecto manualmente, sigue estos pasos:
1. Crea una carpeta para el proyecto:
```bash
  mkdir DaCiberSalut
  cd DaCiberSalut
```

2. Crea un entorno virtual:
```bash
  python -m venv venv
```

3. Activa el entorno virtual:
```bash
  venv\Scripts\activate
```

4. Instala las dependencias necesarias:
```bash
   pip install streamlit torch torchvision timm pillow matplotlib
```
5. Copia los siguientes ficheros a la carpeta DaCiberSalut:
  * app.py
  * histology_filter_model.pth
  * efficientnet_b4_colon_lung.pth
    
6. Ejecuta la aplicación:
```bash
   streamlit run app.py
```

#### Acceso a la Web
Una vez que la aplicación esté corriendo, podrás acceder a la interfaz web en tu navegador en la siguiente URL:
```bash
   http://localhost:8501/
```

## Uso 
Una vez instalada y ejecutada la aplicación, se abrirá una interfaz web donde podrás cargar imágenes histológicas, para ser procesadas por el modelo. La aplicación proporcionará una predicción sobre la presencia de cáncer de colon o pulmón, según sea el caso. En caso de subir una imágen no histológica será detectada y se verá reflejado en la interfaz.

En caso correcto y que se esté pasando una imágen permitida verá algo tal que así:

![Imagen cancer correcta](https://github.com/user-attachments/assets/fe311fb7-a9a9-4601-9784-92201fe37fcb)

Donde pone que es histológica junto con su confianza y en rojo el tipo de cancer.


En caso negativo observará algo tal que así:

![Imagen incorrecta](https://github.com/user-attachments/assets/38d814f1-8c91-411a-b08a-e545d4710f2e)

En cuyo caso se muestra un mensaje en rojo dejando claro que no es una imágen histológica.


## Estructura del proyecto 
El proyecto tiene la siguiente estructura de archivos:
  ```bash
     DaCiberSalut/
    │
    ├── app.py                       # Script principal que ejecuta la aplicación Streamlit
    ├── histology_filter_model.pth   # Modelo de filtrado de imágenes histológicas
    ├── efficientnet_b4_colon_lung.pth # Modelo de predicción de cáncer de colon y pulmón
    └── Ejecutable.bat               # Archivo para instalación automática en Windows
  ```

## Tecnologías utilizadas
* Streamlit: Framework para la creación de aplicaciones web interactivas de manera sencilla.
* PyTorch: Framework para el desarrollo de modelos de aprendizaje profundo.
* Torchvision: Librería de visión por computadora que facilita el trabajo con imágenes.
* Timm: Librería que incluye modelos preentrenados para tareas de visión por computadora.
* Pillow: Librería para la manipulación de imágenes en Python.
* Matplotlib: Librería para la creación de gráficos y visualización de datos.

## Colaboradores
Este proyecto fue realizado por:

[Francisco José González Rodríguez](https://github.com/fjgr)

[Juan Carlos Cox Fernández](https://github.com/JuanCarlosCox)

[Adrián Yared Armas de la Nuez](https://github.com/AdrianYArmas)

Colaboradores de las instituciones:

[IES El Rincón - Gran Canaria](https://www3.gobiernodecanarias.org/medusa/edublog/ieselrincon/)

[Institut Tecnològic de Barcelona (ITB)](https://itb.cat/)

[CIFP Los Gladiolos - Santa Cruz de Tenerife](https://www.losgladiolos.es/)

## Enlace al proyecto 

Puedes encontrar el código fuente completo del proyecto en GitHub:

[https://github.com/AdrianYArmas/DaCiberSalut](https://github.com/AdrianYArmas/DaCiberSalut)



###############################
###########################3###
###############################
# DaCiberSalut: Colon and Lung Cancer Prediction
## Introduction 
DaCiberSalut is a tool developed for the prediction of colon and lung cancer through the analysis of histological images. This project is the result of a collaboration between the Centro de Excelencia IES El Rincón - Gran Canaria, Institut Tecnològic de Barcelona (ITB), and CIFP Los Gladiolos - Santa Cruz de Tenerife.

## Objective
The objective of this application is to provide an Artificial Intelligence-based model that can detect potential indicators of cancer in tissue images, facilitating medical diagnosis. The application uses deep neural networks to analyze histological images and provide a prediction.

## Menu in English 
1. [Download](#Download)
   * [Manual Download](#Manual-Download)
   * [Download via Commands](#Download-via-Commands)
2. [Installation](#Installation)
   * [Automatic-Installation](#Automatic-Installation)
   * [Manual Installation](#Manual-Installation)
3. [Usage](#Usage)
4. [Project Structure](#Project-Structure)
5. [Technologies Used](#Technologies-Used)
6. [Contributors](#Contributors)
7. [Project Link](#Project-Link)

## Download
### Manual Download
Descargar manualmente o clonar el proyecto.
To manually download or clone the project, visit the [github del proyecto](https://github.com/AdrianYArmas/DaCiberSalut), click the green "Code" button, and download the ZIP file:

![Descarga zip](https://github.com/user-attachments/assets/756304f6-fba2-44e4-95b4-6a02826303b0)

Once downloaded, it will appear in the "Downloads" folder or in a dropdown at the top-right corner of the browser:

![Carpeta .zip descargada](https://github.com/user-attachments/assets/bcf795a5-6e36-4950-9f79-979cb45ddd05)

Before execution, you must extract the folder from the ".zip" file by right-clicking on it > Extract All, and selecting the destination folder.

![Vista de extraer todo](https://github.com/user-attachments/assets/bf04ae82-31bb-482e-b491-4ea249d51331)

### Download via Commands
If you want to download the project via the command line, navigate to the directory where you want the application (e.g., the Desktop):
```bash
  cd C:\Users\Su-nombre-de-usuario\Desktop\
```

Then, run the git clone command:
```bash
  git clone https://github.com/AdrianYArmas/DaCiberSalut.git
```

## Installation
### Automatic Installation
For easy installation, you can run the Executable.bat file within the project folder. This will automatically install all dependencies and start the application.

![Ejecutable.bat](https://github.com/user-attachments/assets/5ff96d37-bdb4-4552-9222-2132adbe142c)

Once this window closes, the application execution will stop. This is indicated by a red message in the same window:

![Prueba-mensaje-usuario-cerrado](https://github.com/user-attachments/assets/941a9576-1b61-41f6-9098-f9dd5b680164)

### Manual Installation
If you prefer to install the project manually, follow these steps:
1. Create a folder for the project:
```bash
  mkdir DaCiberSalut
  cd DaCiberSalut
```

2. Create a virtual environment:
```bash
  python -m venv venv
```

3. Activate the virtual environment:
```bash
  venv\Scripts\activate
```

4. Install the required dependencies:
```bash
   pip install streamlit torch torchvision timm pillow matplotlib
```
5. Copy the following files to the DaCiberSalut folder:
  * app.py
  * histology_filter_model.pth
  * efficientnet_b4_colon_lung.pth
    
6. Run the application:
```bash
   streamlit run app.py
```

#### Accessing the Web
Once the application is running, you can access the web interface in your browser at the following URL:
```bash
   http://localhost:8501/
```

## Usage 
After installing and running the application, a web interface will open where you can upload histological images to be processed by the model. The application will provide a prediction on the presence of colon or lung cancer, depending on the case. If a non-histological image is uploaded, it will be detected and this will be displayed in the interface.

If the image is correct and allowed, it will look like this:

![Imagen cancer correcta](https://github.com/user-attachments/assets/fe311fb7-a9a9-4601-9784-92201fe37fcb)

It will display the histological status along with the confidence level and, in red, the type of cancer.

If the image is not correct, you will see something like this:

![Imagen incorrecta](https://github.com/user-attachments/assets/38d814f1-8c91-411a-b08a-e545d4710f2e)

In this case, a red message will clearly state that the image is not histological.

## Project Structure
The project has the following file structure:
  ```bash
     DaCiberSalut/
    │
    ├── app.py                       # Script principal que ejecuta la aplicación Streamlit
    ├── histology_filter_model.pth   # Modelo de filtrado de imágenes histológicas
    ├── efficientnet_b4_colon_lung.pth # Modelo de predicción de cáncer de colon y pulmón
    └── Ejecutable.bat               # Archivo para instalación automática en Windows
  ```

## Technologies Used
* Streamlit: Framework for creating interactive web applications easily.
* PyTorch: Framework for deep learning model development.
* Torchvision: Computer vision library that facilitates working with images.
* Timm: Library that includes pre-trained models for computer vision tasks.
* Pillow: Python image manipulation library.
* Matplotlib: Library for creating graphs and visualizing data.

## Contributors
This project was created by:

[Francisco José González Rodríguez](https://github.com/fjgr)

[Juan Carlos Cox Fernández](https://github.com/JuanCarlosCox)

[Adrián Yared Armas de la Nuez](https://github.com/AdrianYArmas)

Contributors from the following institutions:

[IES El Rincón - Gran Canaria](https://www3.gobiernodecanarias.org/medusa/edublog/ieselrincon/)

[Institut Tecnològic de Barcelona (ITB)](https://itb.cat/)

[CIFP Los Gladiolos - Santa Cruz de Tenerife](https://www.losgladiolos.es/)

## Project Link

You can find the complete source code of the project on GitHub:

[https://github.com/AdrianYArmas/DaCiberSalut](https://github.com/AdrianYArmas/DaCiberSalut)

