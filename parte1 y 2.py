
"""
#MAYOR DE 2 NÚMEROS
def funcion_max(n1, n2):
    if n1>n2:
        return n1
    else:
        return n2

print(funcion_max(300,3))
 """


""" 
#MAYOR DE 3 NÚMEROS
def max_de_tres(a,b,c):
    if a > (b and c):
        return a
    elif b > (a and c):
        return b
    else:
        return c

print(max_de_tres(19,22,20)) """


""" 
#DEVOLVER TRUE SI EL CARACTER ES VOCAL
def is_vocal(caracter):
    vocales=['a','e','i','o','u']
    if caracter in vocales:
        return True
    else:
        return False

print(is_vocal('f')) """


""" 
#SUMA LOS VALORES DE UNA LISTA
def funcion_sum(lista):
    suma=0
    for i in lista:
        suma=suma+(i)
    print(suma)

funcion_sum([1,2,3,4])  """


""" 
#MULTIPLICA LOS VALORES DE UNA LISTA
def funcion_mult(lista):
    result=lista[0]
    i=1
    while i in range(1, len(lista)):
        result=result*lista[i]
        i=i+1
    print(result)

funcion_mult([1,2,3,4])  """


""" 
#INVERSA DE UNA CADENA DE CARACTERES
def inversa(cadena):
    tamanio=-(len(cadena)-1)
    nueva_cadena=str()
    for n in range(tamanio,1):
        n=abs(n)
        nueva_cadena+=cadena[n]
    print(nueva_cadena)
inversa('richard') """


""" 
#VERIFICAR SI UNA PALABRA ES PALINDROMA
def inversa(cadena):
    tamanio=-(len(cadena)-1)
    nueva_cadena=str()
    for i in range(tamanio,1):
        i=abs(i)
        nueva_cadena=nueva_cadena+cadena[i]
    return nueva_cadena

def es_palindromo(cadena):
    nueva_cadena = inversa(cadena)   
    if nueva_cadena == cadena:
        return True

print(es_palindromo('radar')) """


""" def superposicion(lista1, lista2):
    for elem in lista1:
        for elem2 in lista2:
            if elem == elem2:
                return True
    return False

print(superposicion([1, 5, 3], [6, 4, 5])) """

""" for elem in lista1:
        if elem in lista2:
            return True
    return False """


""" def generar_n_caracteres(caracter,n):
    string=caracter
    for i in range(1,n):
        string+=caracter
    
    print(string)
generar_n_caracteres('f',2) """


""" def generar_n_caracteres(caracter,n):
    string=caracter
    print(caracter*n)
generar_n_caracteres('abc',2) """
"""     for i in range(1,n):
        string=string+caracter
    print(string) """


""" def procedimiento(lista):
    for n in lista:
        histograma='*' * n
        print(f'{histograma} \n')
procedimiento([6,7,4])
 """
