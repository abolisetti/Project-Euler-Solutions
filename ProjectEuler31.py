#Project Euler 31
def breakAdd(num):
    num = list(str(num))
    ans = 0
    for n in num:
        ans+= (int(i))**5
    return ans
ans = 0
for i in range(2, 1000000):
    if i == breakAdd(i):
        ans+=i
print(ans)
    
