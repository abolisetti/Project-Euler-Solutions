#Project Euler 2
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
count=0
i=0

while fib(i)<4000000:
    if (fib(i))%2:
        count+=fib(i)
    i+=1
print(count)
