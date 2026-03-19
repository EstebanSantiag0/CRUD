import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.conexion_2

estudiantes = src.conexion_2.read("estudiante", "LEFT(matricula, 4), count(*)", "group by LEFT(matricula, 4) order by LEFT(matricula, 4)")
estudiantes = dict(zip(estudiantes[0], estudiantes[1]))

def test_student_count(anio : str = '2024'):
    count = 0
    if('2027' in estudiantes):
        count = estudiantes.get(anio)
        estudiantes.update({anio: estudiantes.get('2027') + 1})
    else:
        count = 0
        estudiantes[anio] = 1
    return count

print(test_student_count('2027'))
print(test_student_count('2027'))
print(test_student_count('2027'))
print(test_student_count('2027'))
print(test_student_count('2027'))
