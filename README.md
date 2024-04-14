El proyecto se trata de una aplicación de escritorio con el propósito de servir como un adentramiento a una vida más saludable por medio de facilitar el acceso a recursos de temas que abarcan desde molestias generales, información sobre padecimientos mentales comunes y recomendaciones de dietas y ejercicio.

Indicaciones para la instalación de la aplicación

1. Instalar los requisitos: Utilice el siguiente comando para instalar los requisitos desde el archivo requirements.txt:
pip install -r app/requirements.txt

2. Ejecutar auto-py-to-exe:
Ejecute auto-py-to-exe.
Se abrirá una ventana de configuración.

3. Configuración de auto-py-to-exe:
En "Script Location", seleccione el archivo main.py ubicado dentro de la carpeta main.
Seleccione "One Directory" en el apartado "Onefile".
En "Console Windows", elija "Window based (hide the console)".
Seleccione la ubicación del icono en "Icon" (ubicado en app/icono.ico).
En "Additional Files", agregue la carpeta de imágenes, el archivo meditacion.mp3, y el archivo apoyo.py, todos ubicados en la carpeta app.
En caso de desear instalar en una carpeta específica, modifique la dirección en "Settings".

4. Creación del ejecutable:
Haga clic en "Convert .py to .exe".
Finalización del proceso:

Una vez completado el proceso, haga clic en "Open Output Folder".
Dentro de la carpeta main, encontrará el archivo generado. Puede cerrar de forma segura la ventana de auto-py-to-exe.

5. Ajustes adicionales:
Antes de continuar, acceda a la carpeta _internal y mueva la carpeta de imágenes a la carpeta main.
