# Main body of the solver


# Calls the neccesary libraries for the solution of the equation. Also in charge of reading input data and initializing the problem

from numpy import *
import libs
from solver import *
from data import *



model_name, int_scheme, grid_points, plot, save_data, direc = data.read_stddata(initdata.dat)

#Choose integration scheme and setup integration grid

if int_scheme == 'RK4'

    integrator =  integrators.RK4
    grid = array([grid_points])

else:

    return 'Unknow integration scheme'






#Initialization data


#Call solver routines


    print "Numerical solution completed"

#Save data in file if requiered

#Call plot routines if requiered


    print "Plots completed. Check directory. "
