from PyQt6.QtWidgets import QApplication, QPushButton
from PyQt6.QtCore import pyqtSignal
from baseWin import baseWindow
from create import enrollStudent, createCourse, createMajor
import sys










class createWindow(baseWindow):
    data_changed = pyqtSignal()
    def __init__(self):
        super().__init__(windowTitle="Create", width=500, high=210)
        #9513620620
        self.inscribir_alumno = QPushButton("Inscribir\nalumno", self)
        self.inscribir_alumno.setFont(self.ComicNeueFont)
        self.inscribir_alumno.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.inscribir_alumno.clicked.connect(self.first_option)
        self.inscribir_alumno.setGeometry(35, 50, 130, 140)
        
        self.anadir_materia = QPushButton("Añadir\nmateria", self)
        self.anadir_materia.setFont(self.ComicNeueFont)
        self.anadir_materia.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.anadir_materia.clicked.connect(self.second_option)
        self.anadir_materia.setGeometry(185, 50, 130, 140)
        
        self.anadir_carrera = QPushButton("Añadir\ncarrera", self)
        self.anadir_carrera.setFont(self.ComicNeueFont)
        self.anadir_carrera.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.anadir_carrera.clicked.connect(self.third_option)
        self.anadir_carrera.setGeometry(335, 50, 130, 140)
    def sendSignal(self):
        self.data_changed.emit()
        self.close()
    def first_option(self):
        self.enrollWin = enrollStudent()
        self.enrollWin.item_created.connect(self.sendSignal)
        self.enrollWin.show()
    def second_option(self):
        self.createCourseWin = createCourse()
        self.createCourseWin.item_created.connect(self.sendSignal)
        self.createCourseWin.show()
    def third_option(self):
        self.createMajorWin = createMajor()
        self.createMajorWin.item_created.connect(self.sendSignal)
        self.createMajorWin.show()










class readWindow(baseWindow):
    def __init__(self, windowTitle = "Read", width = 500, high = 300):
        super().__init__(windowTitle, width, high)
        self.alumnos_inscritos = QPushButton("Alumnos\ninscritos", self)
        self.alumnos_inscritos.setFont(self.ComicNeueFont)
        self.alumnos_inscritos.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.alumnos_inscritos.setGeometry(35, 50, 130, 100)
        
        self.lista_cursos = QPushButton("Lista de\ncursos", self)
        self.lista_cursos.setFont(self.ComicNeueFont)
        self.lista_cursos.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.lista_cursos.setGeometry(185, 50, 130, 100)
        
        self.carreras_disponibles = QPushButton("Carreras\ndisponibles", self)
        self.carreras_disponibles.setFont(self.ComicNeueFont)
        self.carreras_disponibles.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.carreras_disponibles.setGeometry(335, 50, 130, 100)
        
        self.informacion_alumno = QPushButton("Información\nde alumno", self)
        self.informacion_alumno.setFont(self.ComicNeueFont)
        self.informacion_alumno.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.informacion_alumno.setGeometry(35, 170, 130, 100)
        
        self.informacion_curso = QPushButton("Información\nde curso", self)
        self.informacion_curso.setFont(self.ComicNeueFont)
        self.informacion_curso.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.informacion_curso.setGeometry(185, 170, 130, 100)
        
        self.planes_estudio = QPushButton("Planes de\nestudio", self)
        self.planes_estudio.setFont(self.ComicNeueFont)
        self.planes_estudio.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.planes_estudio.setGeometry(335, 170, 130, 100)









class updateWindow(baseWindow):
    def __init__(self, windowTitle = "Update", width = 500, high = 300):
        super().__init__(windowTitle, width, high)
        self.informacion_alumno = QPushButton("Información\nde alumno", self)
        self.informacion_alumno.setFont(self.ComicNeueFont)
        self.informacion_alumno.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.informacion_alumno.setGeometry(35, 50, 205, 100)
        
        self.informacion_curso = QPushButton("Información\nde curso", self)
        self.informacion_curso.setFont(self.ComicNeueFont)
        self.informacion_curso.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.informacion_curso.setGeometry(260, 50, 205, 100)
        
        self.plan_estudios = QPushButton("Plan de\nestudios", self)
        self.plan_estudios.setFont(self.ComicNeueFont)
        self.plan_estudios.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.plan_estudios.setGeometry(147, 170, 206, 100)










class deleteWindow(baseWindow):
    def __init__(self, windowTitle = "Delete", width = 500, high = 300):
        super().__init__(windowTitle, width, high)
        self.baja_alumno = QPushButton("Dar alumno\nde baja", self)
        self.baja_alumno.setFont(self.ComicNeueFont)
        self.baja_alumno.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.baja_alumno.setGeometry(35, 50, 205, 100)
        
        self.eliminar_curso = QPushButton("Eliminar\ncurso", self)
        self.eliminar_curso.setFont(self.ComicNeueFont)
        self.eliminar_curso.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.eliminar_curso.setGeometry(260, 50, 205, 100)
        
        self.eliminar_carrera = QPushButton("Eliminar\ncarrera", self)
        self.eliminar_carrera.setFont(self.ComicNeueFont)
        self.eliminar_carrera.setStyleSheet("""
            QPushButton {
                /* Estado Normal */
                background-color: transparent;
                color: black;
                border: 4px solid black;
                border-radius: 15px;
                padding: 5px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                /* Fondo negro y letras blancas */
                background-color: black;
                color: white;

                /* Línea interior blanca */
                border: 4px solid white;

                /* Mantener bordes redondeados */
                border-radius: 15px;
                }
            """)
        self.eliminar_carrera.setGeometry(147, 170, 206, 100)











if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = updateWindow()
    win.show()
    sys.exit(app.exec())