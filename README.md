# Proyecto Final Visión Computacional EJ 2022

Se requiere tener Python installado previamente para poder ejecutar el proyecto.

Nota: El objetivo de usar ElectronJS es tener la facilidad de crear interfaces modernas para los usuarios con tecnologias web. La aplicación de escritorio de este proyecto no es nada más que un contenedor web (Chronium) para la página que se ejecuta aisladamente y que cuenta con un backend escrito en Python y NodeJS para el procesamiento de las imagenes.

## ¿Cómo correr el proyecto (Desarrollo)?
1. Instalar NodeJS.
2. Correr `npm install` dentro de la carpeta del proyecto.
3. Ejecutar `pyinstall` en un cmd o terminal.
4. Correr `npm start` en un cmd o terminal.

## Estructura del proyecto
- `index.html`: Interfaz de la aplicación, escrita en HTML.
- `style.css`: Estilos de la página 
- `index.js`: Inicializador de la aplicación
- `preload.js`: Funciones que corren en el backend
- `renderer.js`: Funciones que corren en el frontend
- `processed_images/`: Imagenes resultantes del procesamiento
- `requirements.txt`: Librerias de python necesarias para el proyecto
- `python-env/`: Entorno de python que contiene el ejecutable y las librerias

## ¿Cómo contribuir?
1. Crear una nueva rama apartir de `electron-project` con la nomenclatura `feature_nombreDeLaNuevaCaracteristica`
2. Hacer cambios y subir a la nueva rama
3. Hacer pull request a la rama `electron-project`
