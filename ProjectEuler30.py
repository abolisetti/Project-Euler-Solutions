#Project Euler 30
def breakAdd(num):
    a = list(str(num))
    ans = 0
    for i in a:
        ans += int(i)**5
    return ans
    #if ans = num
#print(breakAdd(1634), breakAdd(8208), breakAdd(9474))
ans = 0
num = 0
while True:
    if num == breakAdd(num):
        ans+=num
        print(ans-1, num)
    num+=1
