import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import preprocessing
from sklearn.neural_network import MLPRegressor
from scipy.special import erf
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
import numpy as np

style.use('ggplot')

def pdf(x):
    return np.exp(-x**2/2)/np.sqrt(2*np.pi)

def cdf(x):
    return (1.0+erf(x/np.sqrt(2.0)))/2.0

def skew_normal(x, amp, e, o, a):
    # e peakposition
    # o peakwidth
    # a bulge
    t = (x-e) / o
    return amp*2 / o * pdf(t) * cdf(a*t)

if __name__ == "__main__":
    df = pd.read_csv('train.csv')
    # selectColumns = ['id', 'cat_case_type', 'cat_i_flightno',
    #                     'cat_s_plane_capacity'] \
    #                     +[x for x in df.columns if x[:7] == 'num_pax']
    selectColumns = [x for x in df.columns if x[:7] == 'num_pax']
    # flightsExploratory = df.ix[df.cat_case_type=='Expl',:]
    flightsTarget = df.ix[df.cat_case_type=='Target',selectColumns]
    i = 3000
    y = flightsTarget[i:i+1].values[0]
    # y[5] = 10
    x = range(len(y))
    # xi = np.linspace(np.min(x), np.max(x), 40)
    # f = interp1d(x,y)
    # yi = f(xi)

    # x = np.linspace(0,16,8)
    # y = skew_normal(x,3,4,5)

    # p, c = curve_fit(skew_normal, x, y, p0=[10, 5, 4, 3])

    x_ = np.linspace(np.min(x), np.max(x), 50)
    # y_ = skew_normal(x_, p[0], p[1], p[2], p[3])
    y_ = skew_normal(x_,100, 5, 4, 3)

    plt.plot(x, y, 'ro')
    plt.plot(x_, y_,'b-')
    plt.show()

    # peakposition = -2.0
    # peakwidth = 2.0
    # bulge = 4.0
    #
    # x = np.linspace(-5,5,1000)
    # y = [skew_normal(k, peakposition, peakwidth, bulge) for k in x]
    # plt.plot(x,y)
    # plt.show()
