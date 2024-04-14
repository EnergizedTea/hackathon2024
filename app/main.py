from apoyo import *
from functools import partial
from PyQt6.QtWidgets import  QRadioButton,QMessageBox
import webbrowser
import pygame
import requests
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        pygame.mixer.init()
        self.regresar()
        self.advertencia('Esta solo es un herramienta de apoyo no es un diagnóstico, consulte a un profesional.')
        self.btn_inicio1.clicked.connect(self.regresar)
        self.btn_inicio_2.clicked.connect(self.regresar)
        self.btn_inicio3.clicked.connect(self.regresar)
        self.btn_inicio4.clicked.connect(self.regresar)
        self.btn_inicio5.clicked.connect(self.regresar)
        self.btn_inicio6.clicked.connect(self.regresar)
        self.pushButton.clicked.connect(partial(self.navegar,1))
        self.pushButton_2.clicked.connect(partial(self.navegar,2))
        self.pushButton_3.clicked.connect(partial(self.navegar,3))
        self.pushButton_4.clicked.connect(partial(self.navegar,4))
        self.pushButton_11.clicked.connect(partial(self.navegar,6))
        self.pushButton_5.clicked.connect(partial(self.navegar,5))
        self.Cabeza.clicked.connect(self.dolores)
        self.Garganta.clicked.connect(self.dolores)
        self.Hombro.clicked.connect(self.dolores)
        self.Brazo.clicked.connect(self.dolores)
        self.Pecho.clicked.connect(self.dolores)
        self.Estomago.clicked.connect(self.dolores)
        self.Pierna.clicked.connect(self.dolores)
        self.Pie.clicked.connect(self.dolores)
        self.pushButton_15.clicked.connect(self.buscar_en_youtube)
        self.depresion.clicked.connect(self.buscar_en_youtube)
        self.ansiedad.clicked.connect(self.buscar_en_youtube)
        self.TDAH.clicked.connect(self.buscar_en_youtube)
        self.bipolaridad.clicked.connect(self.buscar_en_youtube)
        self.btn_play.clicked.connect(self.reproducir_audio)
        self.pushButton_16.clicked.connect(self.descargar_pdf)
        self.musica = 0
    def regresar(self):
        self.stackedWidget.setCurrentIndex(0)
        pygame.mixer.music.stop()
    def navegar(self,boton):
       self.stackedWidget.setCurrentIndex(boton)
    def dolores(self):
        texto =self.obtener_nombre_boton()
        self.label_10.setText(texto)
    def obtener_nombre_boton(self):
        boton = self.sender()
        texto = boton.objectName()
        return texto
    def padecimientos(self):
        padecimiento = self.obtener_nombre_boton()
        return padecimiento
    def buscar_en_youtube(self):
        parte = self.label_10.text()
        padecimiento = self.padecimientos()
        intensidad = None
        consulta = None
        intensidad = self.checar_botones(self.verticalLayout_3)
        if intensidad and parte:
            consulta = f'Dolor {intensidad} de {parte}'
        if not intensidad and padecimiento:
            consulta = f'Identificar si tengo {padecimiento}'
        if consulta:
            url = f"https://www.youtube.com/results?search_query={consulta}&sp=CAASAhAB,EgIQAg%3D%3D"
            webbrowser.open(url)
        else:
            self.advertencia('Por favor seleccione ambas opciones')
    def reproducir_audio(self):
        if self.musica == 0:
            try:
                pygame.mixer.music.load('meditacion.mp3')
                pygame.mixer.music.play()
                self.musica = 1
            except pygame.error as e:
                self.advertencia(f'Error al reproducir el audio:{e}')
        elif self.musica == 1:
            pygame.mixer.music.pause()
            self.musica = 2
        else:
            pygame.mixer.music.unpause()
            self.musica = 1
    def advertencia(self,texto):
        advertencia = QMessageBox(self)
        advertencia.setText(texto)  
        advertencia.show()
    def checar_botones (self,layout):
        eleccion = None
        for i in range(layout.count()):
            boton = layout.itemAt(i).widget()
            if isinstance(boton, QRadioButton) and boton.isChecked():
                eleccion = boton.objectName()
        return eleccion
    def descargar_pdf(self):
        dieta = self.checar_botones(self.horizontalLayout_5)
        ejercicio = self.checar_botones(self.horizontalLayout_6)
        url_pdf = None
        if dieta == 'ganar_musculo':
            url_pdf = 'https://github.com/EnergizedTea/hackathon2024/raw/main/Dieta%20ganar%20musculo.pdf'
        elif dieta == 'perder_grasa':
            url_pdf = 'https://github.com/EnergizedTea/hackathon2024/raw/main/Dieta%20perder%20grasa.pdf'
        elif dieta == 'balancear':
            url_pdf = 'https://github.com/EnergizedTea/hackathon2024/raw/main/Dieta%20balanceada.pdf'
        if ejercicio:
            try:
                response = requests.get(url_pdf)
                response.raise_for_status()
                with open("Dieta.pdf", "wb") as archivo:
                    archivo.write(response.content)
                QMessageBox.information(self, "Descarga Exitosa", "El PDF se ha descargado exitosamente ")
            except requests.exceptions.RequestException as e:
                QMessageBox.warning(self, "Error de Descarga", f"Ocurrió un error al descargar el PDF: {e}")
if __name__=='__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()