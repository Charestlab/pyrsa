#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
this function provides a convenient colormap for visualizing
dissimilarity matrices. it goes from blue to yellow and has grey for
intermediate values.

authors: Ian Charest and Jasper van den Bosch
"""

import numpy as np
from skimage.color import rgb2hsv, hsv2rgb
import matplotlib.pyplot as plt
from pyrsa.graphics.colorScale import colorScale


def RDMcolormap(nCols=256):

    # blue-cyan-gray-red-yellow with increasing V (BCGRYincV)
    anchorCols = np.array([
        [0, 0, 1],
        [0, 1, 1],
        [.5, .5, .5],
        [1, 0, 0],
        [1, 1, 0],
    ])

    # skimage rgb2hsv is intended for 3d images (RGB)
    # here we add a new axis to our 2d anchorCols to satisfy skimage, and then squeeze
    anchorCols_hsv = rgb2hsv(anchorCols[np.newaxis, :]).squeeze()

    incVweight = 1
    anchorCols_hsv[:, 2] = (1-incVweight)*anchorCols_hsv[:, 2] + \
        incVweight*np.linspace(0.5, 1, anchorCols.shape[0]).T

    # anchorCols = brightness(anchorCols)
    anchorCols = hsv2rgb(anchorCols_hsv[np.newaxis, :]).squeeze()

    cols = colorScale(nCols, anchorCols)

    return cols
