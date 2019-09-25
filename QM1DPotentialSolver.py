import numpy as np
import matplotlib.pyplot as plt

# specify potential function. In future will set this up as an evaluatable
# function of x over the range. The values over the range will be represented
# as an nxn diagonal matrix, where n is the number of steps

def vpot(x):
    return x**2

n = 400 # of steps

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
    plt.plot(x,y, label='{}'.format(i))
    plt.xlabel('x')

plt.legend()
plt.show()
