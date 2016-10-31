#!/usr/bin/python
from libs.eqs import *
from libs.physlib import *
from libs.populations import *

def calc_pops(r, Mr, P, L, T, rho, X, Y, ptype="ti", ne0=0):

    if ptype == "ti":
        Ne = nn(T,P)/2.
        pops = pop_TI(T, rho, X, Y, Ne)
    elif ptype == "iterative":
        pops = pop_iter(T, rho, X, Y, ne0)

    return pops

def calc_rhs(r, Mr, P, L, T, X, Y, mu, k_r):
    rho = dens(T, P, mu)
    return array([dMr_r(r, rho), dP_r(r, Mr, rho), dL_r(r, T, rho, X), dT_r(r, Mr, T, L, rho,mu, k_r)])
