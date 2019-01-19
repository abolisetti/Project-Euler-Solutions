#Project Euler 42
def triangle(n):
    return n*(n+1)/2
triangles = [triangle(i) for i in range(1000)]


def nameValue(string):
    return sum([ord(i)-64 for i in list(string)])

file = open("words.txt", "r")
a = file.read().split()
count = 0
for i in a:
    #print(i)
    if nameValue(i) in triangles:
        count+=1
        print(i)
print(count)
    

#ans is 162
