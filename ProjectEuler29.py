#Project Euler 29
ans = []
for a in range(2, 101):
    for b in range(2, 101):
        if a**b not in ans:
            ans.append(a**b)
print(len(ans))
    
