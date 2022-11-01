#frequency multiplex

import numpy as np
import matplotlib.pyplot as plt

# array mirroring
def mirror(a):
    out = list(a[::-1])
    out.extend(a[1:])
    return out

f=np.linspace(-200,201,400)

# 3 random signals
X1=80*(np.heaviside(f+80,1)-np.heaviside(f-80,1))
X2=(f+140)*(np.heaviside(f+140,1)-np.heaviside(f,1))+(-f+140)*(np.heaviside(f,1)-np.heaviside(f-140,1))
X3=(-f)*(np.heaviside(f+100,1)-np.heaviside(f,1))+(f)*(np.heaviside(f,1)-np.heaviside(f-100,1))

# drawing signals
plt.figure(1)
plt.plot(f,X1,'b') 
plt.xlabel("f(Hz)")
plt.ylabel("|X1(f)|")
plt.title("Spectre of random signal X1")
plt.grid()

plt.figure(2)
plt.plot(f,X2,'b') 
plt.xlabel("f(Hz)")
plt.ylabel("|X2(f)|")
plt.title("Spectre of random signal X2")
plt.grid()

plt.figure(3)
plt.plot(f,X3,'b') 
plt.xlabel("f(Hz)")
plt.ylabel("|X3(f)|")
plt.title("Spectre of random signal X3")
plt.grid()

f=np.linspace(0,500,501)
Bg=50

# right side of all signals
Xm1=80*(np.heaviside(f,1)-np.heaviside(f-80,1))
Xm2=(-f+80+Bg+140)*(np.heaviside(f-80-Bg,1)-np.heaviside(f-80-Bg-140,1))
Xm3=(f-80-Bg-140-Bg)*(np.heaviside(f-80-Bg-140-Bg,1)-np.heaviside(f-80-Bg-140-Bg-100,1))

Xm=Xm1+Xm2+Xm3

plt.figure(4)
plt.plot(f,Xm,'b')
plt.xlabel("f(Hz)")
plt.ylabel("|Xfdm(f)|")
plt.title("Spectre of signal Xfdm(f) after AM USSB modulation with Bg=50Hz")
plt.grid()

f=np.linspace(0,25000,25001)

# mirroring right side to get left side
Xdsb=mirror(Xm)

# shifting signal for 20 000Hz
pomak=[0]*19500
Xdsb=pomak+Xdsb
pomak=[0]*4500
Xdsb=Xdsb+pomak

# end result
plt.figure(5)
plt.plot(f,Xdsb,'b')
plt.xlabel("f(Hz)")
plt.ylabel("|Xdsb-am(f)|")
plt.title("Spectre of signal Xdsb-am(f)")
plt.xlim([19500,20500])
plt.grid()