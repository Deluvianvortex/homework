i = 0
j = 0
for n in range(1, 101):
    i += n**2

for z in range(1, 101):
    j+=z

j = j**2

print(j - i)
