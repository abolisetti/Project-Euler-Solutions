#Project Euler 32
def panDigCheck(a, b, c):
    a = sorted(list(str(a) + str(b) + str(c)))
    b = ["1","2","3","4","5","6","7","8","9"]
    return a == b
ans = []
for i in range(1000000):
    for j in range(1000000):
        if panDigCheck(i,j,i*j):
            if i*j not in ans:
                ans.append(i*j)
                print(ans, i*j, i, j, sum(ans))
print(ans)
#ans is 45228
