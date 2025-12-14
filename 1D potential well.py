#investigate on the potential types
#@Harindranath Ambalampitiya
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi,sqrt
from numpy import linalg as LA
import scipy.integrate as integrate
sq2=sqrt(2.)
#description of the basis
###############################################################################
#define a function to compute the normalized Harmonic oscillator wavefunctions
#take in the order, alpha=(m*omega) and point of evaluation
#size of the Harmonic function basis
nsize=40
omega=1.
m=1.
#maximum length along x
xmax=sqrt(2.*(nsize+.5)/(m*omega))*1.5
alpha=m*omega
def harmonicfun(x,n):
    chi=sqrt(alpha)*x
    f_1=0.
    f0=np.exp(-chi**2/2.)*(alpha/pi)**0.25
    fn=f0
    for i in range(1,n+1):
        fn=(chi*sq2*f0-sqrt(i-1)*f_1)/sqrt(i)
        f_1=f0
        f0=fn
    return fn
#print some Harmonic functions
#harm=np.zeros(ndiv)
#for i in range(0,ndiv):
#    harm[i]=harmonicfun(xarr[i],0)
#fig2=plt.figure(2)
#plt.plot(xarr,harm)
###############################################################################
#potential function
def potential(x):
    vx=0.1382*(np.exp(-0.8507*x)-1)**2
    return vx
#############################################################################
#number of divisions along x
ndiv=1000
xarr=np.linspace(-xmax,xmax,num=ndiv)
#to print the potential
vpot=np.zeros(ndiv)
for i in range(0,ndiv):
    vpot[i]=potential(xarr[i])
#fig1=plt.figure(1)
#plt.plot(xarr,vpot)
#plt.xlabel('x (a.u.)')
#plt.ylabel('V(x) (a.u.)')
#plt.grid()
###############################################################################
# define a function to compute the products of Harmonic functions and the 
# residue of the potential function
def hproduct(x,m,n):
    vharm=0.5*omega*omega*x**2
    vpot=potential(x)
    vdiff=vpot-vharm
    vint=harmonicfun(x,m)*harmonicfun(x,n)*vdiff  
    return vint
###############################################################################
#Now construct the Hamiltonian matrix 
#size of the square matrix
H_mat=np.zeros((nsize,nsize))
for i in range(0,nsize):
    for j in range(0,nsize):
        temp=integrate.quad(hproduct,-xmax,xmax,args=(i,j),limit=100)
        H_mat[i,j]=temp[0]
        if i==j:
            H_mat[i,j]=H_mat[i,j]+(j+.5)*omega
eigen_E,eigen_V=LA.eig(H_mat)
#sorting according to the ascending order of energies
idx=np.argsort(eigen_E)
eigen_E=eigen_E[idx]
eigen_V=eigen_V[:,idx]
#print the  wavefunctions
#number of functions and eigen energies to print
iprintw=2
iprinte=5
wave_g=np.zeros((iprintw,ndiv))
for k in range(0,iprintw):    
    for i in range(0,ndiv):
        totw=0.
        for j in range(0,nsize):
            totw=totw+eigen_V[j][k]*harmonicfun(xarr[i],j)
        wave_g[k,i]=totw
fig3=plt.figure(1)
plt.subplots_adjust(wspace=1)
plt.subplot(1,3,1)
plt.plot(xarr,vpot,color='black')
plt.xlabel('x (a.u.)')
plt.ylabel('V(x) (a.u.)')
plt.axis([-2,4,0,2])

plt.subplot(1,3,2)
for k in range(0,iprinte):  
    plt.axhline(y=eigen_E[k], color='b', linestyle='-')
plt.ylabel('Energy Spectrum (a.u)')
plt.xticks([])
plt.yticks(eigen_E[:iprinte])  

plt.subplot(1,3,3)
for k in range(0,iprintw):   
    plt.plot(xarr,wave_g[k],label='n=%s'%k)
plt.xlabel('x (a.u.)')
plt.ylabel('\u03C6 (x)')
plt.legend()
plt.savefig('1dsq_morse.pdf',bbox_inches = "tight")

