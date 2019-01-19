#Project Euler 9
for a in range(1, 750):
    for b in range(1, 750):
        c=(a**2 + b**2)**0.5
        if a+b+c==1000:
            print(a*b*c)
            break
        #break
