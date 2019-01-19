#Project Euler 17
digits = 3+3+5+4+4+3+5+5+4 #36
teens = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 #70
a20andUp = 10*(6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8*36 #748
a1to99 = digits + teens + a20andUp #854

ans = digits*100 + a1to99*9 + 7*9 + 9*99*10 + a1to99 + 11
print(ans)

#21124
