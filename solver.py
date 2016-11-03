#!/usr/bin/python
# Functions for solving the equations of stellar structure

from numpy import zeros, append, linspace
from libs.rhs import calc_pops
from libs.integrators import *
from libs.setup import *
from libs.physlib import *




def integrationSetup():#int_scheme, grid_points, r_s):


    if int_scheme == "RK4":
        if direction == "out->in":
            hh = (-1.)*r_s/grid_points
            sgrid = linspace(r_s, 0, num=grid_points)
            print hh
        elif direction == "in->out":
            hh = r_s/grid_points
            sgrid = linspace(0, r_s, num=grid_points)
            print rs, hh, rs/hh
        solution = zeros([grid_points,5])             #Array container for solution

    else:
        raise ValueError("Integration scheme not found.")

    return hh, sgrid, solution


def solve(grid, hh, solution, Mr, P, L, T, rho):
    """ Global variables """

    #global rho, Mr, P, L, T
    #global pops

    #yy =[Mr, P, L, T]

    if int_scheme == "RK4":
        for jj in range(0,int(grid_points)-1):
            print jj
            r = grid[jj]
            pops = calc_pops(r, rho, Mr, P, L, T, X, Y, ptype='iterative')
            print pops
            mu_Now = mu(T, pops, X, Y, Z)
            k_r = rossOpacity(T, rho)
            Mr, P, L, T = RK4(r, rho, mu_Now, k_r, hh, Mr, P, L, T)
            rho = dens(T , P ,mu_Now)
            print 'After->', 'r\%=',r/r_s, 'mu=',mu_Now, 'rho=',rho,'m=', Mr/Mr_0,'P=', P, 'l=', L/L_0, 'T=',T
            raw_input("")
            solution[jj, :] = Mr, P, L, T, rho
        return array[sgrid.transpose(), solution]

    else:
            raise ValueError('Integration scheme not found\
                                    or integration mesh not set up correctly')
