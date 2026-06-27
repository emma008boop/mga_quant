import sqlite3
import os 

def inicializar_bd():
    os.makedirs('data', exist_ok=True)
    db_path = os.path.join('data', 'mga_database.db')
    
    print(f"Conectando a la base de datos en: {db_path}")
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()
    
    cursor.execute('''PRAGMA foreign_keys = ON''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Conductores (
            id_conductor INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            licencia_comercial TEXT UNIQUE NOT NULL,
            anos_experiencia INTEGER NOT NULL,
            estado_residencia TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Camiones (
            id_camion INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT NOT NULL,
            modelo_ano INTEGER NOT NULL,
            peso_libras REAL NOT NULL,
            millaje_anual REAL NOT NULL,
            dispositivo_telemetria_activo INTEGER DEFAULT 1 -- 1 = Sí, 0 = No
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Polizas_Historicas (
            id_poliza INTEGER PRIMARY KEY AUTOINCREMENT,
            id_conductor INTEGER,
            id_camion INTEGER,
            prima_anual_usd REAL NOT NULL,
            tipo_mercancia TEXT NOT NULL, -- Ej: 'Materiales de construcción' o 'Alimentos'
            siniestros_acumulados_usd REAL DEFAULT 0.0,
            estado_operacion TEXT NOT NULL, -- Ej: 'Texas', 'California'
            FOREIGN KEY (id_conductor) REFERENCES Conductores(id_conductor) ON DELETE CASCADE,
            FOREIGN KEY (id_camion) REFERENCES Camiones(id_camion) ON DELETE CASCADE
        );
    ''')

    conexion.commit()
    conexion.close()
    print("¡Estructura de MGA creada con éxito!")

if __name__ == "__main__":
    inicializar_bd()