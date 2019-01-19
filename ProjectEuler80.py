#Project Euler 80
from decimal import *
getcontext().prec = 100
a = list(str((Decimal(2).sqrt())*10**99))

print(sum([int(i) for i in a])-int(a[0]))

def squareCheck(num):
    return num**0.5 == int(num**0.5)

checks = [i for i in range(101) if not squareCheck(i)]
answer = 0
for i in checks:
    a = list(str((Decimal(i).sqrt())*10**99))
    answer += sum([int(i) for i in a])-int(a[0])
print(answer)
