import os
import re
import subprocess

servidor = "DKWJLRT\SQLJLRT"
usuario = "semi2"
contraseña = "1234"
base_datos = "semi2practica1"

def consulta1():
    comando = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta1.sql"
    ]

    comando2 = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta1.sql",
        "-o", "./db/resultados/consulta1.txt"
    ]
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        subprocess.run(comando2, check=True, text=True, capture_output=True)
        cleaned_output = re.sub(r'(\(\d+ rows affected\)\n)+', '', resultado.stdout)
        print(cleaned_output)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def consulta2():
    comando = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta2.sql"
    ]

    comando2 = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta2.sql",
        "-o", "./db/resultados/consulta2.txt"
    ]
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        subprocess.run(comando2, check=True, text=True, capture_output=True)
        cleaned_output = re.sub(r'(\(\d+ rows affected\)\n)+', '', resultado.stdout)
        print(cleaned_output)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def consulta3():
    comando = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta3.sql"
    ]

    comando2 = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta3.sql",
        "-o", "./db/resultados/consulta3.txt"
    ]
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        subprocess.run(comando2, check=True, text=True, capture_output=True)
        cleaned_output = re.sub(r'(\(\d+ rows affected\)\n)+', '', resultado.stdout)
        print(cleaned_output)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def consulta4():
    comando = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta4.sql"
    ]

    comando2 = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta4.sql",
        "-o", "./db/resultados/consulta4.txt"
    ]
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        subprocess.run(comando2, check=True, text=True, capture_output=True)
        cleaned_output = re.sub(r'(\(\d+ rows affected\)\n)+', '', resultado.stdout)
        print(cleaned_output)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def consulta5():
    comando = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta5.sql"
    ]

    comando2 = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta5.sql",
        "-o", "./db/resultados/consulta5.txt"
    ]
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        subprocess.run(comando2, check=True, text=True, capture_output=True)
        cleaned_output = re.sub(r'(\(\d+ rows affected\)\n)+', '', resultado.stdout)
        print(cleaned_output)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def consulta6():
    comando = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta6.sql"
    ]

    comando2 = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta6.sql",
        "-o", "./db/resultados/consulta6.txt"
    ]
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        subprocess.run(comando2, check=True, text=True, capture_output=True)
        cleaned_output = re.sub(r'(\(\d+ rows affected\)\n)+', '', resultado.stdout)
        print(cleaned_output)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def consulta7():
    comando = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta7.sql"
    ]

    comando2 = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta7.sql",
        "-o", "./db/resultados/consulta7.txt"
    ]
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        subprocess.run(comando2, check=True, text=True, capture_output=True)
        cleaned_output = re.sub(r'(\(\d+ rows affected\)\n)+', '', resultado.stdout)
        print(cleaned_output)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def consulta8():
    comando = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta8.sql"
    ]

    comando2 = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta8.sql",
        "-o", "./db/resultados/consulta8.txt"
    ]
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        subprocess.run(comando2, check=True, text=True, capture_output=True)
        cleaned_output = re.sub(r'(\(\d+ rows affected\)\n)+', '', resultado.stdout)
        print(cleaned_output)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def consulta9():
    comando = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta9.sql"
    ]

    comando2 = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta9.sql",
        "-o", "./db/resultados/consulta9.txt"
    ]
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        subprocess.run(comando2, check=True, text=True, capture_output=True)
        cleaned_output = re.sub(r'(\(\d+ rows affected\)\n)+', '', resultado.stdout)
        print(cleaned_output)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def consulta10():
    comando = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta10.sql"
    ]

    comando2 = [
        "sqlcmd",
        "-S", servidor,
        "-U", usuario,
        "-P", contraseña,
        "-d", base_datos,
        "-i", "./db/scripts/consultas/consulta10.sql",
        "-o", "./db/resultados/consulta10.txt"
    ]
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        subprocess.run(comando2, check=True, text=True, capture_output=True)
        cleaned_output = re.sub(r'(\(\d+ rows affected\)\n)+', '', resultado.stdout)
        print(cleaned_output)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def menu_consultas():
    ruta_salida = './db/resultados/'
    if not os.path.exists(ruta_salida):
        os.makedirs(ruta_salida)
    while True:
        print("\nSelecciona una consulta")
        print("1) Consulta1")
        print("2) Consulta2")
        print("3) Consulta3")
        print("4) Consulta4")
        print("5) Consulta5")
        print("6) Consulta6")
        print("7) Consulta7")
        print("8) Consulta8")
        print("9) Consulta9")
        print("10) Consulta10")
        print("q) Regresar")
        
        opcion = input("Seleccione una opción: ").strip().lower()
        if opcion == '1':
            consulta1()
        elif opcion == '2':
            consulta2()
        elif opcion == '3':
            consulta3()
        elif opcion == '4':
            consulta4()
        elif opcion == '5':
            consulta5()
        elif opcion == '6':
            consulta6()
        elif opcion == '7':
            consulta7()
        elif opcion == '8':
            consulta8()
        elif opcion == '9':
            consulta9()
        elif opcion == '10':
            consulta10()
        elif opcion == 'q':
            print("Regresando...")
            break
        else:
            print("Opción no válida, por favor seleccione una opción válida.")

