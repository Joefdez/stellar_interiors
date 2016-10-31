#!/usr/bin/python
# Main body of the solver


#Calls the necessary libraries for the solution of the equation.
#Also in charge of reading input data and initializing the problem

from numpy import *
from solver import *
from libs.setup import *
from libs.initcond import *


hh, sgrid, solution = integrationSetup()

solved = solve(sgrid, hh, solution)

print "Numerical solution completed"



#Call plot routines if requiered
print "Plots completed. Check directory. "
