#Project Euler 25
def fib_to(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]
n = 0
while True:
    if len(str(fib_to(n))) == 1000:
        print(n)
        break
    n+=1
    #print(n, fib_to(n))
