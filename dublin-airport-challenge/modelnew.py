import numpy as np
import pandas as pd
from sklearn import cross_validation
from sklearn.tree import DecisionTreeRegressor

def columnprediction(date, profile, Xpred):
    dftrain = pd.read_csv("train.csv")
    dftest = pd.read_csv("test.csv")

    # print(dftrain.shape)

    dftrain = dftrain.append(dftest.ix[dftest.cat_case_type=='Expl',:])
    # print(dftrain.shape)

    dftrain.dt_flight_date = pd.to_datetime(dftrain.dt_flight_date)

    pool = dftrain.loc[dftrain.dt_flight_date < '2015-01-01']

    pool.sort_values(['dt_flight_date'], ascending=[True])

    pool.drop('id', inplace=True, axis=1)
    pool.drop('dt_prediction_date', inplace=True, axis=1)
    pool.drop('dt_target_date', inplace=True, axis=1)
    pool.drop('s_model_type', inplace=True, axis=1)
    pool.drop('cat_case_type', inplace=True, axis=1)
    pool.drop('dt_flight_date', inplace=True, axis=1)
    # pool.drop('cat_i_flightno', inplace=True, axis=1)

    # print(pool.columns)

    # flightsExploratory = df.ix[df.cat_case_type=='Expl',:]

    pool.ix[pool.cat_s_plane_capacity == '001 - 050','cat_s_plane_capacity'] = '1'
    pool.ix[pool.cat_s_plane_capacity == '051 - 100','cat_s_plane_capacity'] = '2'
    pool.ix[pool.cat_s_plane_capacity == '101 - 150','cat_s_plane_capacity'] = '3'
    pool.ix[pool.cat_s_plane_capacity == '151 - 200','cat_s_plane_capacity'] = '4'
    pool.ix[pool.cat_s_plane_capacity == '201 - 300','cat_s_plane_capacity'] = '5'
    pool.ix[pool.cat_s_plane_capacity == '300+','cat_s_plane_capacity'] = '6'

    pool.ix[pool.cat_flight_class_type_id == 549,'cat_flight_class_type_id'] = 0
    pool.ix[pool.cat_flight_class_type_id == 553,'cat_flight_class_type_id'] = 1
    pool.ix[pool.cat_flight_class_type_id == 556,'cat_flight_class_type_id'] = 2

    numrows = pool.shape[0]



    trainset = pool.head(int(np.round(numrows*0.8)))
    testset = pool.tail(int(np.round(numrows*0.2)))

    clf = DecisionTreeRegressor(max_depth=10)

    # for profile in range(17):
    X = trainset.values[:,0:-17]
    y = trainset.values[:,-(profile+1)]
    # X_ = testset.values[:,0:-17]
    # y_ = testset.values[:,-(profile+1)]

    clf.fit(X,y)

    ypred = clf.predict(Xpred)
    for j in range(len(ypred)):
        if ypred[j] < 0.0:
            ypred[j] == 0.0

        ypred[j] = np.round(ypred[j])

    return ypred



dftest = pd.read_csv("test.csv")

dftest = dftest.ix[dftest.cat_case_type=='Target',:]

dftest.dt_prediction_date = pd.to_datetime(dftest.dt_prediction_date)

dftest.sort_values(['dt_flight_date'], ascending=[True])

dateranges = ['2015-01-01',
'2015-02-01',
'2015-03-01',
'2015-04-01',
'2015-05-01',
'2015-06-01',
'2015-07-01',
'2015-08-01',
'2015-09-01',
'2015-10-01',
'2015-11-01',
'2015-12-01',
'2016-01-01',
'2016-02-01',
'2016-03-01',
'2016-04-01',
'2016-05-01',
'2016-06-01',
'2016-07-01',
'2016-08-01',
'2016-09-01',]

savecolheaders = [x for x in dftest.columns if x[:7] == 'num_pax']

for i in range(len(dateranges)-1):
    mask = (dftest.dt_prediction_date >= dateranges[i]) & (dftest.dt_prediction_date < dateranges[i+1])
    targetflights = dftest.loc[mask]

    # targetflights.drop('id', inplace=True, axis=1)
    targetflights.drop('dt_prediction_date', inplace=True, axis=1)
    targetflights.drop('dt_target_date', inplace=True, axis=1)
    targetflights.drop('s_model_type', inplace=True, axis=1)
    targetflights.drop('cat_case_type', inplace=True, axis=1)
    targetflights.drop('dt_flight_date', inplace=True, axis=1)
    # targetflights.drop('cat_i_flightno', inplace=True, axis=1)

    # print(targetflights.columns)

    # flightsExploratory = df.ix[df.cat_case_type=='Expl',:]

    targetflights.ix[targetflights.cat_s_plane_capacity == '001 - 050','cat_s_plane_capacity'] = '1'
    targetflights.ix[targetflights.cat_s_plane_capacity == '051 - 100','cat_s_plane_capacity'] = '2'
    targetflights.ix[targetflights.cat_s_plane_capacity == '101 - 150','cat_s_plane_capacity'] = '3'
    targetflights.ix[targetflights.cat_s_plane_capacity == '151 - 200','cat_s_plane_capacity'] = '4'
    targetflights.ix[targetflights.cat_s_plane_capacity == '201 - 300','cat_s_plane_capacity'] = '5'
    targetflights.ix[targetflights.cat_s_plane_capacity == '300+','cat_s_plane_capacity'] = '6'

    targetflights.ix[targetflights.cat_flight_class_type_id == 549,'cat_flight_class_type_id'] = 0
    targetflights.ix[targetflights.cat_flight_class_type_id == 553,'cat_flight_class_type_id'] = 1
    targetflights.ix[targetflights.cat_flight_class_type_id == 556,'cat_flight_class_type_id'] = 2

    for prof in range(len(savecolheaders)):
        print(i, prof)
        Xpred = targetflights.values[:,1:-17]
        ypred = columnprediction(dateranges[i], prof, Xpred)
        dftest.ix[mask,savecolheaders[prof]] = ypred

dftest.to_csv('testresults.csv', index = False)
