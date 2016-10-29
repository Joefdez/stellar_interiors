from physlib import *


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


def dL_r(r, T, rho):
    """ RHS of DE for luminosity  """
    T9 = T/(10E9)

    return  4. * pi * rho**2 * r**2 * X**2 * 2.53E4 * T9**(-2./3.) * exp(-3.37* (T9)**(1./3.))

#Temperature gradient : needs to decide whether convective or radiative transport apply.

def rad_grad(r, T, L, rho):
    """ RHS of DE for teperature if radiative transport dominates"""

    k_r = 34

    return (3 * k_r * L * rho)/(64. * pi * sig) * 1./(r**2 * T**3)

def conv_grad(r, T, Mr):
    """ RHS of DE for temperature if the system is unstable against convective transport """
    g= Mr*G/(r**2)
    return  (-1.) * mu(T)/R * (adgam-1.)/adgam * g



def dT_r(r, Mr, T, L):
    """ Decide which transport mechanism dominates and apply the corresponding RHS """
    radGrad  = rad_grad(r, T, L, kr)
    convGrad = conv_grad(r,T, Mr)

    grad = is_radiative(radGrad, convGrad)

    return grad



def calc_rhs(r, Mr, P, L, T, mu, kr):

    rho = dens(T, P, mu) 
    return rho, dMr_r(r, rho), dP_r(r, Mr, rho), dL_r(r, T, rho), dT_r(r, Mr, T, L)
