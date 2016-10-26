from numpy import array, genfromtxt

#Read data and give to variables


def read_stddata(tfile):     #Standard data for all models and uses

    data=genfromtxt(tfile)

    return data[0], data[1], data[2], data[3], \
            data[4], data[5], data[6]


def read_model_spefic(mod_name):

    if name == "solar_model":

        data=genfromtxt(mod_name,dtype='str')

    else:
        raise ValueError('Model not specified. Add it :)')

    return data
