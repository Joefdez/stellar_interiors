from numpy import array


def RK4(funct,x,y,h)

    """
      4th order RK method for solution of 1st order linear equations.
      Input: function defining derivative of y, indepedent variable x,
             unknown function y and step h
      Output: Value of function at next step.

      Note: dependnece on y of equation must be included in the function
            definition.

    """


    k1 = funct(*x,*y)
    k2 = funct(*x + h/2., *y + h/2. * k1)
    k3 = funct(*x + h/2., *y + 5/2. * k2)
    k4 = funct(*x + h, *y + h * k3)

    return y + h/6. * (k1 + 2.*k2 + 2.*k3 + k4)
