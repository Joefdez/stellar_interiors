# Module for calculating atomic populations for the considered species.
from numpy import array, zeros, linalg.solve
from libs.physlibs import *




def populations(T, Ne0):
        """
        Iterative calculation of the species populations with inital guess of electron number density
        Takes temperature and initial electron number density guess as input.
        """

        cont_iter = True                                                     # Continue iteration? (control variable)
        niter = 0

        UHI    = partFunc(T, HIe, HIdeg )
        UHII   = 1
        UHeI   = partFunc(T, HeIe, HIdeg)
        UHeII  = partFunc(T, HeIIe, HeIIdeg)
        UHeIII = 1


        while cont_iter == True:
            niter += 1
            pops=array([1,5])                                            #Results vector
            coeff_matrix, indep_terms = zeros([5,5]), zeros([5,1])       #Equation coefficients matrix and independent terms vector

                # Fill in coefficients matrix


            coeff_matrix[0,0], coeff_matrix[0,1] = 1, 1
            coeff_matrix[1,2], coeff_matrix[1,3], coeff_matrix[2,5] = 1, 1, 1
            coeff_matrix[2,0], coeff_matrix[2,1] = 1, (-1) * saha(T,UHI,UHII, ChiHI )
            coeff_matrix[3,2], coeff_matrix[3,3] = 1, (-1) * saha(T,UHeI,UHeII, ChiHeI)
            coeff_matrix[4,3], coeff_matrix[4,4] = 1, (-1) * saha(T,UHeII,UHeUIII, ChiHeII )

            #Fill in the independent term column vector

            indep_terms[0,0], indep_terms[1,0] = X, Y    # WRONG, RETHINK THIS!!

            pops = solve(coeff_matrix, indep_terms)

            etaHI, etaHeI, etaHeII = pops[1] / (pops[0] + pops[1]),
                        pops[3] / (sum(pops[3:])), pops[4] / (sum(pops[3:]))

            En = Eg(T, etaHI, etaHeI, etaHeII)

            Ne1 = En * (pops[1] + pops[3] + 2 * pops[4]) #Ionization fraction is number of electrons / number of ions, be definition
                                                         # --> estimate number of electrons from it

            delt = abs(Ne1-Ne0)/Ne0

            if del > 0.05:

                Ne0 = (Ne0+Ne1)/2.    #-----> Replace with mean of the values
            else:
                # If convergence is acheived, break the look
                cont_iter = False

        return pops
