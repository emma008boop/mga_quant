# MGA-Quant: Sistema Inteligente de Suscripción y Gestión de Flotas

MGA-Quant es una plataforma modular de ciencia de datos y aprendizaje automático (Machine Learning) diseñada para la gestión integral del riesgo en el sector de seguros de transporte de carga comercial en Estados Unidos. 

A través de un enfoque puramente cuantitativo, el sistema simula de extremo a extremo las funciones de una dirección de datos dentro de una Agencia General Administradora (MGA), optimizando los procesos críticos de suscripción, tarificación predictiva y mitigación de pérdidas financieras.

El objetivo principal de la plataforma es transformar datos históricos operativos en un activo estratégico para la toma de decisiones, garantizando la estabilidad y rentabilidad del portafolio mediante la aplicación de rigor estadístico y algoritmos predictivos avanzados.

---

## Competencias Técnicas Demostradas en el Proyecto

* **Ciencia de Datos y ML:** Modelos de regresión múltiple, clasificación supervisada, optimización de métricas (RMSE), análisis exploratorio (EDA).
* **Estadística Avanzada:** Pruebas de hipótesis paramétricas (T-Student), pruebas de independencia (Chi-Cuadrado), distribuciones de probabilidad (Poisson), Teorema de Bayes e intervalos de confianza.
* **Ingeniería de Datos:** Diseño de bases de datos relacionales, optimización de consultas SQL, automatización de pipelines y scripts ETL.
* **Conocimiento de Dominio (InsurTech):** Modelado de riesgo de seguros, cálculo de primas comerciales y análisis de siniestralidad.

---

## Tecnologías Utilizadas

| Categoría | Tecnologías y Librerías |
| :--- | :--- |
| **Lenguaje de Programación** | Python |
| **Gestión y Almacenamiento de Datos** | SQLite, SQL, Pandas, NumPy |
| **Modelado Estadístico y Machine Learning** | Scikit-Learn, SciPy, Statsmodels |
| **Visualización y Reportes** | Matplotlib, Seaborn |

---

## Arquitectura y Estructura Operativa del Sistema

El desarrollo de la plataforma se estructuró de manera limpia, modular y secuencial, garantizando la escalabilidad del código.

### Módulo 1: Infraestructura de Datos y Análisis Exploratorio (EDA)
*Enfoque: Establecimiento del ecosistema de datos y auditoría inicial de la información.*
* **Diseño Relacional:** Implementación de un modelo de base de datos local en SQLite que integra y normaliza las entidades de Conductores, Camiones y Pólizas Históricas.
* **Automatización de Pipelines:** Desarrollo de scripts optimizados en Python para la extracción dirigida mediante consultas SQL complejas y el cálculo automatizado de métricas de tendencia central y volatilidad de siniestros.
* **Control de Calidad de Datos:** Análisis de distribución e identificación sistemática de registros anómalos (outliers) o fuera de rango mediante herramientas de visualización estadística.

### Módulo 2: Inferencia y Evaluación Estadística de Riesgo
*Enfoque: Cuantificación matemática de la probabilidad de ocurrencia de eventos críticos.*
* **Modelado de Frecuencia:** Aplicación de la distribución de Poisson para proyectar matemáticamente la probabilidad de acumulación de reclamaciones semanales.
* **Análisis Condicional:** Uso del Teorema de Bayes para evaluar probabilísticamente el incremento del riesgo operativo bajo variables concurrentes, tales como rutas geográficas específicas y condiciones climáticas adversas.
* **Estimación Financiera:** Construcción de intervalos de confianza robustos para delimitar con alta certeza estadística el costo promedio esperado por siniestro, sirviendo de base para la toma de decisiones de la junta directiva.

### Módulo 3: Validación Científica de Hipótesis de Negocio
*Enfoque: Sustentación empírica de las reglas de negocio mediante técnicas de contraste estadístico.*
* **Pruebas de Hipótesis Paramétricas:** Implementación de pruebas T de Student para determinar con significancia estadística si la naturaleza de la carga transportada influye de forma directa en el costo final de los siniestros.
* **Análisis de Independencia:** Evaluación de tablas de contingencia mediante pruebas de Chi-Cuadrado para verificar y validar la correlación existente entre las regiones geográficas de operación y las coberturas seleccionadas por los clientes.

### Módulo 4: Motor Predictivo de Tarificación
*Enfoque: Automatización del cálculo de primas comerciales basado en el perfil de riesgo del asegurado.*
* **Modelado de Regresión:** Desarrollo de un algoritmo de regresión múltiple que procesa variables técnicas del vehículo y el historial del conductor para generar cotizaciones precisas, personalizadas y dinámicas.
* **Métricas de Evaluación:** Optimización del modelo mediante el cálculo del Error Cuadrático Medio (RMSE) para asegurar la proximidad matemática entre la predicción algorítmica y el costo real del riesgo.

### Módulo 5: Modelos de Clasificación y Retención de Cartera
*Enfoque: Desarrollo de mecanismos de protección institucional mediante decisiones automatizadas.*
* **Detección de Fraude y Riesgo de Fuga:** Implementación de modelos de clasificación supervisada para identificar patrones de comportamiento anómalos en los siniestros y optimizar las estrategias de retención de cartera de clientes de alto valor.

---

## Instrucciones de Instalación y Uso

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/MGA-Quant.git](https://github.com/tu-usuario/MGA-Quant.git)
