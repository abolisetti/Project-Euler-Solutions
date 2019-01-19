#Project Euler 71
from fractions import Fraction
ans = []
ans2 = []
for i in range(1, 1000000):
    for j in range(1, i):
        if j/i not in ans2:
            ans.append(str((j/i,str(Fraction(j, i)))))
            ans2.append(j/i)
        
ans = sorted(list(ans))
ans2 = sorted(list(ans2))
a = ans2.index(1/3)
b = ans2.index(1/2)
print(ans[b:a])
#print(sorted(ans))
