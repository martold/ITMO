year = int(input("Put the interest year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, " - is the High Year")
else:
    print(year, " - is not the High Year")