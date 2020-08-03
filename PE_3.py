num = 
curdiv = 2
maxdiv = 0

l = True
while l:
    print(num, curdiv)
    if num % curdiv == 0:
        maxdiv = curdiv
        num = (num / curdiv)
        curdiv = 2
    else:
        curdiv += 1
    if num == 1:
        l = False

print(maxdiv)
        
    
