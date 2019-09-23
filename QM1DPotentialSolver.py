import numpy as np
import matplotlib.pyplot as plt

# specify potential function. In future will set this up as an evaluatable
# function of x over the range. The values over the range will be represented
# as an nxn diagonal matrix, where n is the number of steps

def vpot(x):
    return x**2

n = 1000 # of steps

a = -10 # left wall position
b = 10 # right wall position

# create discrete steps along x-axis

x = np.linspace(a,b,n)

delx = x[1] - x[0] # step spacing


# create T matrix

T = np.zeros((n-2)**2).reshape(n-2,n-2)

for i in range(n-2):
    for j in range(n-2):
        if i==j:
            T[i,j] = -2
        elif np.abs(i-j) == 1:
            T[i,j] = 1
        else:
            T[i,j] = 0

# create V matrix

V = np.zeros((n-2)**2).reshape(n-2,n-2)

for i in range(n-2):
    for j in range(n-2):
        if i==j:
            V[i,j] = vpot(x[i+1])
        else:
            V[i,j] = 0


# construct hamiltonian

H = -T/(2*(delx)**2) + V

print(H)

# calculate n-2 energies and eigenfunctions

val, vec = np.linalg.eig(H)

# vectors and values arent in order, so sort indices by ascending energy
# to get correct eigenfunctions
z = np.argsort(val)

# specify range of eigenfunctions to graph
z = z[0:4]

# normalize and print energies for z
energy_levels = (val[z]/val[z][0])
print(energy_levels)


plt.figure(figsize=(8,6))

# plot each eigenfunction. must append zero to both ends (boundary conditions)
for i in range(len(z)):
    y = []
    y = np.append(y,0)
    y = np.append(y,vec[:,z[i]])
    y = np.append(y,0)
    plt.plot(x,y)

plt.show()

'''
plt.figure(figsize=(8,6))
for i in range(len(z)):
    y = []
    y = np.append(y,vec[:,z[i]])
    y = np.append(y,0)
    y = np.insert(y,0,0)
    plt.plot(x,y,lw=3)
plt.show()


y = []
y = np.append(y,vec[:,0])
y = np.append(y,0)
y = np.insert(y,0,0)
plt.plot(x,y)
plt.show()



# calculated second derivative operator (using 3-point finite differences method)
n = 500 # number of steps

a = 0
b = 1
#delx = (b-a)/n


# create a linspace for x values
#x_values = []

x_values = np.linspace(a,b,n)
delx = x_values[1] - x_values[0]

x = a
for _ in range(n):
    x_values.append(x)
    x += delx


lists = []
# test!!! changed n-2 to n-4, may need to be changed back and n to n-2

# create first row
li = []
element = (2/((delx)**2))
li.append(element)
element = (-1)/((delx)**2)
li.append(element)
for _ in range(n-4):
    li.append(float(0))

lists.append(li)

# create middle n-2 rows
for row in range(n-4):
    li = []
    for e in range(n-2):
        if (e-1) == row:
            element = (2/((delx)**2))
        elif (e-1) == (row-1) or (e-1) == (row+1):
            element = (-1)/((delx)**2)
        else:
            element = 0
        li.append(element)
    lists.append(li)

# create last row
li = []
for _ in range(n-4):
    li.append(0)
element = (-1)/((delx)**2)
li.append(element)
element = (2/((delx)**2))
li.append(element)
lists.append(li)

diff = np.array(lists)
diff = np.divide(diff, -2)




potential = np.zeros(((n-2)**2)).reshape(n-2,n-2)
for i in range(n-2):
    for j in range(n-2):
        if i==j:
            potential[i,j] = vpot(x_values[i+1])
        else:
            potential[i,j] = 0



# specify potential function.
V = "0"


potential_list = []

point = delx
for row in range(n):
    sub = "(" + str(point) + ")"
    pot_at_point = V.replace('x', sub)
    value = eval(pot_at_point)

    li = []
    for e in range(n):
        if e == row:
            li.append(value)
        else:
            li.append(0)

    potential_list.append(li)

    point += delx

potential = np.array(potential_list)


hamiltonian = np.add(diff, potential)

print(hamiltonian)
print(potential)

eig, vec = np.linalg.eig(hamiltonian)

print(eig)

x_values = x_values[:-2]
plt.plot(x_values, vec[:,2])
plt.show()




    
            
        

'''
