# Main body of the solver


# Calls the neccesary libraries for the solution of the equation. Also in charge of reading input data and initializing the problem

from numpy import *
import libs.physlib import mu_0, dens
from solver import *
from data import *


""" Read the model and solution routine information from initdata.dat"""
model_name, int_scheme, grid_points, plot, save_data, directory = data.read_stddata(initdata.dat)


""" Read initial conditions and setup global variables"""
R_0, Mr_0, P_0, L_0, T_0, rho_0 = data.read_initcond("initcond.dat")   #Read from text file
R, Mr, P, L, T, rho = R0, Mr_0, P_0, L_0, T_0, rho_0                       #Initialize calculation variables


""" Defined arrays for solution: variables and RHS """
yy = array([Mr, P, L, T])                      #Unknowns array
funcs = array([dMr_r, dP_r, dL_r, dT_r])       # RHS functions array



""" Set-up solution grid and solve the system """

hh, sgrid, solution = integrationSetup(int_scheme, grid_points, r_s)

solution = solve(grid_points, sgrid, yy, hh)

print "Numerical solution completed"



#Call plot routines if requiered
print "Plots completed. Check directory. "
