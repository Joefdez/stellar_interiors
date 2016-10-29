#!/usr/bin/python
from libs.populations import *
from libs.physlib import rossOpacity

"""

Define derivatives of the quantities (RHS of the ODEs to be solved)
All defined to be explicitly dependent on r and the variable of interest.
Dependecies on the other system variables are introduced through the corresponding variables
without explicit declaration of the dependence.

"""

def dMr_r(r, rho):
    """ RHS of DE for enclosed mass at a given radius """
    return  4. * pi * rho * r**2


def dP_r(r, Mr, rho):
    """ RHS of DE for pressure """
    return  (-1) * (G * rho * Mr)/r**2


def dL_r(r, T, rho, X):
    """ RHS of DE for luminosity  """
    return  4. * pi * rho * r**2 *  e_pp(T, rho, X)

#Temperature gradient : needs to decide whether convective or radiative transport apply.

def rad_grad(r, T, L, rho):
    """ RHS of DE for teperature if radiative transport dominates"""

    k_r = rossOpacity(T, P, mu)

    return (3 * k_r * L * rho)/(64. * pi * sig) * 1./(r**2 * T**3)

def conv_grad(r, T, Mr, pops, X, Y, Z):
    """ RHS of DE for temperature if the system is unstable against convective transport """
    g= Mr*G/(r**2)
    return  (-1.) * mu(T, pops, X, Y, Z)/R * (adgam-1.)/adgam * g


def dT_r(r, Mr, T, L, rho):
    """ Decide which transport mechanism dominates and apply the corresponding RHS """
    radGrad = rad_grad(r, T, L, rho)
    convGrad = conv_grad(r, T, Mr)

    grad = is_radiative(radGrad, convGrad)

    return grad
