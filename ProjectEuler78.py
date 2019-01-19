#Project Euler 78
def fact(num):
    a = 1
    for i in range(1, num+1):
        a *= i
    return a
def p(n):
    return fact(n)/fact(n-1)
for i in range(5):
    print(fact(i))
