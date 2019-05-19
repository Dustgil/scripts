import math

a = [1,0,-1]
b = [1,0,2]
c = [0,2,2]

li = []

li.append(a)
li.append(b)
li.append(c)


for idx, vector in enumerate(li):
    if idx == 0:
        c = 0
        for e in vector:
            c += e**2
        c = math.sqrt(c)

        v = [x / c for x in vector]
        print(v)
        
        
    
