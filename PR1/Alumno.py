class Alumno:
    def __init__(self, nombre="", apellido="", dni=0, correo=""):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__correo = correo

    # NOMBRE
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    #APELLIDO
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    #DNI
    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    #CORREO
    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self, correo):
        self.__correo = correo

    def consultar_datos(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nDNI: {self.dni}\nCorreo: {self.correo}"

    def mostrar_alumnoo(self):
        print("Datos de alumno:")
        print("Nombre: " + self.nombre)
        print("Apellido: " + self.apellido)
        print("DNI: " + str(self.dni))
        print("Correo: " + self.correo)


def mostrar_alumno(alumno):
    print("\nDatos del alumno:")
    print(alumno.consultar_datos())

def crear_alumno():
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el primer apellido: ")
    dni = input("Introduce el DNI: ")
    correo = input("Introduce el correo electrónico: ")

    return Alumno(nombre, apellido, dni, correo)

# Prueba del código
#alumno = Alumno()
#alumno.mostrar_alumnoo()
#alumno = crear_alumno()
#mostrar_alumno(alumno)