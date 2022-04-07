### 1 part ###
import numpy

def averageTemperature(*data):
    TemperatureListClear = list(filter(None, data))
    averageTemperature = numpy.average(TemperatureListClear)
    return round(averageTemperature, 2)

result1 = averageTemperature(5, 6, -19, None, -5, 7, 8, -4.5, None, 9, 2.4)
print(result1)

### 2 part ###
def digitsArray(*digits):
    positiveDigits = []
    negativeDigits = []
    for i in digits:
        if i > 0:
            positiveDigits.append(i)
            #positiveDigits = tuple(positiveDigits)
        else:
            negativeDigits.append(i)
            #negativeDigits = tuple(negativeDigits)
    return sorted(positiveDigits), sorted(negativeDigits, reverse=True)

result2 = digitsArray(5, 6, -19, -5, 7, 8, -4.5, 9, 2.4)
print(result2)

### 3 part ###
def digitExponentiation(a, n):
    result = 1
    for i in range (abs(n)):
        result *= a
    if n < 0:
        result = 1 / result
    elif n == 0:
        result = 1
    return result

result3 = digitExponentiation(4, -5)
print(result3)

def digitExponentiation1(a, n):
    if n > 0:
        return (a * digitExponentiation1(a, n - 1))
    else:
        return 1
a = int(input("Введите число: "))
n = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", digitExponentiation1(a, n))