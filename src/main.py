from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont, QFontDatabase
from graphs import barGraph, pieGraph
from conexion_2 import read
from credits import creditsWindow
from modules import createWindow, readWindow, updateWindow, deleteWindow
import sys, os


class MainWindow(QMainWindow):
    def __init__(self, directorio : str = os.path.dirname(os.path.abspath(__file__))):
        super().__init__()
        self.setWindowTitle("Proyecto CRUD")
        self.setGeometry(200, 100, 700, 740)
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
        # --- CREDITS ---
        path_to_credit_icon = os.path.join(directorio, "assets", "icons", "credit_btn.png")
        path_to_credit_hover = os.path.join(directorio, "assets", "icons", "credit_btn_hover.png")
        self.credit_icon_normal = QIcon(path_to_credit_icon)
        self.credit_icon_hover = QIcon(path_to_credit_hover)
        # --- Milita font ---
        path_to_militta_font = os.path.join(directorio, "assets", "fonts", "MilittaFont", "militta-bw8ag.ttf")
        id_militta = QFontDatabase.addApplicationFont(path_to_militta_font)
        if id_militta == -1:
            print(f"Error: couldn't found source {path_to_militta_font}")
            MilittaFont = QFont("cursive", 12)
        else:
            Militta = QFontDatabase.applicationFontFamilies(id_militta)[0]
            MilittaFont = QFont(Militta, 16)
        # --- CREATE ---
        path_to_create_icon = os.path.join(directorio, "assets", "icons", "create_btn.png")
        path_to_create_hover = os.path.join(directorio, "assets", "icons", "create_btn_hover.png")
        self.create_icon_normal = QIcon(path_to_create_icon)
        self.create_icon_hover = QIcon(path_to_create_hover)
        # --- READ ---
        path_to_read_icon = os.path.join(directorio, "assets", "icons", "read_btn.png")
        path_to_read_hover = os.path.join(directorio, "assets", "icons", "read_btn_hover.png")
        self.read_icon_normal = QIcon(path_to_read_icon)
        self.read_icon_hover = QIcon(path_to_read_hover)
        # --- UPDATE ---
        path_to_update_icon = os.path.join(directorio, "assets", "icons", "update_btn.png")
        path_to_update_hover = os.path.join(directorio, "assets", "icons", "update_btn_hover.png")
        self.update_icon_normal = QIcon(path_to_update_icon)
        self.update_icon_hover = QIcon(path_to_update_hover)
        # --- DELETE ---
        path_to_delete_icon = os.path.join(directorio, "assets", "icons", "delete_btn.png")
        path_to_delete_hover = os.path.join(directorio, "assets", "icons", "delete_btn_hover.png")
        self.delete_icon_normal = QIcon(path_to_delete_icon)
        self.delete_icon_hover = QIcon(path_to_delete_hover)

        #Title
        self.title=QLabel("Tarea 2.2: Create, Read, Update and Delete", self)
        self.title.setFont(MilittaFont)
        self.title.setStyleSheet("color: black;")
        self.title.setGeometry(20, 10, 300, 30)

        #Close button config
        self.close_button = QPushButton()
        self.close_button.setParent(self)
        self.close_button.setGeometry(660, 10, 30, 30)
        self.close_button.clicked.connect(self.close)
        self.close_button.setIcon(QIcon(path_to_close_icon))
        self.close_button.setIconSize(self.close_button.size())
        self.close_button.setStyleSheet("QPushButton { border: none; }")
        self.close_button.enterEvent = lambda e: self.close_button.setIcon(self.close_icon_hover)
        self.close_button.leaveEvent = lambda e: self.close_button.setIcon(self.close_icon_normal)

        #Minimize button config
        self.minimize_button = QPushButton()
        self.minimize_button.setParent(self)
        self.minimize_button.setGeometry(590, 10, 30, 30)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setIcon(QIcon(path_to_minimize_icon))
        self.minimize_button.setIconSize(self.minimize_button.size())
        self.minimize_button.setStyleSheet("QPushButton { border: none; }")
        self.minimize_button.enterEvent = lambda e: self.minimize_button.setIcon(self.minimize_icon_hover)
        self.minimize_button.leaveEvent = lambda e: self.minimize_button.setIcon(self.minimize_icon_normal)
        
        #Credit button config
        self.credit_button = QPushButton()
        self.credit_button.setParent(self)
        self.credit_button.setGeometry(625, 10, 30, 30)
        self.credit_button.clicked.connect(self.showCredits)
        self.credit_button.setIcon(QIcon(path_to_credit_icon))
        self.credit_button.setIconSize(self.credit_button.size())
        self.credit_button.setStyleSheet("QPushButton { border: none; }")
        self.credit_button.enterEvent = lambda e: self.credit_button.setIcon(self.credit_icon_hover)
        self.credit_button.leaveEvent = lambda e: self.credit_button.setIcon(self.credit_icon_normal)

        #Create button config
        self.create = QPushButton()
        self.create.setParent(self)
        self.create.setGeometry(30, 50, 150, 150)
        self.create.clicked.connect(self.showCreate)
        self.create.setIcon(QIcon(path_to_create_icon))
        self.create.setIconSize(self.create.size())
        self.create.setStyleSheet("QPushButton { border: none; }")
        self.create.enterEvent = lambda e: self.create.setIcon(self.create_icon_hover)
        self.create.leaveEvent = lambda e: self.create.setIcon(self.create_icon_normal)

        #Read
        self.read = QPushButton()
        self.read.setParent(self)
        self.read.setGeometry(30, 220, 150, 150)
        self.read.clicked.connect(self.showRead)
        self.read.setIcon(QIcon(path_to_read_icon))
        self.read.setIconSize(self.read.size())
        self.read.setStyleSheet("QPushButton { border: none; }")
        self.read.enterEvent = lambda e: self.read.setIcon(self.read_icon_hover)
        self.read.leaveEvent = lambda e: self.read.setIcon(self.read_icon_normal)

        #Update
        self.update = QPushButton()
        self.update.setParent(self)
        self.update.setGeometry(30, 390, 150, 150)
        self.update.clicked.connect(self.showUpdate)
        self.update.setIcon(QIcon(path_to_update_icon))
        self.update.setIconSize(self.update.size())
        self.update.setStyleSheet("QPushButton { border: none; }")
        self.update.enterEvent = lambda e: self.update.setIcon(self.update_icon_hover)
        self.update.leaveEvent = lambda e: self.update.setIcon(self.update_icon_normal)

        #Delete
        self.delete = QPushButton()
        self.delete.setParent(self)
        self.delete.setGeometry(30, 560, 150, 150)
        self.delete.clicked.connect(self.showDelete)
        self.delete.setIcon(QIcon(path_to_delete_icon))
        self.delete.setIconSize(self.delete.size())
        self.delete.setStyleSheet("QPushButton { border: none; }")
        self.delete.enterEvent = lambda e: self.delete.setIcon(self.delete_icon_hover)
        self.delete.leaveEvent = lambda e: self.delete.setIcon(self.delete_icon_normal)

        #Graphs
        self.canvas0 = pieGraph(*read("carrera", "carrera.nombre, count(*), carrera.id", "join estudiante on estudiante.id_carrera = carrera.id group by carrera.nombre, carrera.id"))
        self.canvas0.setParent(self)
        self.canvas0.setFixedSize(450, 300)
        self.canvas0.move(220, 50)
        
        self.canvas1 = barGraph(*read("curso", "curso.nombre, count(*), curso.id", "join inscrito on curso.id = inscrito.id group by curso.nombre, curso.id order by curso.id"))
        self.canvas1.setParent(self)
        self.canvas1.setFixedSize(450, 300)
        self.canvas1.move(220, 390)

        self.__drag_position = None
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.__drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.__drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.__drag_position)
            event.accept()
    
    def updateCanvas(self):
        self.canvas0.update_data(*read("carrera", "carrera.nombre, count(*), carrera.id", "join estudiante on estudiante.id_carrera = carrera.id group by carrera.nombre, carrera.id"))
        self.canvas1.update_data(*read("curso", "curso.nombre, count(*), curso.id", "join inscrito on curso.id = inscrito.id group by curso.nombre, curso.id order by curso.id"))
    
    def showCredits(self):
        self.creditsWin = creditsWindow()
        self.creditsWin.show()
    
    def showCreate(self):
        self.createWin = createWindow()
        self.createWin.data_changed.connect(self.updateCanvas)
        self.createWin.show()
        
    def showRead(self):
        self.readWin = readWindow()
        self.readWin.show()
    
    def showUpdate(self):
        self.updateWin = updateWindow()
        #self.updateWin.data_changed.connect(self.updateCanvas)
        self.updateWin.show()
    
    def showDelete(self):
        self.deleteWin = deleteWindow()
        #self.deleteWin.data_changed.connect(self.updateCanvas)
        self.deleteWin.show()

if __name__ == "__main__":
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
