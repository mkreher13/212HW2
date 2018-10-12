#22.212 HW2 Miriam Kreher (2018)
#Class to create & operate on geometry and rays

from Plotter import *
from Flux import *
import numpy as np
import random

class Geometry():

	def __init__(self):
		self

######################################################

	def surface(self, r, P):
		
		HalfPitch = P/2.
		self.xRight = HalfPitch
		self.xLeft = -HalfPitch
		self.yTop = HalfPitch
		self.yBottom = -HalfPitch

		self.P = Plotter()
		self.P.pincell(r, P)

######################################################	

	def ray_tracing(self, F, r, P, d_tot, d_mod, d_fuel, iteration, nGrps):
		#New ray
		F.newray(nGrps)


		StartX = random.random()*1.26-0.63
		StartY = random.random()*1.26-0.63
		theta = random.random()*2*np.pi

		# if StartX < r and StartX > -r and StartY < r and StartX < r:
		# 	print("started in circle")
		# print("RAY RAY RAY RAY RAY RAY RAY --------------")

		
		while d_tot < 10:
			# print("theta is ", theta)
			# print("start x and y are: ", StartX, StartY)
			D = []
			d5 = 0
			d6 = 0
			#d1 is distance from right boundary
			d1 = (self.xRight-StartX)/np.cos(theta)
			if d1 > 1e-14:
				D.append(d1)
				# print("d1", d1)
			#d2 is distance from left boundary
			d2 = (self.xLeft-StartX)/np.cos(theta)
			if d2 > 1e-14:
				D.append(d2)
				# print("d2", d2)
			#d3 is distance from top boundary
			d3 = (self.yTop-StartY)/np.sin(theta)
			if d3 > 1e-14:
				D.append(d3)
				# print("d3", d3)
			#d4 is distance from bottom boundary
			d4 = (self.yBottom-StartY)/np.sin(theta)
			if d4 > 1e-14:
				D.append(d4)
				# print("d4", d4)
			#d5 and d6 are distances from circle intersections
			k = StartX*np.cos(theta)+StartY*np.sin(theta)
			c = StartX**2+StartY**2-r**2
			if k**2-c > 0:
				d5 = -k+np.sqrt(k**2-c)
				if d5 > 1e-14:
					D.append(d5)
				d6 = -k-np.sqrt(k**2-c)
				if d6 > 1e-14:
					D.append(d6)

			d = min(D)

			d_tot = d_tot+d
			# print(D)
			# print(d)
			EndX = StartX+d*np.cos(theta)
			EndY = StartY+d*np.sin(theta)
			# print("end x and y are: ", EndX, EndY)

			#Change angle if hitting cell boundary
			#and add segment contribution to distance tallies
			if d == d1 or d == d2:
				theta = -theta+np.pi
				d_mod = d_mod+d
				cell=1
				F.contribute(cell,d,nGrps)
				# print cell, F.phibar
			elif d == d3 or d == d4:
				theta = -theta
				d_mod = d_mod+d
				cell=1
				F.contribute(cell,d,nGrps)
				# print cell, F.phibar
			elif d == d5 or d == d6:
				# print("in circle? ", d5, d6)
				if d5 > 1e-14 and d6 > 1e-14:
					d_mod = d_mod+d
					cell=1
					F.contribute(cell,d,nGrps)
					# print cell, F.phibar
					# print("flag1 ",d)
				else:
					d_fuel = d_fuel+d
					cell=0
					F.contribute(cell,d,nGrps)
					# print cell, F.phibar
					# print("flag2 ",d)

			#Plot rays
			if iteration == 0:
				self.P.rays(StartX, StartY, EndX, EndY)
			StartX = EndX
			StartY = EndY
		# print(F.phibar)


		# print F.psi
		# print("d total is ", d_tot)
		# print("d mod is ", d_mod)
		# print("d fuel is ", d_fuel)
