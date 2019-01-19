#Project Euler 52
def numberCheck(num):
    a = sorted(list(str(num)))
    b = sorted(list(str(num*2)))
    if a == b:
        b = sorted(list(str(num*3)))
        if a == b:
            b = sorted(list(str(num*4)))
            if a == b:
                b = sorted(list(str(num*5)))
                if a == b:
                    b = sorted(list(str(num*6)))
                    if a == b:
                        return True
num = 1   
while True:
    if numberCheck(num):
        print(num)
    num+=1
