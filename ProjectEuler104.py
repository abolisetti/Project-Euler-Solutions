#Project Euler 104
def fib(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]

def panDigCheck(num):
    a = sorted(list(str(num)))
    b = ["1","2","3","4","5","6","7","8","9"]
    return a == b

for i in range(84, 100000):
    a = fib(i)
    print((len(str(fib(i)))), i)
    if panDigCheck(int((str(a))[0:10])) and panDigCheck(int((str(a))[-1:-9])):
        print(i)
        break

    
    

