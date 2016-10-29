from numpy import array, empty


def RK4(funct,x,y,h):

    """
      4th order RK method for solution of 1st order linear equations.
      Input: function defining derivative of y, indepedent variable x,
             unknown function y and step h
      Output: Value of function at next step.

      System of ODEs --> y is vector valued, as are the ki and the returned value.

      Note: dependnece on y of equation must be included in the function
            definition.

    """
    num = len(y)
    k1, k2, k3, k4 = empty(num), empty(num), empty(num), empty(num)

    for ii in range(0,num):
        k1[ii] = funct[ii](y[ii],x)
    for ii in range(0,num):
        k2[ii] = funct[ii](y[ii] + k1[ii] * h/2., x + h/2.)
    for ii in range(0,num):
        k3[ii] = funct[ii](y[ii] + k2[ii] * h/2., x + h/2. )
    for ii in range(0,num):
        k4[ii] = funct[ii](y[ii] + k3[ii] * h, x + h)



    return y + h/6. * (k1 + 2.*k2 + 2.*k3 + k4)
