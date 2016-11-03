#!/usr/bin/python
from numpy import array, exp, log10
from libs.initcond import *
from libs.setup import *
from bisect import *
from scipy.interpolate import interp2d

#####      Physical constants in cgs units  #####

R     = 8.3144598E7                     # Gas constant (erg K^-1 mol^-1)
N_a   = 6.02214086E23                   # Avogradro's number
sig   = 5.670373E-5                     # Stefan-Boltzmann constant (erg cm^-2 s^-1 K^-4
m_H   = 1.67372E-24                     # Hydrogen mass (g)
m_He  = 6.64647E-24                     # Helium mass (g)
G     = 6.67428E-8                      # Universal gravitational constant (cm^3 g^-1 s^-2=
k_b   = 1.38064852E-16                  # Boltzmann constant (JK^-1
adgam = 5./3.                           # Adiabatic coefficient for monoatomic gas
m_u   = 1.661E-24                      # Atomic mass constantc
# Ionization energies

Chi_HI     = 2.18E-11
Chi_HeI    = 3.94E-11
Chi_HeII   = 8.72E-11

# Excitation energies and level degeneracies

HIe       = array([0, 2.178E-11])
HIdeg     = array([2, 8])
HeIe      = array([0, 3.17E-11, 3.30E-11, 3.36E-11, 3.40E-11, 3.64E-11])
HeIdeg    = array([1, 3,1,9,3,3])
HeIIe     = array([0, 6.54E-11, 7.75E-11, 8.17E-11, 8.33E-11])
HeIIdeg   = array([2, 8, 18, 32, 50 ])

######     Physical equations and transformations     #######

# Saha equation

def saha(T,n_e,U,U_1,Ei):

    """
       Saha equation. Input: temperature, electron density, density of previous ionization state,
       partition functions of state of interest and previous state and energies.
       Output: relative population of ionization state to next ionization state

    """

    phi=2.07E-16*(U/U_1)*T**(-3./2.)*exp(Ei/(k_b*T))     #Calculate Saha factor. (E_0-E)

    return n_e*phi                                     #Calculate population of ionization state.


# Ideal gas equation

def dens(T, P, mu):

    """
        Ideal gas equation. Input: temperature, pressure, mean molecular mass. Calculates gas density.
        This form of the equation is of most interest for integrating the equations of stellar structure.
    """
    return (m_u*mu*P)/(k_b*T)

def nn(T, P):

    """
       Ideal gas equation in terms of the number density. Input: temperature and pressure
    """

    return P/(k_b * T)


# Mean molecular mass for neutral gas

def mu_0(X, Y, Z):
    return 1./(X+Y/4.+Z/2.)

# Ionization

def Eg(T, pops, X, Y, Z):

    """
       Ionitzation state. Input: Hydogren and helium fractions, metallicity. Calculates the ionization degree of
       the gas.
    """
    if ptype == 'ti':
        etaHI   = 1.
        etaHeI  = pops[1, 0]/(pops[1, 0] + pops[2, 0])
        etaHeII = pops[2, 0]/(pops[1, 0] + pops[2, 0])
    else:
    	etaHI = pops[1,0]/(pops[0,0]+pops[1,0])
    	etaHeI = pops[3,0]/(pops[2,0]+pops[3,0]+pops[4,0])
      	etaHeII = pops[4,0]/(pops[2,0]+pops[3,0]+pops[4,0])



    ionization_state = mu_0(X, Y, Z)*  ( etaHI * X + (etaHeI + 2.*etaHeII) * Y/4. )
    return ionization_state



# Mean molecular mass for gas with non-zero ionization

def mu(T, pops, X, Y, Z):
    """
        Calculates the mean moleculare weight for a partially ionized gas.
    """
    E = Eg(T, pops, X, Y, Z)
    #print 'Eg, T',Eg, T
    return mu_0(X, Y, Z)/(1+E)


# pp nuclear energy generation rate

def e_pp(T, rho, X):

    T9 = T/(1E9)                  # Temperature in units of 10^9 K
    #print 'T9', T9
    return 2.53E4 * rho * X**2 *T9**(-2./3.)*exp(-3.37 * T9**(-1./3.))

# Convective transport / Radiative transport criteria

def is_radiative(rad_grad, conv_grad):

    """
        Returns true if the system is stable against Convection, that is, if radiative transport
        dominates. Returns false if convective transport dominates.
    """

    response = conv_grad>rad_grad
    if response:
    #   print 'radiative'
        return rad_grad
    else:
    #   print 'covnective'
        return conv_grad


def partFunc(T,energ, degen):
    """Calculates canonical partition function of a system, given the energy levels and degeneracies"""
    #print sum(degen * exp(-energ/(k_b*T)))
    return sum(degen * exp(-energ/(k_b*T)))

def rossOpacity(T, rho):
    T6 = T/(1E6)
    #print T, T6, rho
    #print rho/T6**3
    lD = log10(rho/T6**3)
    lT = log10(T)
    #print lD, lT

    for ii in range(1,len(opTab[1,:])):
        if opTab[0,ii]>lD:
            d2 = opTab[0,ii]
            d1 = opTab[0,ii-1]
            break
    for ii in range(1,len(opTab[:,1])):
        if opTab[ii,0]>lT:
            t2 = opTab[ii,0]
            t1 = opTab[ii-1,0]
            break
    #print d1, d2, t1, t2

    k11, k12, k21, k22 = opTab[t1, d1], opTab[t1, d2],\
                         opTab[t2, d1], opTab[t2, d2]
    delT, delD = t2-t1, d2-d1

    val = (d2-lD)/delD * ( (t2-lT)/delT * k11 + (lT-t1)/delT * k21) \
        + (lD-d1)/delD * ( (t2-lT)/delT * k12 + (lT-t1)/delT * k22)

    #delK = kappa2-kappa1
    #val = kappa1 + delK/(upperT-lowerT) * (lT-lowerT) + delK/(upperD-lowerD) * (lD-lowerD)
    #print k11,k12,k21,k22, val
    return val
