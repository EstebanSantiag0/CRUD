from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFontDatabase, QFont
import sys, os

class creditsWindow(QMainWindow):
    def __init__(self, directorio : str = os.path.dirname(os.path.abspath(__file__))):
        super().__init__()
        self.setWindowTitle("credits window")
        self.setGeometry(900, 100, 400, 260)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: white;")

        #Paths
        # --- CLOSE ---
        path_to_close_icon = os.path.join(directorio, "assets", "icons", "close_btn.png")
        path_to_close_hover = os.path.join(directorio, "assets", "icons", "close_btn_hover.png")
        self.close_icon_normal = QIcon(path_to_close_icon)
        self.close_icon_hover = QIcon(path_to_close_hover)
        # --- MINIMIZE ---
        path_to_minimize_icon = os.path.join(directorio, "assets", "icons", "min_btn.png")
        path_to_minimize_hover = os.path.join(directorio, "assets", "icons", "min_btn_hover.png")
        self.minimize_icon_normal = QIcon(path_to_minimize_icon)
        self.minimize_icon_hover = QIcon(path_to_minimize_hover)
        # --- Milita font ---
        path_to_militta_font = os.path.join(directorio, "assets", "fonts", "MilittaFont", "militta-bw8ag.ttf")
        id_militta = QFontDatabase.addApplicationFont(path_to_militta_font)
        if id_militta == -1:
            print(f"Error: couldn't found source {path_to_militta_font}")
            MilittaFont = QFont("cursive", 12)
        else:
            Militta = QFontDatabase.applicationFontFamilies(id_militta)[0]
            MilittaFont = QFont(Militta, 16)
        path_to_comic_neue_font = os.path.join(directorio, "assets", "fonts", "ComicNeue-Regular.ttf")
        id_comic_neue = QFontDatabase.addApplicationFont(path_to_comic_neue_font)
        if id_comic_neue == -1:
            print(f"Error: Couldn't found source: {path_to_comic_neue_font}")
            ComicNeueFont = QFont("cursive", 12)
        else:
            ComicNeue = QFontDatabase.applicationFontFamilies(id_comic_neue)[0]
            ComicNeueFont = QFont(ComicNeue, 14)

        #Title
        self.title=QLabel("Creditos", self)
        self.title.setFont(MilittaFont)
        self.title.setStyleSheet("color: black;")
        self.title.setGeometry(20, 10, 300, 30)

        #Close button config
        self.close_button = QPushButton()
        self.close_button.setParent(self)
        self.close_button.setGeometry(360, 10, 30, 30)
        self.close_button.clicked.connect(self.close)
        self.close_button.setIcon(QIcon(path_to_close_icon))
        self.close_button.setIconSize(self.close_button.size())
        self.close_button.setStyleSheet("QPushButton { border: none; }")
        self.close_button.enterEvent = lambda e: self.close_button.setIcon(self.close_icon_hover)
        self.close_button.leaveEvent = lambda e: self.close_button.setIcon(self.close_icon_normal)

        #Minimize button config
        self.minimize_button = QPushButton()
        self.minimize_button.setParent(self)
        self.minimize_button.setGeometry(325, 10, 30, 30)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setIcon(QIcon(path_to_minimize_icon))
        self.minimize_button.setIconSize(self.minimize_button.size())
        self.minimize_button.setStyleSheet("QPushButton { border: none; }")
        self.minimize_button.enterEvent = lambda e: self.minimize_button.setIcon(self.minimize_icon_hover)
        self.minimize_button.leaveEvent = lambda e: self.minimize_button.setIcon(self.minimize_icon_normal)
        
        text = ["Este programa fué realizado por Esteban",
                "de Jesús Santiago Torres, alumno de la",
                "Universidad Tecnológica de la Mixteca",
                "para la materia de Bases de Datos con",
                "el único fin de reforzar y adquirir nuevos",
                "conocimientos de los lenguajes Python y",
                "aumentar mi repositorio con proyectos de",
                "calidad, además de poder ayudar a quien",
                "requiera de funcionalidades similares."
        ]
        for i in range(0, len(text)):
            line0 = QLabel(text[i], self)
            line0.setFont(ComicNeueFont)
            line0.setStyleSheet("color: black;")
            line0.setGeometry(30, 50 + i*20, 340, 20)

        self.__drag_position =  None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.__drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.__drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.__drag_position)
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win =  creditsWindow()
    win.show()
    sys.exit(app.exec())