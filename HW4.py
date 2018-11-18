#22.212 HW4 Miriam Kreher (2018)
#SN methods

#Imports
from Methods import *
import numpy as np

#Variables
S = 1.0          #[n/cm2/s]
SigmaT = 1.0     #[cm-1]
SigmaS = 0.5     #[cm-1]
length = 50.0    #[cm]
n = 200
delta = length/n

#Iterations
mesh = np.linspace(0,length,n+1)
Q = np.zeros(len(mesh))
phi = np.zeros(len(mesh))
psi1 = np.zeros(len(mesh))
psi2 = np.zeros(len(mesh))
psi3 = np.zeros(len(mesh))
psi4 = np.zeros(len(mesh))
# print(delta)
# print(mesh)

M = Methods()
phi[:] = 1
M.step(S, SigmaT, SigmaS, mesh, delta, 
	Q, phi, psi1, psi2, psi3, psi4)
# M.charac()
M.diamond(S, SigmaT, SigmaS, mesh, delta, 
	Q, phi, psi1, psi2, psi3, psi4)
# M.linear_discont()
