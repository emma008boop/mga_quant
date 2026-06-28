import math

def calcular_promedio(lista): 
    """
        Calcula el promedio de una lista de datos
    """
    if not lista:
        raise ValueError("la lista no puede estar vacia para calcular el promedio")
    return sum(lista) / len(lista) 

def calcular_variacion_estandar_muestra(lista):
    """
        Calcula la variacion estandar de una lista en base a una muestra de la poblacion
    """
    
    sigma = 0
    cantidad_num = len(lista)
    promedio = calcular_promedio(lista)
    for n in lista:
        sigma += (n - promedio) ** 2
    return math.sqrt(sigma / (cantidad_num - 1))
        
def calcular_coheficiente_pearson(lista1, lista2):

    if not lista1 or not lista2:
        return "Las listas no deben esta vacias"
    
    if not len(lista1) == len(lista2):
        return "Las listas no tienen el mismo numero de datos"
    
    if len(lista1) < 5 or len(lista2) < 5:
        return "Las listas deben de tener al menos mas de 5 numeros" 
    

    sigma_covarianza = 0
    promedio_l1, promedio_l2 = calcular_promedio(lista1), calcular_promedio(lista2)
    
    for n_l1, n_l2 in zip(lista1, lista2):
        diferencia_l1 = n_l1 - promedio_l1
        diferencia_l2 = n_l2 - promedio_l2
        
        sigma_covarianza += diferencia_l1 * diferencia_l2
        sumatoria_l1_potenciada += diferencia_l1 ** 2
        sumatoria_l2_potenciada += diferencia_l2 ** 2
        
    raiz = math.sqrt(sumatoria_l1_potenciada * sumatoria_l2_potenciada)
    
    if raiz == 0:
        return 0.0
    
    return sigma_covarianza / raiz


if __name__ == "__main__":
    lista = [10, 12, 23, 23, 16, 23, 21, 16]
    
    resultado = calcular_variacion_estandar_muestra(lista)
    
    print(f"La variación estándar de la muestra es: {resultado}")
