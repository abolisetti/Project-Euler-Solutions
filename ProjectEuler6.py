#Project Euler 6
cnt=0
cnt2=0
for i in range(0,101):
    cnt+=i**2
for i in range(0,101):
    cnt2+=i
print(cnt-cnt2**2)
