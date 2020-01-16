# pypyravol - finds the volume of a pyramid of dynamic height and length

# Purpose: Basic exercise to improve comprehension of python scripting

def bitpow(x, n):
    pwr = 1
    while n!=0:
        if (n & 1):
            pwr *= x
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

v = (bitpow(float(a), 2)) / 3
s = square(bitpow(float(h), 2) + (bitpow(float(a)/2, 2)))
area = (s*float(a))/2

txt = "The length of the base of the pyramid is {}"
print(txt.format(a))

txt1 = "The height of the pyramid is {}"
print(txt1.format(h))

txt2 = "The total surface area of the faces is {}"
print(txt2.format(area))

txt3 = "The volume of the pyramid is {}"
print(txt3.format(v))
