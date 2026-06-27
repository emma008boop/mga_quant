## El Proyecto: "MGA-Quant: Sistema Inteligente de Suscripción y Gestión de Flotas"

Vas a simular que eres el Lead Data Scientist de una **MGA (Managing General Agent)** de seguros que asegura camiones de carga comercial en EE. UU., y que además utiliza técnicas de _Trading_ y optimización de datos para gestionar el riesgo del portafolio.

A medida que avances en el plan de estudios, irás construyendo los módulos de este sistema.

### Módulo 1 (Mes 1): El Corazón de los Datos (EDA & SQL)

- **Lo que haces:** Diseñas una base de datos local en SQLite que simule la operación de la MGA. Creas tres tablas: `Conductores`, `Camiones` y `Polizas_Históricas`.
    
- **Tu entregable de este mes:** Un script de Python que se conecta a SQL, extrae los datos y genera un reporte estadístico automatizado.
    
    - _Estadística:_ Usas `pandas` y `numpy` para sacar las medias de las primas y la volatilidad de los siniestros.
        
    - _Visualización:_ Usas `seaborn` para crear la campana de Gauss de las edades de los conductores y detectar si hay un "outlier" (como un conductor de 120 años o de 12 años).
        

### Módulo 2 (Mes 2): El Evaluador Estadístico de Riesgo

- **Lo que haces:** Empiezas a aplicar distribuciones reales a los datos de la MGA para predecir el comportamiento del portafolio.
    
- **Tu entregable de este mes:** Un script de inferencia estadística.
    
    - _Poisson:_ Calculas cuál es la probabilidad de que la MGA reciba más de 5 reclamos de camiones en una sola semana.
        
    - _Bayes:_ Calculas la probabilidad condicional de que un camión choque dado que opera en rutas de Texas bajo clima adverso.
        
    - _Intervalos de confianza:_ Generas un reporte que le diga a la junta directiva: _"Estamos 95% seguros de que el costo promedio por choque este año estará entre $4,800 y $5,200"_.
        

### Módulo 3 (Mes 3): El Validador de Hipótesis de Negocio

- **Lo que haces:** En lugar de asumir cosas sobre el negocio, las pruebas científicamente cruzando datos avanzados con SQL (`JOINs` y funciones de ventana).
    
- **Tu entregable de este mes:** Un módulo de testeo A/B y pruebas de hipótesis.
    
    - _T-Test:_ Pruebas formalmente la hipótesis: ¿Los camiones que transportan mercancía pesada (Materiales de construcción) generan reclamos significativamente más caros que los de mercancía ligera (Alimentos)?
        
    - _Chi-Cuadrado:_ Analizas si el estado donde opera el camión (Texas, California, Florida) es independiente o está ligado al tipo de cobertura que eligen.
        

### Módulo 4 (Mes 4): El Cotizador Automático (Regresión)

- **Lo que haces:** Pasas de analizar el pasado a predecir el futuro mediante álgebra lineal y regresiones.
    
- **Tu entregable de este mes:** El motor predictivo de precios (Tarificador).
    
    - _Regresión Múltiple:_ Creas un modelo con `Scikit-Learn` donde metes las variables del camión (Años de experiencia del chofer, peso del camión, millaje anual) y el algoritmo predice automáticamente el **precio exacto de la prima** que se le debe cobrar.
        
    - _Evaluación:_ Calculas el RMSE para poder decir: _"Nuestro modelo calcula el precio de la póliza con un margen de error promedio de apenas $25"_.
        

### Módulo 5 (Mes 5): El Filtro Anti-Fraude y Retención (Clasificación)

- **Lo que haces:** Implementas modelos de Machine Learning para tomar decisiones binarias (Sí/No).
    
- **Tu entregable de este mes:** El Pipeline automatizado de clasificación y el Dashboard final.
    
    - _Regresión Logística / Árboles:_ Creas un modelo que predice la probabilidad de que un cliente cancele su póliza el próximo mes (_Churn_) y otro que detecte reclamos potencialmente fraudulentos (1 = Fraude, 0 = Legítimo).
        
    - _Matriz de Confusión:_ Optimizas el modelo para reducir los Falsos Negativos (dejar pasar un fraude es muy costoso para la MGA).