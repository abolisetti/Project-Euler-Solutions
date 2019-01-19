#Project Euler 12
def factors(n):
    result_set = set()
    sqrtn = int(n**0.5)
    for i in range(1,sqrtn+1):
        q, r = n/i, n%i
        if r == 0:
            result_set.add(q)
            result_set.add(i)
    return len(result_set)
    
def triangleNum(num):
    return sum([i for i in range(num+1)])
num=0
print(triangleNum(12375))
print(factors(76576500))
while True:
    if (factors(triangleNum(num)))>499:
        print(num)
        break
    num+=1
    #print(num, factors(triangleNum(num)))

