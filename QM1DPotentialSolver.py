import numpy as np
import matplotlib.pyplot as plt

# specify potential function. In future will set this up as an evaluatable
# function of x over the range. The values over the range will be represented
# as an nxn diagonal matrix, where n is the number of steps

V = 0

# calculated second derivative operator (using 3-point finite differences method)
n = 45 # number of steps

a = 0
b = 100
delx = (b-a)/n


# create a linspace for x values
x_values = []

x = a
for _ in range(n):
    x_values.append(x)
    x += delx


lists = []


# create first row
li = []
element = (2/((delx)**2))
li.append(element)
element = (-1)/((delx)**2)
li.append(element)
for _ in range(n-2):
    li.append(float(0))

lists.append(li)

# create middle n-2 rows
for row in range(n-2):
    li = []
    for e in range(n):
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
for _ in range(n-2):
    li.append(0)
element = (-1)/((delx)**2)
li.append(element)
element = (2/((delx)**2))
li.append(element)
lists.append(li)

diff = np.array(lists)

# specify potential function.
V = "0"


potential_list = []

point = a
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

eig, vec = np.linalg.eig(hamiltonian)

plt.plot(x_values, vec[:,3])
plt.show()




    
            
        

