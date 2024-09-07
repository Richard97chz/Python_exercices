# 1 kata 8
""" def greet(name):
    greet=f"Hello, {name} how are you doing today?"
    return greet """


# 2 kata 8
""" def check_the_bucket(bucket):
    if 'gold' in bucket:
        return True
    return False """


# 3 kata 8
""" def remove_char(s):
    result=s[1:-1]
    return result """

# 4 kata 7
""" 
#DE NUMEROS SEPARADOS POR ESPACIOS SACAR EL MAX Y MIN  ("1 3 2 7 5 -2")
def high_and_low(numbers):
    withoutSpace=numbers.split(' ')
    newArray=[]
    for num in withoutSpace:
        newArray.append(int(num))
    newArray.sort()
    return f'{newArray[-1]} {newArray[0]}' """


# 5 kata 7
""" 
#DE UNA LISTA DEVUELVE LOS DIGITOS NO PRESENTES (23, 18, 4)
def unused_digits(*numbers):
    result= ''
    numbersString=str(numbers)
    cleanDigits=numbersString.replace(' ','').replace(',','')
    
    for num in range(0,10):
        if str(num) not in cleanDigits:
            result+=str(num)
        
    return result """


def unused_digits(*numbers):
    result = ''
    nummbersString = str(numbers)
    cleanDigits = nummbersString.replace(' ', '').replace(',', '')

    for num in range(0, 10):
        if str(num) not in cleanDigits:
            result += str(num)

    return result


print(unused_digits([23, 18, 45]))


# 5 kata7 mi intento
""" def digits(list):
    elements = ''
    for n in range(len(list)):
        elements += str(list[n])
        n += 1
    return elements


def missingDigits(elements):
    result = ''
    for num in range(0, 10):
        if str(num) not in elements:
            result += str(num)
    return result


list = [23, 45, 98]
elements = digits(list)
print(missingDigits(elements)) """


# 6 kata 6
""" def solution(number):
    result=0
    for num in range(1,number):
        if (num%3==0) or (num%5==0):
            result+=num
    return result """

# 7 kata 7
""" def get_sum(a,b):
    maximum=max(a,b)
    minimum=min(a,b)
    sumTotal=0
    for num in range(minimum,maximum+1):
        sumTotal+=num
    return sumTotal """
