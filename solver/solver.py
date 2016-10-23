# Functions for solving the equations of stellar structure

from numpy import array


def integrationSetup(int_scheme, grid_points, r_s):

        if integrator=="RK4":

            hh = r_s/grid_points                           #Integration step
            sgrid = grid(h)                                #Numerical grid

            solution = array([grpid_points,4])






        else :
            raise ValueError("Integration scheme not found.")

        return hh, sgrid, solution


def solve(grid_points, sgrid, yy, hh):

        global yy
        global solution
        if integreator == "RK4":

            for jj in range(grid_points):

                next_step = integrators.RK4(funcs,sgrid[jj],yy,hh)
                solution[jj] = next_step
                yy = next_step

                return array[sgrid.transpose(), solution]

        else
                raise ValueError('Integration scheme not found
                                        or integration mesh not set up correctly')
