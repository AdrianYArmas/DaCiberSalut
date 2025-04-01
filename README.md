# DaCiberSalut: Predicción de Cáncer de Colon y Pulmón
## Introducción 
DaCiberSalut es una herramienta desarrollada para la predicción de cáncer de colon y pulmón mediante el análisis de imágenes de histología. Este proyecto es el resultado de una colaboración entre Centro de Excelencia IES El Rincón - Gran Canaria, Institut Tecnològic de Barcelona (ITB), y CIFP Los Gladiolos - Santa Cruz de Tenerife.

## Objetivo
El objetivo de esta aplicación es proporcionar un modelo basado en Inteligencia Artificial que permita detectar posibles indicadores de cáncer en imágenes de tejidos, facilitando el diagnóstico médico. La aplicación utiliza redes neuronales profundas para analizar las imágenes histológicas y proporcionar una predicción.

## Índice
## Índice
1. [Descarga](#Descarga)
   * [Descarga manual](###Descarga-manual)
   * [Descarga por comandos](###Descarga-por-comandos)
2. [Instalación](##Instalación)
   * [Instalación Automática](##Instalación-automática)
   * [Instalación Manual](##instalación-manual)
3. [Uso](##uso)
4. [Estructura del Proyecto](##Estructura-del-proyecto)
5. [Tecnologías Utilizadas](##Tecnologías-utilizadas)
6. [Colaboradores](##Colaboradores)
7. [Enlace al Proyecto](##Enlace-al-proyecto)

## Descarga
### Descarga-manual {#Descarga-manual}
Descargar manualmente o clonar el proyecto.
para descargar manualmente debes acceder al [github del proyecto](https://github.com/AdrianYArmas/DaCiberSalut), dar click al botón verde que pone código y descargar como zip:
![Descarga zip](https://github.com/user-attachments/assets/756304f6-fba2-44e4-95b4-6a02826303b0)

Una vez descargada aparecerá en la carpeta descargas o en un desplegable en la esquina superior derecha del navegador:

![Carpeta .zip descargada](https://github.com/user-attachments/assets/bcf795a5-6e36-4950-9f79-979cb45ddd05)

Previo a su ejecución debes extraer la carpeta que se encuentra en ".zip", dando click derecho sobre ella con el ratón > extraer todo, y seleccionando la ruta donde quiera tener la aplicación.
![Vista de extraer todo](https://github.com/user-attachments/assets/bf04ae82-31bb-482e-b491-4ea249d51331)

### Descarga por comandos {#Descarga-por-comandos}
Si deseas descargar el proyecto mediante el cmd, deberás ir a la ruta en la que quiera tener la aplicación, por ejemplo el escritorio:
```bash
  cd C:\Users\Su-nombre-de-usuario\Desktop\
```

Y ahi debe hacer un git clone:
```bash
  git clone https://github.com/AdrianYArmas/DaCiberSalut.git
```

## Instalación {#Instalación}
### instalación automática {#Instalación-automática}
Para facilitar la instalación del proyecto, puedes ejecutar el archivo Ejecutable.bat dentro de la carpeta del proyecto. Esto instalará todos los requisitos automáticamente y pondrá en marcha la aplicación.

![Ejecutable.bat](https://github.com/user-attachments/assets/5ff96d37-bdb4-4552-9222-2132adbe142c)

Y una vez se cierra esta ventana, parará la ejecución de la aplicación. Esta instrucción queda reflejada mediante un mensaje rojo en la misma ventana:

![Prueba-mensaje-usuario-cerrado](https://github.com/user-attachments/assets/941a9576-1b61-41f6-9098-f9dd5b680164)

### instalación manual {#Instalación-manual}
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

## Uso {#uso}
Una vez instalada y ejecutada la aplicación, se abrirá una interfaz web donde podrás cargar imágenes histológicas, para ser procesadas por el modelo. La aplicación proporcionará una predicción sobre la presencia de cáncer de colon o pulmón, según sea el caso. En caso de subir una imágen no histológica será detectada y se verá reflejado en la interfaz.

##estructura del proyecto {#estructura-del-proyecto}
El proyecto tiene la siguiente estructura de archivos:
  ```bash
     DaCiberSalut/
    │
    ├── app.py                       # Script principal que ejecuta la aplicación Streamlit
    ├── histology_filter_model.pth   # Modelo de filtrado de imágenes histológicas
    ├── efficientnet_b4_colon_lung.pth # Modelo de predicción de cáncer de colon y pulmón
    └── Ejecutable.bat               # Archivo para instalación automática en Windows
  ```

## tecnologías utilizadas {#tecnologías-utilizadas}
* Streamlit: Framework para la creación de aplicaciones web interactivas de manera sencilla.
* PyTorch: Framework para el desarrollo de modelos de aprendizaje profundo.
* Torchvision: Librería de visión por computadora que facilita el trabajo con imágenes.
* Timm: Librería que incluye modelos preentrenados para tareas de visión por computadora.
* Pillow: Librería para la manipulación de imágenes en Python.
* Matplotlib: Librería para la creación de gráficos y visualización de datos.

## Colaboradores {#colaboradores}
Este proyecto fue realizado por:

[Francisco José González Rodríguez]()

[Juan Carlos Cox Fernández](https://github.com/JuanCarlosCox)

[Adrián Yared Armas de la Nuez](https://github.com/AdrianYArmas)

Colaboradores de las instituciones:

[IES El Rincón - Gran Canaria](https://www3.gobiernodecanarias.org/medusa/edublog/ieselrincon/)

[Institut Tecnològic de Barcelona (ITB)](https://itb.cat/)

[CIFP Los Gladiolos - Santa Cruz de Tenerife](https://www.losgladiolos.es/)

## Enlace al proyecto {#Enlace-al-proyecto}

Puedes encontrar el código fuente completo del proyecto en GitHub:

[https://github.com/AdrianYArmas/DaCiberSalut](https://github.com/AdrianYArmas/DaCiberSalut)
