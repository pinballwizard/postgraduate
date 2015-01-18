__author__ = 'pinballwizard'

import scipy
from scipy import array, exp, arange, linspace, zeros, sort, cos, vstack, hstack, sqrt
from scipy.constants import m_e, pi, hbar
from scipy.sparse.linalg import eigs
from scipy.integrate import ode, odeint
from matplotlib.pyplot import *
import matplotlib.animation as animation
from utils import time_counter


A = 1
w = 1
r = 1
x = linspace(-10, 10, 1000)
k_vector = 1
dk = 10
V = 100
mu = 0

wave_pack = lambda x, k, dt: (A/dk)*exp(-1j*(w*k*(x-dt)-r))
gaussian = lambda x: -V*exp(-((x-mu)**2))

@time_counter
def wave_pack_gen():
    for time in linspace(-10, 10, 100):
        fs = []
        for k_iter in linspace(k_vector-dk/2, k_vector+dk/2, 100):
            fs.append(wave_pack(x, k_iter, time))
        fs = array(sum(fs))
        yield fs/(sqrt(sum(abs(fs)**2)))



@time_counter
def anim():
    fig = figure()
    gen = wave_pack_gen()
    ims = []
    for item in gen:
        ims.append(plot(x, item, 'b'))
    ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=0, blit=True)
    grid()
    show()