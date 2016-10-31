#!/usr/bin/python
from numpy import empty
from rhs import calc_rhs
from libs.initcond import *
from libs.setup import *

def RK4(r, mu, k_r, hh, Mr, P, L, T):

    """
      4th order RK method for solution of 1st order linear equations.
      Input: function defining derivative of y, indepedent variable x,
             unknown function y and step h
      Output: Value of function at next step.

      System of ODEs --> y is vector valued, as are the ki and the returned value.

      Note: dependnece on y of equation must be included in the function
            definition.

    """


    k1 = calc_rhs(r, Mr, P, L, T, X, Y, mu, k_r)
    k2 = calc_rhs(r + hh/2., Mr + hh/2.*k1[0], P + hh/2.*k1[1],
                                   L + hh/2.*k1[2], T + hh/2.*k1[3], X, Y, mu, k_r)
    k3 = calc_rhs(r + hh/2., Mr + hh/2.*k2[0], P + hh/2.*k2[1],
                                   L + hh/2.*k2[2], T + hh/2.*k2[3], X, Y, mu, k_r)
    k4 = calc_rhs(r + hh, Mr + hh*k3[0], P + hh*k3[1],
                                   L + hh*k3[2], T + hh*k3[3], X, Y, mu,  k_r)




    return [Mr + hh/6. * (k1[0] + 2.*k2[0] + 2.*k3[0] + k4[0]),
             P + hh/6. * (k1[1] + 2.*k2[1] + 2.*k3[1] + k4[1]),
             L + hh/6. * (k1[2] + 2.*k2[2] + 2.*k3[2] + k4[2]),
             T + hh/6. * (k1[3] + 2.*k2[3] + 2.*k3[3] + k4[3])]
