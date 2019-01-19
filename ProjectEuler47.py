#Project Euler 47

from Euler import *

ci = 1
nf = 4
ns = 4		
n = 2*3*5*7	
while ci != ns:
    n += 1
    if len(factor(n)) == nf:
        ci += 1
    else:
        ci = 0

print(n-nf + 1)
