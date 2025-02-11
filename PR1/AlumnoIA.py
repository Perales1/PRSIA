from Alumno import Alumno

class Alumno_IA(Alumno):
    def __init__(self, nombre, apellido, dni, correo, grupo_teoria, grupo_practicas):
        super().__init__(nombre, apellido, dni, correo)
        self.__grupo_teoria = grupo_teoria
        self.__grupo_practicas = grupo_practicas
        self.__notas_practicas = [0, 0, 0, 0]

    @property
    def grupo_teoria(self):
        return self.__grupo_teoria

    @grupo_teoria.setter
    def grupo_teoria(self, grupo_teoria):
        self.__grupo_teoria = grupo_teoria

    @property
    def grupo_practicas(self):
        return self.__grupo_practicas

    @grupo_practicas.setter
    def grupo_practicas(self, grupo_practicas):
        self.__grupo_practicas = grupo_practicas

    @property
    def notas_practicas(self):
        return self.__notas_practicas

    @notas_practicas.setter
    def notas_practicas(self, notas_practicas):
        self.__notas_practicas = notas_practicas

    def consultar_datos(self):
        datos = super().consultar_datos()
        return f"{datos}\nGrupo de Teoría: {self.grupo_teoria}\nGrupo de Prácticas: {self.grupo_practicas}"

    def leer_notas_practicas(self):
        print("Introduce las notas de las prácticas 1, 2, 3 y 4:")
        for i in range(4):
            self.notas_practicas[i] = float(input(f"Nota práctica {i + 1}: "))

        media_practicas = sum(self.notas_practicas) / 4
        print(f"La media de las notas de las prácticas es: {media_practicas:.2f}")
        return media_practicas

def crear_alumno_IA():
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el primer apellido: ")
    dni = input("Introduce el DNI: ")
    correo = input("Introduce el correo electrónico: ")
    grupo_teoria = input("Introduce el grupo de teoría: ")
    grupo_practicas = input("Introduce el grupo de prácticas: ")

    return Alumno_IA(nombre, apellido, dni, correo, grupo_teoria, grupo_practicas)

def mostrar_alumno_IA(alumno):
    print("\nDatos del alumno de IA:")
    print(alumno.consultar_datos())
    alumno.leer_notas_practicas()

#alumno_IA_nuevo = crear_alumno_IA()
#mostrar_alumno_IA(alumno_IA_nuevo)