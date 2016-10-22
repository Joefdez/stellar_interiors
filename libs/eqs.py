from libs.physlib import


"""

Define derivatives of the quantities (RHS of the ODEs to be solved)
All defined to be explicitly dependent on r and the variable of interest.
Dependecies on the other system variables are introduced through the corresponding variables
without explicit declaration of the dependence.

"""

def dMr_r(r,Mr):
   """ RHS of DE for enclosed mass at a given radius """
    return  4. * pi * (mu(T) * P)/(R * T) * r**2


def dP_r(r,P):
    """ RHS of DE for pressure """
    return  (-1) * (G * mu(T))/(R) * (Mr * P)/(T**2 * r**2)


def dL_r(r,L):
    """ RHS of DE for luminosity  """
    T9 = T/(10E9)

    return  4. * pi * (chi**2 * mu(T) / R) * T9**(-5./3.)/(10E9) *  exp(-3.37* (T9)**(1./3.))

#Temperature gradient : needs to decide whether convective or radiative transport apply.

def rad_grad(r,T):
    """ RHS of DE for teperature if radiative transport dominates"""
    return  (3 * kB * L)/(64. * pi * sig) * 1./(r**2 * T**3)

def conv_grad(r,T):
    """ RHS of DE for temperature if the system is unstable against convective transport """
    return  (-1.) * mu(T)* G/R * (adgam-1.)/adgam * Mr/(r**2)



def dT_r(r,T):
    """ Decide which transport mechanism dominates and apply the corresponding RHS """
    radGrad  = rad_grad(r,T)
    convGrad = conv_grad(r,T)

    grad = is_radiative(radGrad, convGrad)

    return grad
