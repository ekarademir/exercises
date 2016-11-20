import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import preprocessing
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.multioutput import MultiOutputRegressor
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
    selectColumns = ['id', 'cat_i_flightno', 'cat_s_plane_capacity'] \
                        +['cat_destination_group_id'] \
                        +['cat_longhaul_ind'] \
                        +[x for x in df.columns if x[:7] == 'num_pax']
    # flightsExploratory = df.ix[df.cat_case_type=='Expl',:]

    df.ix[df.cat_s_plane_capacity == '001 - 050',:] = '1'
    df.ix[df.cat_s_plane_capacity == '051 - 100',:] = '2'
    df.ix[df.cat_s_plane_capacity == '101 - 150',:] = '3'
    df.ix[df.cat_s_plane_capacity == '151 - 200','cat_s_plane_capacity'] = '4'
    df.ix[df.cat_s_plane_capacity == '201 - 300','cat_s_plane_capacity'] = '5'
    df.ix[df.cat_s_plane_capacity == '300+','cat_s_plane_capacity'] = '6'



    flightsTarget = df.ix[df.cat_case_type=='Expl',selectColumns]
    flightsTargetTest = df.ix[df.cat_case_type=='Target',selectColumns]

    print(len([x for x in df.columns if x[:7] == 'num_pax']))

    X = flightsTarget.values[:,2:-17]
    y = flightsTarget.values[:,-1]


    hiddenlayers = (200,)
    mlpr = MLPRegressor(hidden_layer_sizes=hiddenlayers,\
                        activation="logistic", \
                        learning_rate="adaptive")
    # mlpr = MultiOutputRegressor(estimator=estimator)
    # mlpr = LinearRegression(normalize=False)

    # mlpr = ElasticNet(l1_ratio=0.5, alpha=0.1)

    mlpr.fit(X,y)

    print(np.shape(X))
    print(np.shape(y))

    dfTest = pd.read_csv('test.csv')
    # flightsExploratory = df.ix[df.cat_case_type=='Expl',:]

    dfTest.ix[dfTest.cat_s_plane_capacity == '001 - 050',:] = '1'
    dfTest.ix[dfTest.cat_s_plane_capacity == '051 - 100',:] = '2'
    dfTest.ix[dfTest.cat_s_plane_capacity == '101 - 150',:] = '3'
    dfTest.ix[dfTest.cat_s_plane_capacity == '151 - 200','cat_s_plane_capacity'] = '4'
    dfTest.ix[dfTest.cat_s_plane_capacity == '201 - 300','cat_s_plane_capacity'] = '5'
    dfTest.ix[dfTest.cat_s_plane_capacity == '300+','cat_s_plane_capacity'] = '6'

    submission = dfTest(['id']+[x for x in df.columns if x[:7] == 'num_pax'])

    submission.head()

    flightsTargetTest2 = dfTest.ix[dfTest.cat_case_type=='Expl',selectColumns]



    XTest = flightsTargetTest.values[:,2:-17]
    yTest = flightsTargetTest.values[:,-17]
    XTest2 = flightsTargetTest2.values[:,2:-17]
    yTest2 = flightsTargetTest2.values[:,-17]

    print(flightsTarget.shape)
    print(np.shape(XTest))
    print(np.shape(yTest))
    print(np.shape(XTest2))
    print(np.shape(yTest2))

    yPredict = mlpr.predict(XTest)

    plt.plot(yPredict)
    plt.plot(yTest)
    plt.show()
    confidence = mlpr.score(XTest, yTest)
    confidence2 = mlpr.score(XTest2, yTest2)
    print(confidence)
    print(confidence2)
