from numpy import array, genfromtxt

model_name = 'solar model'
int_scheme = 'RK4'
grid_points = 1000
plot = True
save_data = True
directory = 'plots/sun_model'
direction = 'out->in'
ptype = 'iterative'

X, Y, Z = 0.912, 0.087, 0.001
M_s, r_s = 1.989E33, 6.957E10

""" Read in rosseland opacity table"""
opTab = genfromtxt("rosseland.dat")
