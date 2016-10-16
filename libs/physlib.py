import libraries

#####      Physical constants in SI units  #####

R=8.3144598                       # Gas constant (J K^-1 mol^-1)
N_a=6.02214086E23                 # Avogradro's number
sig=5.670373E-8                   # Stefan-Boltzmann constant (J m^-2 s^-2 K^-4
m_H=1.67372E-27                   # Hydrogen mass (kg)
G=6.67408E-11                     # Universal gravitational constant (m^3 kg^-1 s^-2=
k_b=1.38064852E-23                # Boltzmann constant (JK^-1

## Ionization energies




#####      Unit conversions     #####


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


def saha_ne(T,U,U_1,Ei):

    """
        Saha equation divided by electron number. Output: relative population of ionization state to previous
        ionization state and electron number.

    """

    phi=2.07E-16*(U/U_1)*T**(-3/2)*exp(Ei/(k_b*T))

    return phi

# Ideal gas equation

def rho(T,P,mu):

    """ 
        Ideal gas equation. Input: temperature, pressure, mean molecular mass. Calculates gas density.
        This form of the equation is of most interest for integrating the equations of stellar structure.
    """
    return (mu*P)/(R*T)



# Mean molecular mass for neutral gas

def mu_0():
     return 1./(X+Y/4.+Z/2.)
   
# Ionization

def Eg(T,n_HII, n_HeII, n_HeIII):
   
    """
       Ionitzation state. Input: Hydogren and helium fractions, metallicity. Calculates the ionization degree of 
       the gas. 
    """
         
   
   ionization_state= mu_0() ( n_HII*X + (n_HeII + n_HeIII) * Y/4. )

   return ionization_state


# Mean molecular mass for gas with non-zero ionization

def mu(T,n_HII, n_HeII, n_HeIII):
    
    """
        Calculates the mean moleculare weight for a partially ionized gas.

    """



    E=Eg(T,n_HII, n_HeII, n_HeIII)
    
    return mu_0()/(1+E)


# pp nuclear energy generation rate

def e_pp(T,rho):
    
    T9 = T/(10E9)                  # Temperature in units of 10^9 K 
    
    return 2.53E4 * rho * X**2 * T9**(2./3.) * exp(-3.37 * T9**(-1./3.) )

# Convective transport / Radiative transport criteria

def is_radiative(rad_grad, conv_grad)

    """
        Returns true if the system is stable against Convection, that is, if radiative transport
        dominates. Returns false if convective transport dominates.         

    """

    return conv_grad>rad_grad
