#Project Euler 5
count=0
def check(num):
    checkList=[20,19,18,17,16,14,13,11]
    checks=True
    for i in checkList:
        if num%i!=0:
            checks=False
            break
    return checks
numb=0
while True:
    numb+=20
    if check(numb):
        print(numb)
        break
    
