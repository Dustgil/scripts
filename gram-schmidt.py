import math

a = [1,2,0]
b = [1,1,0]
c = [0,0,1]

vectors = []

vectors.append(a)
vectors.append(b)
#vectors.append(c)

orth_vectors = []

for vector in vectors:
    v = vector
    
    for e in orth_vectors:
        component = 0
        for i in range(len(e)):
            component += e[i] * v[i]

        b = [x * component for x in v]
        
        for i in range(len(e)):
            v[i] = v[i] - b[i]

    c = 0
    for e in v:
        c += e**2
    c = math.sqrt(c)

    v = [x / c for x in v]
    orth_vectors.append(v)
        
    
            
print(orth_vectors)



'''
for idx, vector in enumerate(li):
    if idx == 0:
        c = 0
        for e in vector:
            c += e**2
        c = math.sqrt(c)

        v = [x / c for x in vector]
        print(v)
        
'''      
    
