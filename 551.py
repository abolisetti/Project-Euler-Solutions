def digSum(num):
    return sum([int(i) for i in list(str(num))])

#print(sum([digSum(i) for i in range(10*15)]))

A = [1]
for i in range(101):
    A += [sum([digSum(i) for i in A])]
print(A[101])


A=[1]
for i in range(10**15):
    A = [A[-1], A[-1] + digSum(A[-1])]
print(A[10**15-1])
