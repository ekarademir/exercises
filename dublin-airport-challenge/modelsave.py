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
from sklearn.tree import DecisionTreeRegressor
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

    df.ix[df.cat_s_plane_capacity == '001 - 050','cat_s_plane_capacity'] = '1'
    df.ix[df.cat_s_plane_capacity == '051 - 100','cat_s_plane_capacity'] = '2'
    df.ix[df.cat_s_plane_capacity == '101 - 150','cat_s_plane_capacity'] = '3'
    df.ix[df.cat_s_plane_capacity == '151 - 200','cat_s_plane_capacity'] = '4'
    df.ix[df.cat_s_plane_capacity == '201 - 300','cat_s_plane_capacity'] = '5'
    df.ix[df.cat_s_plane_capacity == '300+','cat_s_plane_capacity'] = '6'

    savecolheaders = [x for x in df.columns if x[:7] == 'num_pax']

    flightsTarget = df.ix[df.cat_case_type=='Expl',selectColumns]

    dfTest = pd.read_csv('test.csv')

    selectTestColumns = ['id', 'cat_i_flightno', 'cat_s_plane_capacity'] \
                        +['cat_destination_group_id'] \
                        +['cat_longhaul_ind'] \
                        +[x for x in dfTest.columns if x[:7] == 'num_pax']

    submission = dfTest.ix[dfTest.cat_case_type == 'Target',['id']+[x for x in dfTest.columns if x[:7] == 'num_pax']]
    print(submission.shape)

    dfTest.ix[dfTest.cat_s_plane_capacity == '001 - 050','cat_s_plane_capacity'] = '1'
    dfTest.ix[dfTest.cat_s_plane_capacity == '051 - 100','cat_s_plane_capacity'] = '2'
    dfTest.ix[dfTest.cat_s_plane_capacity == '101 - 150','cat_s_plane_capacity'] = '3'
    dfTest.ix[dfTest.cat_s_plane_capacity == '151 - 200','cat_s_plane_capacity'] = '4'
    dfTest.ix[dfTest.cat_s_plane_capacity == '201 - 300','cat_s_plane_capacity'] = '5'
    dfTest.ix[dfTest.cat_s_plane_capacity == '300+','cat_s_plane_capacity'] = '6'

    flightsTargetTest = dfTest.ix[dfTest.cat_case_type=='Target',selectTestColumns]
    print(flightsTargetTest.shape)

    for i in range(17):


        print(i+1, 'of' ,len([x for x in df.columns if x[:7] == 'num_pax']))

        X = flightsTarget.values[:,2:-17]
        y = flightsTarget.values[:,-(i+1)]

        XPredict = flightsTargetTest.values[:,2:-17]

        hiddenlayers = (200,)
        # mlpr = MLPRegressor(hidden_layer_sizes=hiddenlayers,\
        #                     activation="logistic", \
        #                     learning_rate="adaptive")

        mlpr = DecisionTreeRegressor(max_depth=10)
        mlpr.fit(X,y)

        yPredict = mlpr.predict(XPredict)

        for j in range(len(yPredict)):
            if yPredict[j] < 0.0:
                yPredict[j] == 0.0

            yPredict[j] = np.round(yPredict[j])

        print(np.shape(XPredict))
        print(np.shape(yPredict))
        print(submission.shape)
        submission.ix[:,savecolheaders[i]] = yPredict

    submission.to_csv('model_submission.csv', header = False, index = False)

    # ddd = pd.DataFrame.to_csv(path_or_buf=None, header=True, )
