# Functions for solving the equations of stellar structure




def integrationSetup():

        if integrator=="RK4":

            hh = r_s/grid_points                            #Integration step
            sgrid = grid(h)                                #Numerical grid

            solution = array([grpid_points,4])






        else :
            print "Specified integrator not found. Check available integrators or add it yourself :) !"

        return hh, sgrid, solution


def solve(sgrid, yy):

        global yy
        global solution

        for jj in range(grid_points):

            next_step = integrators.RK4(funcs,sgrid[jj],yy,h)
            solution[jj] = next_step
            yy = next_step

        return [sgrid.transpose(), solution]
