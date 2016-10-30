#!/usr/bin/python
from numpy import array, exp, log
from bisect import *
from scipy.interpolate import interp2d

#####      Physical constants in cgs units  #####

R     = 8.3144598E7                     # Gas constant (erg K^-1 mol^-1)
N_a   = 6.02214086E23                   # Avogradro's number
sig   = 5.670373E-5                     # Stefan-Boltzmann constant (erg cm^-2 s^-1 K^-4
m_H   = 1.67372E-30                     # Hydrogen mass (g)
m_He  = 6.64647E-30                     # Helium mass (g)
G     = 6.67428E-8                      # Universal gravitational constant (cm^3 g^-1 s^-2=
k_b   = 1.38064852E-16                  # Boltzmann constant (JK^-1
adgam = 5./3.                           # Adiabatic coefficient for monoatomic gas

# Ionization energies

Chi_HI     = 2.18E-11
Chi_HeI    = 3.94E-11
Chi_HeII   = 8.72E-11

# Excitation energies and level degeneracies

HIe       = [0,2.178E-11]
HIdeg     = [2,8]
HeIe      = [0,3.17E-11, 3.30E-11, 3.36E-11, 3.40E-11, 3.64E-11]
HeIdeg    = [1,3,1,9,3,3]
HeIIe     = [0, 6.54E-11, 7.75E-11, 8.17E-11, 8.33E-11, 8.48E-11]
HeIIdeg     = [2, 8, 18, 32, 50 ]

######     Physical equations and transformations     #######

# Saha equation

def saha(T,n_e,U,U_1,Ei):

    """
       Saha equation. Input: temperature, electron density, density of previous ionization state,
       partition functions of state of interest and previous state and energies.
       Output: relative population of ionization state to next ionization state

    """

    phi=2.07E-16*(U/U_1)*T**(-3/2)*exp(Ei/(k_b*T))     #Calculate Saha factor. (E_0-E)

    return n_e*phi                                     #Calculate population of ionization state.


# Ideal gas equation

def dens(T, P, mu):

    """
        Ideal gas equation. Input: temperature, pressure, mean molecular mass. Calculates gas density.
        This form of the equation is of most interest for integrating the equations of stellar structure.
    """
    return (mu*P)/(R*T)

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
    etaHI = pops[1]/(pops[0]+pops[1])
    etaHeI = pops[3]/(pops[2]+pops[3]+pops[4])
    etaHeII = pops[4]/(pops[2]+pops[3]+pops[4])
    ionization_state = mu_0(X, Y, Z)*  ( etaHI * X + (etaHeI + 2*etaHeII) * Y/4. )

    return ionization_state


# Mean molecular mass for gas with non-zero ionization

def mu(T, pops, X, Y, Z):
    """
        Calculates the mean moleculare weight for a partially ionized gas.
    """
    E = Eg(T, pops, X, Y, Z)

    return mu_0(X, Y, Z)/(1+E)


# pp nuclear energy generation rate

def e_pp(T, rho, X):

    T9 = T/(10E9)                  # Temperature in units of 10^9 K

    return 2.53E4 * rho * X**2 *T9**(2./3.)*exp(-3.37 * T9**(-1./3.))

# Convective transport / Radiative transport criteria

def is_radiative(rad_grad, conv_grad):

    """
        Returns true if the system is stable against Convection, that is, if radiative transport
        dominates. Returns false if convective transport dominates.
    """

    response = conv_grad>rad_grad
    if response:
        return rad_grad
    else:
        return conv_grad


def partFunc(T,energ, degen):
    """Calculates canonical partition function of a system, given the energy levels and degeneracies"""

    return sum(degen * exp(-energ/(k_b*T)))

def rossOpacity(T, rho, mu):
    T6 = T/(10E6)
    lD = log(rho/T6)
    lT = log(T)

    lowerT, lowerD = bisect_left(lT, opTab[:, 0]), bisect_left(lD, opTab[0, :])
    upperT, upperD = bisect_right(lT, opTab[:, 0]), bisect_right(lD, opTab[0, :])
    kappa1, kappa2 = opTab[lowerT, lowerD], opTab[upperT,upperD]

    fit = interp2d([lowerT, upperT], [lowerD, upperD], [kappa1, kappa2], kind='linear')
    val = fit(lT, lD)

    return val
