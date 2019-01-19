#Project Euler 23
def factors(n):
    result_set = []
    sqrtn = int(n**0.5)
    for i in range(1,sqrtn+1):
        q, r = n/i, n%i
        if r == 0 and r!=q:
            result_set.append(q)
            result_set.append(i)
        elif r == 0 and r!=q:
            result_set.append(q)
    return result_set

def d(num):
    return sum(factors(num))-num
a=[]
for i in range(28123):
    if d(i)>i and i**0.5 != int(i**0.5):
        a.append(i)

ans = 0
for i in range(28123):
    for i in a:
        for j in a:
            check = False
            if i+j == i:
                check = True
            if check:
                ans+=i
                break
                break
                
        
