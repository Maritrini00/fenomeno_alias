#Realizar un programa en python que calcule las frecuencias (aliadas o no) de los componentes de una señal especificando una frecuencia de muestreo.  
import math
def calcularFrecuencia(components, fs, fmin, fmax):
    n = 1 #inicializando n igual a 1
    result = 0
    result_list = [] # lista de las frecuencias vacia
    if not components:
        return result_list # si no hay componentes la lista se regresa vacia
    #para cada componente en la lista de componentes
    for component in components:
        result = component/ (2*math.pi) #la frecuencia se calcula dividiente entre 2pi
        #si el resultado es mayor o menor al limite del ancho de banda (frecuencia aliada)
        while result > fmax or result < fmin:
            #se suplanta la frecuencia aliada
            result = abs(result - (n)(fs)) # se resta el resultado de la frecuencia menos el producto de n por la frecuencia de muestreo
            n =+ 1 # se incrementa el numero de n en uno
        result_list.append(result) # se anexan las frecuencias en la lista resulatnte
    return result_list

if __name__ == '__main__':
    input_componentes = input("introduce las frecuencias de las componentes de la señal separadas por un espacio: ")
    lista_componentes = input_componentes.split()
    lista_componentes = [int(num) for num in lista_componentes]
    input_frec_muestreo = input("introduce la frecuencia de muestreo: ")
    frec_muestreo = int(input_frec_muestreo)
    input_frec_minima = input("introduce la frecuencia minima: ")
    frec_minima = int(input_frec_minima)
    input_frec_maxima = input("introduce la frecuencia maxima: ")
    frec_maxima = int(input_frec_maxima)
    result = calcularFrecuencia(lista_componentes,frec_muestreo,frec_minima,frec_maxima)
    print("Resultado de la las frecuencias en Hz: ",result)