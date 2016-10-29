#!/usr/bin/python
# Module for calculating atomic populations for the considered species.
from numpy import array, zeros
from numpy.linalg import solve
from physlib import *




def pop_iter(T, rho, X, Y, Ne0):
    """
        Iterative calculation of the species populations with inital guess of electron number density
        Takes temperature and initial electron number density guess as input.
    """
    Ne = Ne0
    cont_iter = True                                                     # Continue iteration? (control variable)
    niter = 0

    UHI    = partFunc(T, HIe, HIdeg )
    UHII   = 1
    UHeI   = partFunc(T, HeIe, HIdeg)
    UHeII  = partFunc(T, HeIIe, HeIIdeg)
    UHeIII = 1

    pops=array([1,5])                                            #Results vector
    coeff_matrix, indep_terms = zeros([5,5]), zeros([5,1])       #Equation coefficients matrix and independent terms vector
    indep_terms[0, 0], indep_terms[1, 0] = rho * X / m_H, rho * Y/ m_He # Fill independent coefficients

    while cont_iter == True:
        niter += 1


        coeff_matrix[0, 0], coeff_matrix[0, 1] = 1, 1                # Fill in coefficients matrix
        coeff_matrix[1, 2], coeff_matrix[1, 3], coeff_matrix[2, 5] = 1, 1, 1
        coeff_matrix[2, 0], coeff_matrix[2, 1] = 1, (-1) * saha(T, Ne, UHI, UHII, Chi_HI )
        coeff_matrix[3, 2], coeff_matrix[3, 3] = 1, (-1) * saha(T, Ne, UHeI,UHeII, Chi_HeI)
        coeff_matrix[4, 3], coeff_matrix[4, 4] = 1, (-1) * saha(T, Ne, UHeII, UHeIII, Chi_HeII )



        pops = solve(coeff_matrix, indep_terms)

        #etaHI, etaHeI, etaHeII = pops[1] / (pops[0] + pops[1]
        #), pops[3] / (sum(pops[3:])), pops[4] / (sum(pops[3:]))

        Ne1 = pops[1] + pops[3] + 2*pops[4]     #Number of electrons = that of totally ionized plasma

        delt = abs(Ne1-Ne0)/Ne0

        if delt > 0.05:
            Ne0 = (Ne0+Ne1)/2.    #-----> Replace with mean of the values
        else:
            cont_iter = False    # If convergence is acheived, break the look

        #En = Eg(T, etaHI, etaHeI, etaHeII, X, Y)

        #muNow= mu(T, pops[1], pops[3], pops[4])

        return pops#, muNow



def pop_TI(T, rho, X, Y, Ne):

    """
    Calculation of the ionic populations under the assumption that the plasma is totally ionized. Under this assumption,
    the electron density is given as the number density contributing half of the plasma pressure.
    """

    UHI    = partFunc(T, HIe, HIdeg )
    UHII   = 1
    UHeI   = partFunc(T, HeIe, HIdeg)
    UHeII  = partFunc(T, HeIIe, HeIIdeg)
    UHeIII = 1


    pops=array([1,5])                                            #Results vector
    coeff_matrix, indep_terms = zeros([5,5]), zeros([5,1])       #Equation coefficients matrix and independent terms vector

    indep_terms[0, 0], indep_terms[1, 0] = rho * X / m_H, rho * Y/ m_He

    coeff_matrix[0, 0], coeff_matrix[0, 1] = 1, 1                # Fill in coefficients matrix
    coeff_matrix[1, 2], coeff_matrix[1, 3], coeff_matrix[2, 5] = 1, 1, 1
    coeff_matrix[2, 0], coeff_matrix[2, 1] = 1, (-1) * saha(T, Ne, UHI, UHII, Chi_HI )
    coeff_matrix[3, 2], coeff_matrix[3, 3] = 1, (-1) * saha(T, Ne, UHeI,UHeII, Chi_HeI)
    coeff_matrix[4, 3], coeff_matrix[4, 4] = 1, (-1) * saha(T, Ne, UHeII, UHeIII, Chi_HeII )

    pops = solve(coeff_matrix, indep_terms)

    return pops

#   etaHI, etaHeI, etaHeII = pops[1] / (pops[0] + pops[1]
#   ), pops[3] / (sum(pops[3:])), pops[4] / (sum(pops[3:]))
