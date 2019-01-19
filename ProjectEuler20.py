#Project Euler 20
def factorial(num):
    a = 1
    for i in range(1, num+1):
        a*=i
    return a
def sumDigits(num):
    ans = list(str(num))
    ans = sum([int(i) for i in ans])
    return ans

print(sumDigits(factorial(100)))
