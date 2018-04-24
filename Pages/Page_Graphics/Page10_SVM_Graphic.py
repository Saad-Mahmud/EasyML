from Pages.Page_Main import EasyML_Page10
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import copy
from time import time
import plotly.graph_objs as go
import numpy as np


def algo(c,ga,de,ke,da):
    print('{} {} {} {} {} '.format(c,ga,de,ke,da))
    maindata=copy.deepcopy(EasyML_Page10.util.maindata)
    X_train, X_test, y_train, y_test = train_test_split(maindata.X, maindata.Y, stratify=maindata.Y,random_state=42)

    if(da=='reg'):
        min_train = X_train.min(axis=0)
        range_train = 0.1+(X_train - min_train).max(axis=0)
        X_train = (X_train - min_train) / range_train
        X_test= (X_test - min_train) / range_train

    dt = SVC(random_state=42,C=c,gamma=ga,degree=de,kernel=ke)
    t0=time()
    dt.fit(X_train, y_train)
    Ac=dt.score(X_test, y_test)
    Tm=time()-t0
    EasyML_Page10.util.Xs.append(c)
    EasyML_Page10.util.Ys.append(Ac * 100)
    EasyML_Page10.util.Texts.append(
        "Time = {}, C = {} , Gamma = {}, Kernel = {}, Degree = {}, Data = {}".format(Tm,c,ga,ke,de,da))
    print('done')

def graphic():
    print('here')
    return {
        'data': [
            go.Scatter(
                x=np.asarray(EasyML_Page10.util.Xs),
                y=np.asarray(EasyML_Page10.util.Ys),
                text=np.asarray(EasyML_Page10.util.Texts),
                mode='markers+lines',
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'color': 'blue',
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )],
        'layout': go.Layout(
            xaxis={
                'title': 'Layer Size',
                'type': 'linear'
            },
            yaxis={
                'title': 'Accuracy(%)',
                'type': 'linear'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

def dum():
    return {
        'data': [
            go.Scatter(
                x=np.asarray([]),
                y=np.asarray([]),
                text=np.asarray([]),
                mode='markers',
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'color': 'blue',
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )],
        'layout': go.Layout(
            xaxis={
                'title': 'Layer Size',
                'type': 'linear'
            },
            yaxis={
                'title': 'Accuracy(%)',
                'type': 'linear'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }