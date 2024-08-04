import subprocess
import readfile as mread

servidor = "DKWJLRT\SQLJLRT"
usuario = "semi2"
contraseña = "1234"
base_datos = "semi2practica1"

def menu():
    while True:
        print("\nMenú de Opciones")
        print("a) Borrar modelo")
        print("b) Crear modelo")
        print("c) Extraer información")
        print("d) Cargar información")
        print("e) Realizar consultas")
        print("q) Salir")
        
        opcion = input("Seleccione una opción: ").strip().lower()
        
        if opcion == 'a':
            borrar_modelo()
        elif opcion == 'b':
            crear_modelo()
        elif opcion == 'c':
            extraer_informacion()
        elif opcion == 'd':
            cargar_informacion()
        elif opcion == 'e':
            realizar_consultas()
        elif opcion == 'q':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor seleccione una opción válida.")

def borrar_modelo():
    print("Borrando modelo...")
    comando = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/eliminar_modelo.sql"
    ]
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        print("Modelo eliminado")
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def crear_modelo():
    print("Creando modelo...")
    comando = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/crear_modelo.sql"
    ]
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        print("Modelo creado")
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def extraer_informacion():
    print("Extrayendo información...")
    opcion = input("ingrese la ruta del archivo: ").strip().lower()
    mread.LeerArchivo(opcion)
    print("Información extraída")

def cargar_informacion():
    # Implementar la lógica para cargar información
    print("Cargando información...")

def realizar_consultas():
    # Implementar la lógica para realizar consultas
    print("Realizando consultas...")

# Ejecutar el menú
menu()