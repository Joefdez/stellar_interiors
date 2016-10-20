# Main body of the solver


# Calls the neccesary libraries for the solution of the equation. Also in charge of reading input data and initializing the problem

from numpy import *
import libs
from solver import *
from data import *




#Read model information

model_name, int_scheme, grid_points, plot, save_data, direc = data.read_stddata(initdata.dat)

#Build numerical grid 



#Read initial conditions and initialize the problem variables

Mr_0, P_0, L_0, T_0 = data.read_initcond(model_name)
Mr, P, L, T = Mr_0, P_0, L_0, T_0

#Initialize atomic populations vector

pops0 = #Call to populations script with initial conditions
pops  = pops0

#Choose integration scheme and setup integration grid

if int_scheme == 'RK4'

    integrator =  integrators.RK4
    grid = array([grid_points])

else:

    return 'Unknow integration scheme'




#Call solver routines

for step in grid:

	#Calculate populations
 	
	#Integrator algorithm

        #Write to file?

	


    print "Numerical solution completed"



#Call plot routines if requiered


    print "Plots completed. Check directory. "
