import scipy.spatial.distance
import matplotlib.pyplot as plt


def plot_rdm(utv, title, ax=None):
    rdm = scipy.spatial.distance.squareform(utv)
    if ax is None:
        fig, ax = plt.subplots()
    ax.set_title(title)
    return ax.imshow(rdm)