import math 


#Solicto ingreso de un string
pal = input('Ingrese una palabra:  ')

diccionario = {}

#Funcion que contabiliza la cantidad de cada letra

def contador_letras(pal):
    for letra in pal:
        if letra in diccionario:
            diccionario[letra]=diccionario[letra]+1
        else:
            diccionario[letra]=1
    return diccionario

#Funcion que analiza los numeros

def es_primo(numero):
    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo
    # En este loop, empezamos por el dos hasta un numero anterior a el, por lo
    # que si en el loop, alguna vez se divide el numero, quiere decir que no es
    # primo
    if (numero<=1):
        return False
 
    for i in range(2, math.ceil(math.sqrt(numero))+1):
        if(numero%i==0 and i!=numero):
            return False
    return True
 
#comienza el programa

diccionario = contador_letras(pal)

for letra in diccionario:
    numero = diccionario[letra]
    if es_primo(numero):
        print(letra,'aparece un numero primo de veces')
exit()
# No tuve dificultades con la resolucion pero quisiera saber
# si es conveniente o posible transformar en clases las funciones para importarlas
# Sobre el uso de exit() yo lo implemente para terminar la conclusion, ¿hay
# otras formas de hacerlo? o ¿es correcto como lo aplique en esta situacion?
		
			
	
