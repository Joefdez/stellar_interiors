from numpy import array, genfromtxt

"""This module defines a few functions for reading the different information text files
   relevant to the model. Defined this way for convenience.
"""


def read_stddata(tfile):     #Standard data for all models and uses

    data=genfromtxt(tfile)

    return data[0], data[1], data[2], data[3], \
            data[4], data[5], data[6]


def read_model_spefic(mod_name):   #Read model speficif information

    if name == "solar_model":

        data=genfromtxt(mod_name,dtype='str')

    else:
        raise ValueError('Model not specified. Add it :)')

    return data

def read_kappar(tfile):            # Read in opacity table

    data=genfromtxt(tfile)

    return data

def read_initcond(tfile):          # Read initial conditions into memory

    data=genfromtxt(tfile)

    return data[0], data[1], data[2], data[3], data[4], data[5]
