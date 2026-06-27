def calcular__promedio(cantidad_num, suma_datos): 
    return suma_datos / cantidad_num 

def calcular_variacion_estandar_muestra(lista):
    sigma = 0
    cantidad_num = len(lista)
    suma_datos = sum(lista)
    for n in lista:
        sigma += (n - calcular__promedio(cantidad_num, suma_datos)) ** 2
    return (sigma / (cantidad_num - 1)) ** 0.5
        


if __name__ == "__main__":
    lista = [10, 12, 23, 23, 16, 23, 21, 16]
    
    resultado = calcular_variacion_estandar_muestra(lista)
    
    print(f"La variación estándar de la muestra es: {resultado}")
