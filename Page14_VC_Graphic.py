import EasyML_Page14
from DataProcessor import dtf
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import copy
from time import time
import plotly.graph_objs as go
import numpy as np
import pandas as pd

def algo(dp,ms,mx):
    print('{} {} {}'.format(dp,ms,mx))
    maindata=copy.deepcopy(EasyML_Page14.util.maindata)
    X_train, X_test, y_train, y_test = train_test_split(maindata.X, maindata.Y, stratify=maindata.Y,random_state=42)
    dt = DecisionTreeClassifier(max_depth=dp,min_samples_split=ms,max_features=mx,random_state=0)
    t0=time()
    dt.fit(X_train, y_train)
    Ac=dt.score(X_test, y_test)
    Tm=time()-t0
    EasyML_Page14.util.Xs.append(dp)
    EasyML_Page14.util.Ys.append(Ac*100)
    EasyML_Page14.util.Texts.append("Time = {}, min_sample_split = {}, max_features = {}".format(Tm,ms,mx))
    print('done')

def graphic():
    print('here')
    return {
        'data': [
            go.Scatter(
                x=np.asarray(EasyML_Page14.util.Xs),
                y=np.asarray(EasyML_Page14.util.Ys),
                text=np.asarray(EasyML_Page14.util.Texts),
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
                'title': 'Depth',
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
                'title': 'Depth',
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