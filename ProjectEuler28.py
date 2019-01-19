#Project Euler 28

topRight = sum([i**2 for i in range(3, 1001, 2)])
topLeft = sum([i**2-(i-1) for i in range(3, 1001, 2)])
botRight = sum([i**2-(i-1) for i in range(2, 1001, 2)])
botLeft = sum([i**2+1 for i in range(2, 1001, 2)])

ans = sum([topRight, topLeft, botRight, botLeft])
print(ans-3)
#Got 667167995
