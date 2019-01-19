#Project Euler 63

def numCheck(num, exp):
    return len(str(num)) == exp
count = 0
for i in range(1, 10000):
    for j in range(1, 1000):
        if numCheck(i**j, j):
            count+=1
            print(count, i**j, j)
    
