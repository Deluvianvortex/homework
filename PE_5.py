def check(n):
    for x in range(11, 21):
        if n % x != 0:
            return False
    return True

n = 2520
while not check(n):
    print(n)
    n = n + 2520

print(n)

    
        
    
        
