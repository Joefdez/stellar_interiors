#!/usr/bin/python
# Functions for solving the equations of stellar structure

from numpy import zeros, append, linspace
from libs.rhs import calc_pops
from libs.integrators import *
from libs.setup import *
from libs.initcond import *
from libs.physlib import *




def integrationSetup():#int_scheme, grid_points, r_s):

    hh = r_s/grid_points
    if int_scheme == "RK4":
        if direction == "out->in":
            sgrid = linspace(r_s, 0, num=grid_points)
        elif direction == "in->out":
            sgrid = linspace(0, r_s, num=grid_points)
        solution = zeros([grid_points,5])             #Array container for solution

    else:
        raise ValueError("Integration scheme not found.")

    return hh, sgrid, solution


def solve(grid, hh, solution):
    """ Global variables """

    global rho, Mr, P, L, T
    global pops

    yy =[Mr, P, L, T]

    if int_scheme == "RK4":
        for jj in range(1,int(grid_points)):
            r = grid[jj]
            pops = calc_pops(r, Mr, P, L, T, rho, X, Y)
            mu_Now = mu(T, pops, X, Y, Z)
            k_r = rossOpacity(T, rho)
            next_step = RK4(r, mu_Now, k_r, hh, Mr, P, L, T)
            rho = dens(next_step[3] ,next_step[1] ,mu_Now)
            solution[jj, :] = append(next_step, array([rho]))
            Mr, P, L, T = next_step[0], next_step[1]\
                          , next_step[2], next_step[3]


        return array[sgrid.transpose(), solution]

    else:
            raise ValueError('Integration scheme not found\
                                    or integration mesh not set up correctly')
