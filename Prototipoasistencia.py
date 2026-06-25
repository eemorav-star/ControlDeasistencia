# oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# PROTOTIPO REGISTRO DE ASISTENCIA POR GRUPOS
# Tema: Educación - Control de asistencia de estudiantes
# Materia: Herramientas de Programación - UTP
# Integrante: Mora, Elpidio  8-251-827
# oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo



# oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# Entrada
#  LISTAS DE ESTUDIANTES 
# oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

# Tres grupos,  nombres cada uno 
GrupoA = ["Ana Pérez", "Luis Gómez", "Marta Ríos", "Carlos Tuñón", "Sofía Vega"]
GrupoB = ["Eduardo Sáenz", "Iris Bonilla", "Pedro Castillo", "Yariela Quiel"]
GrupoC = ["Diego Herrera", "Camila Ortiz", "Bruno Salas"]

# Lista que va a llevar quienes estan presentes (se llena con append)
Presentes = []


# FUNCION: MOSTRAR MENU DE GRUPOS
def ElegirGrupo():
    print("\n--- SELECCIONE UN GRUPO ---")
    print("1. Grupo A")
    print("2. Grupo B")
    print("3. Grupo C")
    Opcion = input("Ingrese el numero del grupo: ")

    if Opcion == "1":
        return GrupoA, "Grupo A"
    elif Opcion == "2":
        return GrupoB, "Grupo B"
    elif Opcion == "3":
        return GrupoC, "Grupo C"
    else:
        print("Opcion invalida, se usara el Grupo A por defecto.")
        return GrupoA, "Grupo A"
