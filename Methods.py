#Class to perform SN in various discretization methods
#Miriam Kreher 22.212 HW4 (2018)

#Imports
import matplotlib.pyplot as plt
import copy

class Methods():

	def __init__(self):
		self

#######################################################

	def step(self, S, SigmaT, SigmaS, mesh, D, 
		Q, phi, psi1, psi2, psi3, psi4):

		mu1 = 0.8611363115
		mu2 = -mu1
		mu3 = 0.3399810435
		mu4 = -mu3

		for n in range(0,100):
			Q[:] = 0.5*(SigmaS*phi[:]+S)
			for i in range(1,len(mesh)):
				psi1[i] = D*Q[i]/mu1+psi1[i-1]*(1-D*SigmaT/mu1)
				psi2[len(mesh)-1-i] = -D*Q[i]/mu2+psi2[len(mesh)-i]*(1+D*SigmaT/mu2)
				psi3[i] = D*Q[i]/mu3+psi3[i-1]*(1-D*SigmaT/mu3)
				psi4[len(mesh)-1-i] = -D*Q[i]/mu4+psi4[len(mesh)-i]*(1+D*SigmaT/mu4)
			phi[:] = (psi1[:]+psi2[:]+psi3[:]+psi4[:])/Q[:]
			# print phi

		plt.plot(phi)
		plt.savefig('step')


#######################################################

	def charac(self):

		print("hello world2")

#######################################################

	def diamond(self, S, SigmaT, SigmaS, mesh, D, 
		Q, phi, psi1, psi2, psi3, psi4):

		mu1 = 0.8611363115
		mu2 = -mu1
		mu3 = 0.3399810435
		mu4 = -mu3

		for n in range(0,100):
			Q[:] = 0.5*(SigmaS*phi[:]+S)
			for i in range(1,len(mesh)):
				psi1[i] = D*Q[i]/mu1/(1.0+D*SigmaT/2.0/mu1
					)+psi1[i-1]*(mu1-D*SigmaT*0.5)/(mu1+D*SigmaT*0.5)
				psi2[len(mesh)-1-i] = -D*Q[i]/mu2/(1.0-D*SigmaT/2.0/mu2
					)+psi2[len(mesh)-i]*(mu2+D*SigmaT*0.5)/(mu2-D*SigmaT*0.5)
				psi3[i] = D*Q[i]/mu3/(1.0+D*SigmaT/2.0/mu3
					)+psi3[i-1]*(mu3-D*SigmaT*0.5)/(mu3+D*SigmaT*0.5)
				psi4[len(mesh)-1-i] = -D*Q[i]/mu4/(1.0-D*SigmaT/2.0/mu4
					)+psi4[len(mesh)-i]*(mu4+D*SigmaT*0.5)/(mu4-D*SigmaT*0.5)
			phi[:] = (psi1[:]+psi2[:]+psi3[:]+psi4[:])/Q[:]
			# print phi

		plt.plot(phi)
		plt.savefig('diamond')

#######################################################

	def linear_discont(self):

		print("hello world4")