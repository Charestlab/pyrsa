from pyrsa.plotting import plot_rdm
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

def update(f, *fargs):
    utvs, ax, title = fargs
    utv = utvs[f, :]
    return plot_rdm(utv, title, ax=ax),

def movie_rdm(utvs, title):
    nframes, _ = utvs.shape
    fig, ax = plt.subplots()
    return FuncAnimation(
        fig,
        update,
        frames=nframes,
        repeat=False,
        fargs=(utvs, ax, title)
    )
