#22.212 HW2 Miriam Kreher (2018)
#MOC

from Geometry import *

rays = 10
fuel_rad = 0.4
pitch = 1.26
nGrps = 2

G = Geometry()
G.surface(fuel_rad, pitch)

F = Flux(fuel_rad, pitch, nGrps)
k = 1.0
for iteration in range(0,100):
	# print("ITERATION -----------")
	random.seed(1)
	F.phibar = np.array([[0.0,0.0],[0.0,0.0]])
	for ray in range(0,rays):
		d_tot = 0
		d_mod = 0
		d_fuel = 0
		G.ray_tracing(F, fuel_rad, pitch, d_tot, d_mod, d_fuel, iteration, nGrps)
	if iteration == 0:
		G.P.end()
	#Update k
	power = sum(F.oldphi[:,:]*F.nufiss[:,:])
	NEWpower = sum(F.phibar[:,:]*F.nufiss[:,:])
	k = sum(NEWpower)/sum(power)*k

	#Update q
	# print F.q
	nuf_rate = F.phibar[:,:]*F.nufiss[:,:]
	scatsrc = np.array([[0.0,0.0],[0.0,0.0]])
	# inscat_rate = F.phibar[:,:]* 
	for cell in range(0,2):
		for g in range(0,nGrps):
			# print F.scat[:,g+nGrps*cell]
			# print F.phibar[cell,:]
			# print F.scat[:,g+nGrps*cell]*F.phibar[cell,:]
			# print sum(F.scat[:,g+nGrps*cell]*F.phibar[cell,:])
			scatsrc[cell,g] = sum(F.scat[:,g+nGrps*cell]*F.phibar[cell,:])
	# print scatsrc

	# print(fissrate)
	# print(sum(power))
	for cell in range(0,2):
		for g in range(0,nGrps):
			# print(sum(fissrate[cell,:]))
			F.q[cell,g] = 1./4./np.pi*(F.chi[cell,g]/k*sum(nuf_rate[cell,:])+scatsrc[cell,g])
	F.oldphi = copy.copy(F.phibar)

	F.q[:] = F.q[:]/np.linalg.norm(F.q)


	print k

