import names, re
from random import randint

#### First part ####

list1 = [randint(1, 100) for i in range(100)]

list2 = list1.copy()

for i in range(len(list2)):
    if list2[i] > 50:
        list2[i] = "HIGH"
    else:
        list2[i] = "LOW"

print(list2)

#### Second part ####

namesAll = ([''.join(names.get_first_name()) for i in range(100)])

namesAM = []
namesOther = []
pattern1 = re.compile("[^N-Z]")
pattern2 = re.compile("[^A-M]")

namesAM = list(filter(pattern1.match, namesAll))
namesOther = list(filter(pattern2.match, namesAll))

print(namesAM, "\nTotal names:", len(namesAM))
print(namesOther, "\nTotal names:", len(namesOther))
