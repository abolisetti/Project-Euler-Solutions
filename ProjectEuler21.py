#Project Euler 21
def factors(n):
    result_set = []
    sqrtn = int(n**0.5)
    for i in range(1,sqrtn+1):
        q, r = n/i, n%i
        if r == 0:
            result_set.append(q)
            result_set.append(i)
    return result_set

def d(num):
    return sum(factors(num))-num

ans = 0
print(d(6),d(28),d(562))

for i in range(10000):
    if i!=d(i):
        if i == d(d(i)) and d(i) == d(d(d(i))):
            ans+=i

print(ans)
        
        
        
        
      


