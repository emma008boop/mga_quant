MGA-Quant: Sistema Inteligente de Suscripción y Gestión de Flotas

El proyecto MGA-Quant es una plataforma modular de ciencia de datos y aprendizaje automático diseñada para la gestión integral del riesgo en el sector de seguros de transporte de carga comercial en Estados Unidos. A través de un enfoque cuantitativo, el sistema simula las funciones de una dirección de datos dentro de una agencia general administradora (MGA), optimizando los procesos de suscripción, tarificación predictiva y mitigación de pérdidas financieras.

El objetivo principal es transformar datos históricos operativos en un activo estratégico para la toma de decisiones, garantizando la estabilidad del portafolio mediante la aplicación de rigor estadístico y modelos predictivos.

Estructura Operativa del Proyecto
El desarrollo del sistema se divide en cinco módulos secuenciales, pero la arquitectura se mantiene limpia con nombres claros


Módulo 1: Infraestructura de Datos y Análisis Exploratorio
Establecimiento de las bases de datos y auditoría inicial de la información.

Diseño Relacional: Implementación de un modelo de base de datos local en SQLite que integra las entidades de Conductores, Camiones y Pólizas Históricas.

Automatización de Reportes: Desarrollo de scripts en Python para la extracción dirigida mediante consultas SQL y el cálculo de métricas de tendencia central y volatilidad de siniestros.

Control de Calidad: Análisis de distribución e identificación de registros anómalos o fuera de rango mediante herramientas de visualización estadística.

Módulo 2: Inferencia y Evaluación Estadística de Riesgo
Cuantificación matemática de la probabilidad de ocurrencia de eventos críticos.

Modelado de Frecuencia: Aplicación de la distribución de Poisson para proyectar la probabilidad de acumulación de reclamaciones semanales.

Análisis Condicional: Uso del teorema de Bayes para evaluar el incremento del riesgo operativo bajo variables concurrentes como rutas específicas y condiciones climáticas adversas.

Estimación Financiera: Construcción de intervalos de confianza para delimitar con alta certeza el costo promedio esperado por siniestro ante la junta directiva.

Módulo 3: Validación Científica de Hipótesis de Negocio
Sustentación empírica de las reglas de negocio mediante técnicas de contraste estadístico.

Pruebas de Hipótesis Paramétricas: Implementación de pruebas T de Student para determinar si la naturaleza de la carga transportada influye significativamente en el costo de los siniestros.

Análisis de Independencia: Evaluación de contingencia mediante pruebas de Chi-Cuadrado para verificar la correlación entre las regiones geográficas de operación y las coberturas seleccionadas.

Módulo 4: Motor Predictivo de Tarificación
Automatización del cálculo de primas comerciales basado en el perfil de riesgo del asegurado.

Modelado de Regresión: Desarrollo de un algoritmo de regresión múltiple que procesa variables del vehículo y del conductor para generar cotizaciones precisas y personalizadas.

Métricas de Evaluación: Optimización del modelo mediante el cálculo del error cuadrático medio (RMSE) para asegurar la proximidad matemática entre la predicción y el costo real del riesgo.

Módulo 5: Modelos de Clasificación y Retención de Cartera
Desarrollo de mecanismos de protección institucional mediante decisiones binarias automatizadas.

Detección de Fraude: Implementación de modelos de clasificación