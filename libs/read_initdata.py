from numpy import array, genfromtxt

"""This module defines a few functions for reading the different information text files
   relevant to the model. Defined this way for convenience.
"""


def read_stddata(tfile):     #Standard data for all models and uses

    data=[]
    with open(tfile) as f:
        for line in f:
            li=line.strip()
            if not li.startswith("#"):
                data.append(li)
    return data[0], data[1], data[2], data[3], \
            data[4], data[5], data[6], data[7]


def read_model_spefic(model_name):   #Read model speficif information

    if model_name == 'sunmodel.dat':
        #data=genfromtxt("sunmodel.dat",dtype='str')
        data=[]
        with open(model_name) as f:
            for line in f:
                li=line.strip()
                if not li.startswith("#"):
                    data.append(li)

    else:
        raise ValueError('Model not specified. Add it :)')

    return data[0], data[1], data[2], data[3], data[4]


def read_initcond(tfile):          # Read initial conditions into memory

    data=genfromtxt(tfile)

    return data[0], data[1], data[2], data[3], data[4], data[5]
