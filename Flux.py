#22.212 Miriam Kreher (2018)
#Class to calculate flux contributions

import numpy as np
import copy

class Flux():

	def __init__(self,r,P, nGrps):
		self.q = np.array([[0.22/4/np.pi,0.5/4/np.pi],[0.15/4/np.pi,4.0/4/np.pi]])
		self.scat = np.array([[0.2,0.4,0.4,1.8],[0,0.3,0,2.1]])
		self.vol = np.array([np.pi*r**2,P**2-np.pi*r**2])
		self.tot = np.array([[0.27,0.93],[0.27,3.6]])
		self.chi = np.array([[0.763,0.0],[0.0,0.0]])
		self.nufiss = np.array([[0.027,0.98],[0.0,0.0]])
		self.oldphi = np.array([[0.22/4/np.pi,0.5/4/np.pi],[0.15/4/np.pi,4.0/4/np.pi]])

######################################################

	def newray(self, nGrps):
		self.deltapsi = np.array([[0.0,0.0],[0.0,0.0]])
		self.psi = copy.copy(self.q)


######################################################

	def contribute(self, cell, s, nGrps):
		# print("new segment here ------------------")

		for g in range(0, nGrps):
			# print("new energy group here --------------------")
			self.deltapsi[cell,g] = self.psi[cell,g]
			self.psi[cell,g] = self.psi[cell,g]*np.exp(-self.tot[cell,g]*s
				)+self.q[cell,g]/self.tot[cell,g]*(1-np.exp(-self.tot[cell,g]*s))
			self.deltapsi[cell,g] = self.deltapsi[cell,g]-self.psi[cell,g]

			self.phibar[cell,g] = self.q[cell,g]/self.tot[cell,g]+1/(
				self.tot[cell,g]*self.vol[cell])*self.deltapsi[cell,g]

		# print self.phibar

		# for g in range(0,2):
		# 	print("new line here --------------------")
		# 	print g, cell
		# 	print self.phibar

		# 	self.fisssrc[cell,g] = sum(self.phibar[cell,:]*self.nufiss[cell,:])
		# 	print self.fisssrc
		# 	# print(sum(self.fisssrc[cell,:]))

		# 	# self.q[cell,g] = 1/(4*np.pi)*(self.chi[cell,g])