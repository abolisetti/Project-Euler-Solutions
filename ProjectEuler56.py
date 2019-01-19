#Project Euler 56
a = []
def digSum(num):
    return sum([int(i) for i in (list(str(num)))])
#print(digSum(10**100))
a = 0
for i in range(100):
    for j in range(100):
        if digSum(i**j)>a:
            a = digSum(i**j)
print(a)
