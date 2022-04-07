### 1 part ###
import numpy

# def averageTemperature():
#     TemperatureList = []
#     # TemperatureValue = (input("Enter the Temperature with ',' separator:"))
#     # for value in TemperatureValue:
#     #     TemperatureList = list(sep=',')
#     averageTemperature = numpy.average(TemperatureList)
#     print(averageTemperature)

# averageTemperature(1, 2, 3)

# TemperatureValue = int(input("Enter the Temperature with ',' separator:"))
# def averageTemperature(*args):
#     TemperatureList = []
#     TemperatureListClear = []
#     for i in TemperatureList:
#         if i != 'None':
#             TemperatureListClear.append(i)
#     print(TemperatureListClear)

#     averageTemperature = numpy.average(TemperatureListClear)
#     print(round(averageTemperature, 2))

# averageTemperature(5, 6, 7, 8, 'None', 9, 2.4, -10)
# for i in TemperatureList:
#     if i != 'None':
#         TemperatureListClear.append(i)


def averageTemperature(*data):
    TemperatureListClear = list(filter(None, data))
    print(str(TemperatureListClear))
    averageTemperature = numpy.average(TemperatureListClear)
    print(round(averageTemperature, 2))

averageTemperature(5, 6, -19, None, -5, 7, 8, -4.5, None, 9, 2.4)





### 2 part ###


### 3 part ###5