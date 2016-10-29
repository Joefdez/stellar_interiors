#!/usr/bin/python
# Functions for solving the equations of stellar structure

from numpy import array


def integrationSetup(int_scheme, grid_points, r_s):

    if integrator=="RK4":

        hh = r_s/grid_points                           #Integration step
        sgrid = grid(h)                                #Numerical grid
        solution = array([grpid_points,4])             #Array container for solution

    else:
        raise ValueError("Integration scheme not found.")

    return hh, sgrid, solution


def solve(grid_points, sgrid, hh):

    global yy                    """ Global variables """
    global rho
    global solution
    global pops

    if integreator == "RK4":

        for jj in range(grid_points):

            pops, muNow  = populations(T,rho, Ne0)            #Use electron density from previous step????

            next_step = integrators.RK4(funcs,sgrid[jj],yy,hh)
            rho =  dens(yy[1],yy[3],muNow)
            solution[jj,:4], solution[jj,4] = next_step, rho
            yy = next_step

        return array[sgrid.transpose(), solution]

        else:
            raise ValueError('Integration scheme not found\
                                    or integration mesh not set up correctly')
