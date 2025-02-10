class Alumno:
    def __init__(self, nombre, apellido, dni, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.correo = correo

    def consultar_datos(self):
        return f"Nombre: {self.nombre} {self.apellido}\nDNI: {self.dni}\nCorreo: {self.correo}"


def crear_alumno():
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el primer apellido: ")
    dni = input("Introduce el DNI: ")
    correo = input("Introduce el correo electrónico: ")

    return Alumno(nombre, apellido, dni, correo)


def mostrar_alumno(alumno):
    print("\nDatos del alumno:")
    print(alumno.consultar_datos())


# Prueba del código
alumno_nuevo = crear_alumno()
mostrar_alumno(alumno_nuevo)