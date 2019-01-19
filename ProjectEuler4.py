#project euler 4

def palindrome(num):
    num=str(num)
    return num == num[::-1]

biggest=[]
for i in range(100,1000):
    for j in range(100,1000):
        if palindrome(i*j):
            biggest.append(i*j)
print(max(biggest))
            
