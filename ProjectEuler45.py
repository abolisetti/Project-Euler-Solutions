#Project Euler 45
def triangle(n):
    return n*(n+1)/2
def pentagon(n):
    return n*(3*n-1)/2
def hexagon(n):
    return n*(2*n-1)



triangles = [triangle(i) for i in range(100000)]
pentagons = [pentagon(i) for i in range(100000)]
hexagons = [hexagon(i) for i in range(100000)]


a = set(triangles).intersection(pentagons)
b = set(hexagons).intersection(a)
print(b)
