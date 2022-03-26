string1 = " This is a string. "
string2 = " This is a another string. "
print(string1 + string2)

##########
print(len(string1))
print(len(string2))
print(string1.title())
print(string2.lower())
print(string1.upper())
print(string2.rstrip())
print(string1.lstrip())
print(string2.strip())
print(string1.strip(' '))

###########
d = "qwerty123"
ch1 = d[5]
ch2 = d[1:]
ch3 = d[:5]
ch4 = d[1:5:2] # не понятно
ch5 = d[2:8]
print(ch1, ch2, ch3, ch4, ch5)

#########
param = "string" + str(15)
print(param)

###########
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print('{0} plus {1} = {2}'.format(n1,n2,n3)) # не понятно

##########
a = 1/3
print("{:7.3f}".format(a))
print(a)

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

#######
list1 = [82,8,23,97,92,44,17,39,11,12]
(dir(list1))

#####
dict = {}
while (True):
    print('Enter key (empty enter - exit):')
    key = input()
    if key == '':
        break
    print('Enter value:')
    value = input()
    dict[key] = value
print(dict)