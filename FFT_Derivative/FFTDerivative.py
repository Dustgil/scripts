import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [12,12]
plt.rcParams.update({'font.size': 18})

# define variables
n = 1000
L = 50
dx = L/n

x = np.arange(-L/2,L/2,dx, dtype='complex_')
f = np.cos(x) * np.exp(-np.power(x,2)/25)
df = -(np.sin(x) * np.exp(-np.power(x,2)/25) + (2/25)*x*f)



# approximate derivative with FFT
fhat = np.fft.fft(f)
kappa = (2*np.pi/L)*np.arange(-n/2,n/2)
kappa = np.fft.fftshift(kappa)  #re-order fft frequencies to match

dfhat = kappa * fhat * (1j)
dfFFT = np.real(np.fft.ifft(dfhat))

# plot results. plotting f with df may not work out well due to scaling differences so be careful.
plt.plot(x,df.real, '--', color='r', LineWidth=2, label='True Derivative')
plt.plot(x,dfFFT.real, '--', color='c', LineWidth=1.5, label='FFT Derivative')
#plt.plot(x,f.real, '--',color='r', LineWidth=2, label='Original Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
