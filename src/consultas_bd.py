import sqlite3
import os 
import pandas as pd

def consultar_db():

    db_path = os.path.join('data', 'mga_database.db')
    
    try:
        conexion = sqlite3.connect(db_path)
        
        query = "SELECT * FROM Conductores"
        
        df_conductores = pd.read_sql_query(query, conexion)
        
        conexion.close()
        
        print("Datos de conductores cargados")
        print(df_conductores.head())

        return df_conductores
    
    except sqlite3.OperationalError as e:
        
        print(f"Error al conectar a la base de datos: {e}")
        return None
    
def simular_e_inyectar_datos():
    
    db_path = os.path.join('data', 'mga_database.db')
        
    conexion, cursor = sqlite3.connect(db_path), conexion.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM Conductores")
    if cursor.fetchone()[0] > 0:
        conexion.close()
        return


    nombres = ["John Doe", "Michael Smith", "Carlos Rodriguez", "David Jones", "James Wilson"]
    estados = ["TX", "CA", "FL", "NY", "GA"]
    
    conductores_data = []
    for i in range(20):
        nombre = random.choice(nombres) + f" {i}"
        edad = random.randint(25, 65) 
        if i == 5: 
            edad = 120 
            
        conductores_data.append((
            nombre, 
            edad, 
            f"CDL-{random.randint(10000, 99999)}", 
            random.randint(1, 30), 
            random.choice(estados)
        ))
        
    cursor.executemany('''
        INSERT INTO Conductores (nombre, edad, licencia_comercial, anos_experiencia, estado_residencia)
        VALUES (?, ?, ?, ?, ?);
    ''', conductores_data)

    marcas = ["Freightliner", "Peterbilt", "Kenworth", "Volvo"]
    camiones_data = [
        (random.choice(marcas), random.randint(2015, 2024), random.uniform(30000, 80000), random.uniform(50000, 120000), 1)
        for _ in range(20)
    ]
    cursor.executemany('''
        INSERT INTO Camiones (marca, modelo_ano, peso_libras, millaje_anual, dispositivo_telemetria_activo)
        VALUES (?, ?, ?, ?, ?);
    ''', camiones_data)

    mercancias = ["Materiales de construcción", "Alimentos", "Electrónicos", "Químicos"]
    polizas_data = []
    for i in range(1, 21):
        # Prima promedio de camiones en EE.UU. ronda los $8,000 - $15,000
        prima = random.uniform(7000, 16000)
        # Siniestros: algunos chocan (tienen costo), muchos no chocan (costo 0)
        siniestro = random.choice([0.0, 0.0, random.uniform(1500, 25000)])
        
        polizas_data.append((i, i, prima, random.choice(mercancias), siniestro, random.choice(estados)))

    cursor.executemany('''
        INSERT INTO Polizas_Historicas (id_conductor, id_camion, prima_anual_usd, tipo_mercancia, siniestros_acumulados_usd, estado_operacion)
        VALUES (?, ?, ?, ?, ?, ?);
    ''', polizas_data)

    conexion.commit()
    conexion.close()

