from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QApplication, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFontDatabase, QFont
import os, sys

class baseWindow(QMainWindow):
    def __init__(self, windowTitle : str, width : int, high : int, directorio : str = os.path.dirname(os.path.abspath(__file__))):
        super().__init__()
        self.setWindowTitle(windowTitle)
        self.setGeometry(900, 100, width, high)
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
            self.MilittaFont = QFont("cursive", 12)
        else:
            Militta = QFontDatabase.applicationFontFamilies(id_militta)[0]
            self.MilittaFont = QFont(Militta, 16)
        path_to_comic_neue_font = os.path.join(directorio, "assets", "fonts", "ComicNeue-Regular.ttf")
        id_comic_neue = QFontDatabase.addApplicationFont(path_to_comic_neue_font)
        if id_comic_neue == -1:
            print(f"Error: Couldn't found source: {path_to_comic_neue_font}")
            self.ComicNeueFont = QFont("cursive", 12)
        else:
            ComicNeue = QFontDatabase.applicationFontFamilies(id_comic_neue)[0]
            self.ComicNeueFont = QFont(ComicNeue, 14)

        #Title
        self.title=QLabel(windowTitle, self)
        self.title.setFont(self.MilittaFont)
        self.title.setStyleSheet("color: black;")
        self.title.setGeometry(20, 10, 300, 30)

        #Close button config
        self.close_button = QPushButton()
        self.close_button.setParent(self)
        self.close_button.setGeometry(width-40, 10, 30, 30)
        self.close_button.clicked.connect(self.close)
        self.close_button.setIcon(QIcon(path_to_close_icon))
        self.close_button.setIconSize(self.close_button.size())
        self.close_button.setStyleSheet("QPushButton { border: none; }")
        self.close_button.enterEvent = lambda e: self.close_button.setIcon(self.close_icon_hover)
        self.close_button.leaveEvent = lambda e: self.close_button.setIcon(self.close_icon_normal)

        #Minimize button config
        self.minimize_button = QPushButton()
        self.minimize_button.setParent(self)
        self.minimize_button.setGeometry(width-75, 10, 30, 30)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setIcon(QIcon(path_to_minimize_icon))
        self.minimize_button.setIconSize(self.minimize_button.size())
        self.minimize_button.setStyleSheet("QPushButton { border: none; }")
        self.minimize_button.enterEvent = lambda e: self.minimize_button.setIcon(self.minimize_icon_hover)
        self.minimize_button.leaveEvent = lambda e: self.minimize_button.setIcon(self.minimize_icon_normal)

        self.__drag_position = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.__drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.__drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.__drag_position)
            event.accept()


class baseEntryWindow(baseWindow):
    def __init__(self, windowTitle, width, high, directorio : str = os.path.dirname(os.path.abspath(__file__))):
        super().__init__(windowTitle, width, high, directorio)
        self.entry = QLineEdit(self)
        self.entry.setGeometry(20, 100, width-40, 40)
        self.entry.setStyleSheet(
            """
            QLineEdit {
                background-color: white;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
            }
            """
        )
        self.entry.setFont(self.ComicNeueFont)
        
        self.search = QPushButton("Buscar", self)
        
        self.search.setParent(self)
        self.search.setStyleSheet(
        """QPushButton {
            background-color: white;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
        }
        QPushButton:hover {
                background-color: black;
                color: white;
                border-radius: 15px;
        }
        """
        )
        self.search.setGeometry(int((width - 80)/2), 150, width - 2*int((width - 80)/2), 35)
        self.search.setFont(self.ComicNeueFont)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = baseEntryWindow("Awa", 300, 200)
    win.show()
    sys.exit(app.exec())