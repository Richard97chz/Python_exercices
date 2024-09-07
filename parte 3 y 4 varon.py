""" def multiplica(n1, n2):
    resultado=0
    for i in range(n1):
        resultado=resultado+n2
    return resultado

print(multiplica(3,9)) """


""" def extraerNum(text):
    numbers=''
    for i in text:
        if i.isdigit():
            numbers+=i
    return numbers

def sortDigits(numbers):
    sortedDigits=sorted(numbers)
    sortedStringDigits=''.join(sortedDigits)
    return sortedStringDigits

def sumDigits(numbers):
    total=sum(int(number) for number in numbers)
    return total

def showResult(numbers,sortedDigits,total):
    msg=f'''
    Los digitos extraidos son: {numbers}
    Los digitos ordenados de menor a mayor son: {sortedDigits}
    La suma de todos los digitos es: {total}
    '''
    print(msg)

if __name__ == "__main__":
    text = '3h5hf7vbd8scs9ds9d7sds4ds3'
    numbers=extraerNum(text)
    sortedDigits=sortDigits(numbers)
    total=sumDigits(numbers)
    print(total)
    showResult(numbers,sortedDigits,total) """


""" def bubbleSort(arrayNums):
    change=True
    while change:
        change=False
        for num in range(len(arrayNums)-1):
            if arrayNums[num]>arrayNums[num+1]:
                temp=arrayNums[num]
                arrayNums[num]=arrayNums[num+1]
                arrayNums[num+1]=temp
                change=True
    return arrayNums

arrayNums=[2,4,5,1]
result=bubbleSort(arrayNums)

print(result) """


def sortMethod(arrayNums):
    change = True
    while change:
        change = False
        for n in range(len(arrayNums)-1):
            if arrayNums[n] > arrayNums[n+1]:
                temp = arrayNums[n]
                arrayNums[n] = arrayNums[n+1]
                arrayNums[n+1] = temp
                change = True
    return arrayNums


arrayNums = [2, 4, 5, 1]
print(sortMethod(arrayNums))
