from Alumno import*
from AlumnoIA import *


nombreFichero = "2-datos.txt"
modo = "rt"
vector_alumnos = []
fichero = open(nombreFichero, modo)

lineas = fichero.readlines()

for linea in lineas:
    dato = linea.strip().split(",")
    dni,correo = dato[1], dato[2]
    dato_nombre = dato[0].rstrip()
    partes = dato_nombre.rsplit(" ", 1)
    nombre,apellido = partes
    vector_alumnos.append(Alumno(nombre.strip(), apellido.strip(), int(dni.strip()), correo.strip()))

fichero.close()

for alumno in vector_alumnos:
    mostrar_alumno(alumno)

archivo_impares = "impares.txt"

with open(archivo_impares, "w") as salida:
    for alumno in vector_alumnos:
        if alumno.dni % 2 != 0:  # Verificar si es impar
                salida.write(f"{alumno.nombre} {alumno.apellido}, {alumno.dni}, {alumno.correo}\n")
print(f"Archivo '{archivo_impares}' creado .")