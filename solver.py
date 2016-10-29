#!/usr/bin/python
# Functions for solving the equations of stellar structure

from numpy import array, append
from rhs import *
from integrators import *

def integrationSetup(int_scheme, grid_points, r_s):

    if integrator == "RK4":

        hh = r_s/grid_points                           #Integration step
        sgrid = grid(h)                                #Numerical grid
        solution = array([grpid_points,4])             #Array container for solution

    else:
        raise ValueError("Integration scheme not found.")

    return hh, sgrid, solution


def solve(grid_points, sgrid, hh, type="ti"):
    """ Global variables """
    global yy
    global rho
    global solution
    global pops



    if integrator == "RK4":

        for jj in range(grid_points):

            pops = calc_pops(r, Mr, P, L, T, rho, X, Y, ne=0)
            mu_Now = mu(T, pops, X, Y, Z)
            next_step = RK4()
            rho = dens(next_step[3] ,next_step[1] ,muNow)
            solution[jj] = append(next_step, array([rho]))
            yy = next_step

        return array[sgrid.transpose(), solution]

    else:
            raise ValueError('Integration scheme not found\
                                    or integration mesh not set up correctly')
