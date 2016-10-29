# Main body of the solver


# Calls the neccesary libraries for the solution of the equation. Also in charge of reading input data and initializing the problem

from numpy import *
from solver import *
from libs.read_initdata import *


""" Read the model and solution routine information from initdata.dat"""

model_name, int_scheme, grid_points, plot, save_data, directory = read_stddata("initdata.dat")
X, Y , Z, M_s, r_s = read_model_spefic("sonmodel.dat")

""" Read initial conditions and setup global variables"""
R_0, Mr_0, P_0, L_0, T_0, rho_0 = read_initcond("initcond.dat")   #Read from text file
R, Mr, P, L, T, rho = R_0, Mr_0, P_0, L_0, T_0, rho_0                       #Initialize calculation variables

""" Read in rosseland opacity table"""
opTab = genfromtxt("rosseland.dat")

""" Defined arrays for solution: variables and RHS """
yy = array([rho, Mr, P, L, T])                      #Unknowns array
funcs = array([dMr_r, dP_r, dL_r, dT_r])       # RHS functions array


""" Set-up solution grid and solve the system """

hh, sgrid, solution = integrationSetup(int_scheme, grid_points, r_s)

solution = solve()

print "Numerical solution completed"



#Call plot routines if requiered
print "Plots completed. Check directory. "
