#Project Euler 34
def factorial(num):
    ans = 1
    for i in range(1, num+1):
        ans *= i
    return ans
def breakFact(num):
    num = list(str(num))
    ans = 0
    for n in num:
        ans += factorial(int(n))
    return ans
ans = 0
for i in range(3, 1000000):
    if breakFact(i) == i:
        print(i)
        ans+=i
print(ans)
        
        
