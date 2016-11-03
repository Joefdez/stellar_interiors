#!/usr/bin/python
# Main body of the solver


#Calls the necessary libraries for the solution of the equation.
#Also in charge of reading input data and initializing the problem

from numpy import *
from solver import *
from libs.setup import *
from libs.initcond import *

Mr, P, L, T, rho = Mr_0, P_0, L_0, T_0, rho_0
hh, sgrid, solution = integrationSetup()

print 'Model name:', model_name, "\n" \
      'Integratin scheme:', RK4, "\n" \
      'Grid points, distance step', grid_points, hh, "\n" \
      'Ptype', ptype, "\n" \
      'Mr0=', Mr_0, 'P0=', P_0, 'L_0=', L_0, 'T_0=', T_0, 'rho_0=', rho_0



solved = solve(sgrid, hh, solution, Mr, P, L, T, rho)
print solved[-1,:]

print "Numerical solution completed"



#Call plot routines if requiered
print "Plots completed. Check directory. "
