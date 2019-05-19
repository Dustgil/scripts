import math

a = [1,0,0]
b = [1,0,2]
c = [0,2,2]

li = []

li.append(a)
li.append(b)
li.append(c)


v1 = li[0]
c = 0

for e in v1:
    c += e**2
print(c)

c = math.sqrt(c)
print(c)

v1 = [x / c for x in v1]

print(v1)
