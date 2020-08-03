def even(n):
    x = n/2

    return x

def odd(n):
    x = 3*n + 1

    return x

start = 1000000
curiter = 0
maxiter = 0
maxnum = 0
while start >= 1:

    x = start
    
    while x != 1:
        if x % 2 == 0:
            x = even(x)
        else:
            x = odd(x)
        curiter += 1
    
    if curiter > maxiter:
        maxiter = curiter
        maxnum = start
    curiter = 0
    print(start)
    start = start - 1

print(maxnum, maxiter)


    
