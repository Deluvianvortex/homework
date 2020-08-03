num = 0
l = True

def isPalindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False


for x in range(999, 100, -1):
    print(x)
    for y in range(999, 100, -1):
        z = x * y
        if z > num:
            if isPalindrome(z):
                num = z
print(num)
        
    
