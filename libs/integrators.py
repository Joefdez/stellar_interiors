#!/usr/bin/python
from numpy import empty
from libs.rhs import calc_rhs
from libs.initcond import *
from libs.setup import *

def RK4(r, rho, mu, k_r, hh, Mr, P, L, T):

    """
      4th order RK method for solution of 1st order linear equations.
      Input: function defining derivative of y, indepedent variable x,
             unknown function y and step h
      Output: Value of function at next step.

      System of ODEs --> y is vector valued, as are the ki and the returned value.

      Note: dependnece on y of equation must be included in the function
            definition.

    """
    #print 'RK4 ->' , r, mu, k_r, hh, Mr, P, L, T, rho
    print r
    k1 = hh * calc_rhs(r, rho, Mr, P, L, T, X, Y, mu, k_r)
    #print k1[0]
    #print 'hh*k1', hh*k1
    k2 = hh * calc_rhs(r + hh/2., rho, Mr + 1/2.*k1[0], P + 1/2.*k1[1],
                                   L + 1/2.*k1[2], T + 1/2.*k1[3], X, Y, mu, k_r)
    #print 'hh*k2', hh*k2
    #print 'second t coeff', hh/2.*k2[3], T, hh
    k3 = hh * calc_rhs(r + hh/2., rho,  Mr + 1/2.*k2[0], P + 1/2.*k2[1],
                                   L + 1/2.*k2[2], T + 1/2.*k2[3], X, Y, mu, k_r)
    #print 'hh*k3', hh*k3
    k4 = hh * calc_rhs(r + hh, rho, Mr + k3[0], P + k3[1],
                                   L + k3[2], T + k3[3], X, Y, mu,  k_r)
    #print 'hh*k4', hh*k4

    #print hh, k1, k2, k3, k4

    #print 1/6. * (k1[0] + 2.*k2[0] + 2.*k3[0] + k4[0]), 1/6. * (k1[1] + 2.*k2[1] + 2.*k3[1] + k4[1]),\
    # 1/6. * (k1[2] + 2.*k2[2] + 2.*k3[2] + k4[2]), 1/6. * (k1[3] + 2.*k2[3] + 2.*k3[3] + k4[3])

    return Mr + 1/6. * (k1[0] + 2.*k2[0] + 2.*k3[0] + k4[0]), \
             P + 1/6. * (k1[1] + 2.*k2[1] + 2.*k3[1] + k4[1]), \
             L + 1/6. * (k1[2] + 2.*k2[2] + 2.*k3[2] + k4[2]), \
             T + 1/6. * (k1[3] + 2.*k2[3] + 2.*k3[3] + k4[3])
