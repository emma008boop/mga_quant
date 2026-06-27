import seaborn as sns
import matplotlib.pyplot as plt
'''
    Se encarga de generar graficas 
'''

def graficar_boxplot(df, columna_x, columna_y):
    """
        Grafica un boxplot usando un DF de Pandas 
    """
    plt.figure(figsize=(8, 6))
    
    # crear DF pasandole el DF y las columnas
    sns.boxplot(x=columna_x, y=columna_y, data=df, palette="Set2")
    
    plt.title(f"Distribucion de {columna_x} por {columna_y}")
    plt.xlabel(columna_x, fontsize=12)
    plt.ylabel(columna_y, fontsize=12)
    
    plt.show()
    
