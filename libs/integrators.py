#!/usr/bin/python
from numpy import array, empty


def RK4():

    """
      4th order RK method for solution of 1st order linear equations.
      Input: function defining derivative of y, indepedent variable x,
             unknown function y and step h
      Output: Value of function at next step.

      System of ODEs --> y is vector valued, as are the ki and the returned value.

      Note: dependnece on y of equation must be included in the function
            definition.

    """
    num = len(y)-1
    k1 = calc_rhs(r, Mr, P, L, T, rho, X, Y, mu)
    k2 = calc_rhs(r + hh/2., Mr + hh/2.*k1[0], P + hh/2.*k1[1], L + hh/2.*k1[2], T + hh/2.*k1[3], X, Y, mu)
    k3 = calc_rhs(r + hh/2., Mr + hh/2.*k2[0], P + hh/2.*k2[1], L + hh/2.*k2[2], T + hh/2.*k2[3], X, Y, mu)
    k4 = calc_rhs(r + hh, Mr + hh*k3[0], P + hh*k3[1], L + hh*k3[2], T + hh*k3[3], X, Y, mu)

    return y + h/6. * (k1 + 2.*k2 + 2.*k3 + k4)
