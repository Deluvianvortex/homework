def triNum(x):
    y = 0
    for n in range(1, x+1):
        y+=n
    return y

def divisors(x):
    y = 0
    if x == 1: return 1
    
    for n in range(1, int(x/2)):
        if x%n == 0:
            y+=1
    return y+1


