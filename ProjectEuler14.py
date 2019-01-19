#Project Euler 14

def collatz(num):
    chain = 1
    while num != 1:
        num = num/2 if num%2==0 else num*3 + 1
        chain += 1
        if num == 1:
            return chain
            break        
a = (0, 0)
for i in range(1000000):
    ans = collatz(i)
    if ans>a[0]:
        a[0] = ans
        a[1] = i
print(a)
#ans is 837799, 525
    
