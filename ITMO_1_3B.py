from syslog import LOG_WARNING
import names
from random import randint

list1 = [randint(1, 100) for i in range(10)]
print(list1)

list2 = list1.copy()

for i in range(len(list2)):
    if i > 50:
        i = "HIGH"
    else:
        i = "LOW"

print(list2)

