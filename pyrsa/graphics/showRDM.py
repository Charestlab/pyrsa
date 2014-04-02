#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt

def showRDM(rdm, save=False):
    plt.matshow(rdm.square)
    plt.title(rdm.name)
    if save:
        plt.savefig(rdm.name.replace(' ','_')+'.png')
        plt.close()
    else:
        show()
