from PyQt6.QtWidgets import QApplication, QPushButton, QComboBox, QLineEdit, QLabel
from PyQt6.QtCore import pyqtSignal
from pydantic import BaseModel, Field
from conexion_2 import create, read
from baseWin import baseWindow
from datetime import date
import sys, os, string

carreras = read("carrera", "count(*)")[0]
carreras = carreras[0]
cursos = read("curso", "count(*)")[0]
cursos = cursos[0]


class Estudiante(BaseModel):
    matricula: str = Field(
        max_length=20,
        pattern=r"^\d{4}-\d{3}$",
        description="Matrícula del estudiante. Formato: YYYY-NNN (ej. 2024-001)"
    )
    nombre: str = Field(max_length=20, min_length=1)
    id_carrera: int = Field()

class Curso(BaseModel):
    id: int = Field()
    nombre: str = Field(max_length=60, min_length=1)

class Carrera(BaseModel):
    id: int = Field()
    nombre:str = Field(max_length=60, min_length=1)










class enrollStudent(baseWindow):
    item_created = pyqtSignal()
    def __init__(self, directorio : str = os.path.dirname(os.path.abspath(__file__))):
        super().__init__("Inscribir Alumno", 400, 325, directorio)
        self.entry = QLineEdit(self)
        self.entry.setGeometry(20, 100, 360, 40)
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
        
        self.add = QPushButton("Añadir", self)
        
        self.add.setParent(self)
        self.add.setStyleSheet(
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
        self.add.setGeometry(160, 260, 80, 35)
        self.add.clicked.connect(self.enroll)
        self.add.setFont(self.ComicNeueFont)
        
        self.line0 = QLabel("Nombre del alumno", self)
        self.line0.setStyleSheet("color: black;")
        self.line0.setFont(self.ComicNeueFont)
        self.line0.setGeometry(20, 70, 360, 30)
        
        self.majors = list(read("carrera", "nombre", "order by id")[0])
        self.majorList = QComboBox(self)
        self.majorList.addItems(self.majors)
        self.majorList.setStyleSheet(
        """
        QComboBox {
            background-color: white;
            color: black;
            border: 4px solid black;
            border-radius: 15px;
            padding-left: 12px;
        }

        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 24px;
            border-left: 2px solid black;
            border-top-right-radius: 12px;
            border-bottom-right-radius: 12px;
            background-color: white;
        }

        QComboBox::down-arrow {
            image: none;
            width: 0px;
            height: 0px;
        }
        """
        )
        self.majorList.setFont(self.ComicNeueFont)
        self.majorList.setGeometry(20, 180, 360, 40)
        
        self.line0 = QLabel("Carrera", self)
        self.line0.setStyleSheet("color: black;")
        self.line0.setFont(self.ComicNeueFont)
        self.line0.setGeometry(20, 150, 360, 30)
    
    def enroll(self):
        current_year = date.today().year
        estudiantes = (read("estudiante", "count(*)", f"WHERE LEFT(matricula, 4) = '{current_year}'")[0])[0] + 1
        matricula = str(current_year)+"-"+f"{estudiantes:03d}"
        try:
            nombre = self.entry.text()
            if nombre.isspace():
                raise Exception()
            for i in nombre:
                if not(i.isspace()) and not(i.isalpha):
                    raise Exception()
        except:
            self.entry.setPlaceholderText("Caracteres inválidos")
            self.entry.setText("")
            return
        try:
            student = Estudiante(matricula=matricula, nombre=self.entry.text(), id_carrera=self.majorList.currentIndex()+1)
            student_dic = student.model_dump()
            create("estudiante", student_dic)
            self.item_created.emit()
            self.close()
        except:
            self.entry.setPlaceholderText("Nombre muy chico o muy grande")
            self.entry.setText("")












class createCourse(baseWindow):
    item_created = pyqtSignal()
    def __init__(self, directorio: str = os.path.dirname(os.path.abspath(__file__))):
        super().__init__("Nuevo Curso", 400, 220, directorio)

        self.line0 = QLabel("Nombre del curso", self)
        self.line0.setStyleSheet("color: black;")
        self.line0.setFont(self.ComicNeueFont)
        self.line0.setGeometry(20, 70, 360, 30)

        self.entry = QLineEdit(self)
        self.entry.setGeometry(20, 100, 360, 40)
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

        self.add = QPushButton("Añadir", self)
        self.add.setStyleSheet(
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
        self.add.setGeometry(160, 160, 80, 35)
        self.add.clicked.connect(self.addCourse)
        self.add.setFont(self.ComicNeueFont)

    def addCourse(self):
        nuevo_id = (read("curso", "count(*)")[0])[0] + 101
        try:
            curso = Curso(id=nuevo_id, nombre=self.entry.text())
            create("curso", curso.model_dump())
            self.item_created.emit()
            self.close()
        except:
            self.entry.setPlaceholderText("Nombre muy chico o muy grande")
            self.entry.setText("")










class createMajor(baseWindow):
    item_created = pyqtSignal()
    def __init__(self, directorio: str = os.path.dirname(os.path.abspath(__file__))):
        super().__init__("Nueva Carrera", 400, 220, directorio)

        self.line0 = QLabel("Nombre de la carrera", self)
        self.line0.setStyleSheet("color: black;")
        self.line0.setFont(self.ComicNeueFont)
        self.line0.setGeometry(20, 70, 360, 30)

        self.entry = QLineEdit(self)
        self.entry.setGeometry(20, 100, 360, 40)
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

        self.add = QPushButton("Añadir", self)
        self.add.setStyleSheet(
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
        self.add.setGeometry(160, 160, 80, 35)
        self.add.clicked.connect(self.addMajor)
        self.add.setFont(self.ComicNeueFont)

    def addMajor(self):
        nuevo_id = (read("carrera", "count(*)")[0])[0] + 1
        try:
            carrera = Carrera(id=nuevo_id, nombre=self.entry.text())
            create("carrera", carrera.model_dump())
            self.item_created.emit()
            self.close()
        except:
            self.entry.setPlaceholderText("Nombre muy chico o muy grande")
            self.entry.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = enrollStudent()
    win.show()
    sys.exit(app.exec())