#Project Euler 22
file = open("names.txt", "r")
a = sorted(file.read().split())

def nameValue(string):
    return sum([ord(i)-64 for i in list(string)])
ans = 0

for i in a:
    num = a.index(i)+1
    ans += num*(nameValue(i))
print(ans)
