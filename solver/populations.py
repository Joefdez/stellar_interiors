# Module for calculating atomic populations for the considered species.

import libs


if spec_con===" ":

    def populations(T):

        pops=array([1,5])                                            #Results vector
        coeff_matrix, indep_terms = zeros([5,5]), zeros([5,1])       #Equation coefficients matrix and independent terms vector

        # Fill in coefficients matrix


        coeff_matrix[0,0], coeff_matrix[0,1] = 1, 1                                                #H
        coeff_matrix[1,2], coeff_matrix[1,3], coeff_matrix[2,5] = 1, 1, 1                          #He
        coeff_matrix[2,0], coeff_matrix[2,1] = 1, (-1) * saha( )
        coeff_matrix[3,2], coeff_matrix[3,3] = 1, (-1) * saha( )
        coeff_matrix[4,3], coeff_matrix[4,4] = 1, (-1) * saha( )

        #Fill in the independent term column vector

        indep_terms[0,0], indep_terms[1,0] = X, Y

        return pops



else

    print "Species consideration parameter not recognized."
