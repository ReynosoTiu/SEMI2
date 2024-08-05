import pandas as pd # type: ignore
import pyodbc# type: ignore
import sys

def LeerArchivo(ruta_archivo):
    # Configura la conexión a la base de datos
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DKWJLRT\SQLJLRT;'
        'DATABASE=semi2practica1;'
        'UID=semi2;'
        'PWD=1234'
    )

    # Leer el archivo CSV usando pandas
    archivo_csv = ruta_archivo
    df = pd.read_csv(archivo_csv)
    df['Departure Date'] = pd.to_datetime(df['Departure Date'], errors='coerce')

    # Crear una tabla temporal en la base de datos
    create_table_query = """
    USE semi2practica1;
    IF NOT EXISTS (
        SELECT * 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_NAME = 'PassengerDataTemp'
    )
    BEGIN
        CREATE TABLE PassengerDataTemp (
            passenger_id varchar(40),
            first_name varchar(100),
            last_name varchar(100),
            gender varchar(10),
            age int,
            nationality varchar(100),
            airport_name varchar(100),
            airport_country_code varchar(50),
            country_name varchar(100),
            airport_continent varchar(10),
            continents varchar(50),
            departure_date date,
            arrival_airport varchar(10),
            pilot_name varchar(100),
            flight_status varchar(20)
        );
    END
    ELSE
    BEGIN
        TRUNCATE TABLE PassengerDataTemp;
    END
    """

    # Ejecutar el comando de creación de tabla
    with conn.cursor() as cursor:
        cursor.execute(create_table_query)
        conn.commit()

    # Insertar datos en la tabla temporal
    insert_query = """
    INSERT INTO PassengerDataTemp (
        passenger_id, first_name, last_name, gender, age, nationality,        
        airport_name, airport_country_code, country_name, airport_continent,
        continents, departure_date, arrival_airport, pilot_name, flight_status
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    total_filas = len(df)
    with conn.cursor() as cursor:
        for index, row in df.iterrows():
            cursor.execute(insert_query, row.tolist())
            if index % 2500 == 0 or index == total_filas - 1:
                percent_complete = (index + 1) / total_filas * 100
                sys.stdout.write(f'\rProgreso: {percent_complete:.2f}%')
                sys.stdout.flush()
        print()
    conn.commit()
    conn.close()