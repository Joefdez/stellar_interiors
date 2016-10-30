#!/usr/bin/python
from libs.eqs import *


def calc_pops(r, Mr, P, L, T, rho, X, Y, type="ti", ne0=0):

    if type == "ti":
        Ne = nn(T,P)/2.
        pops = pop_TI(T, rho, X, Y, Ne)
    elif type == "iterative":
        pops = pop_iter(T, rho, X, Y, ne0)

    return pops

def calc_rhs(r, Mr, P, L, T, X, Y, mu):
    rho = dens(T, P, mu)
    return array([dMr_r(r, rho), dP_r(r, Mr, rho), dL_r(r, T, rho), dT_r(r, Mr, T, L, rho,mu)])
