"""
 given triples of RGB values, returns the overall brightness vector. This
 is performed on each row of the input (RGBrows) independently.
__________________________________________________________________________
 Copyright (C) 2010 Medical Research Council
 Ported in Python by Jasper van den Bosch and Ian Charest
"""
import numpy as np

def brightness(RGBrows=None):

    if RGBrows is None:
        RGBrows = np.array([[1, 0, 0], [0, 0, 1]])

    
    RGBweights=np.array([.241, .691, .068]).T

    b=np.sqrt(RGBrows*RGBweights)

    return b
