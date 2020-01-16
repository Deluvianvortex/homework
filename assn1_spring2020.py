# PerleyP1

# Programmer (scripter): Michael Perley

# E-Mail: mperley2@cnm.edu

# Purpose: Basic exercise to improve comprehension of python scripting

def bitpow(n, p):
    pwr = 1
    while n!=0:
        if (n & 1):
            pwr *= n
        n = n >> 1
        x = x * x
    return pwr
    
def square(n):
    x = n
    y = 1
    e = 0.00000000000001
    while (x - y > e):
        x = (x + y) / 2
        y = n / x
    return x

a = input("Please Enter the length of the base of the pyramid: ")
h = input("Please Enter the height of the pyramid: ")

v = bitpow(a, 2) / 3
s = square(bitpow(h, 2) + (bitpow(a/2, 2)))
area = s*a/2

print(