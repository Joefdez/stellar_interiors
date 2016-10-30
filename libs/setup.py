from numpy import array, genfromtxt

model_name = 'solar model'
int_scheme = 'RK4'
grid_points = 10000
plot = True
save_data = True
directory = 'plots/sun_model'
direction = 'out->in'
ptype = 'ti'

X, Y, Z = 0.912, 0.087, 0.001
M_s, r_s = 1.989E30, 6.957E8

""" Read in rosseland opacity table"""
opTab = genfromtxt("rosseland.dat")
print type(opTab)
print opTab[0,:]
print opTab[:,0]
