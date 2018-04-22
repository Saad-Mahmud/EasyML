from Pages import EasyML_Page6
from DataProcessor import dtf
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import copy
from time import time
import plotly.graph_objs as go
import numpy as np
import pandas as pd

def algo(itr,sol,al):
    if(sol=='liblinear' and al=='multinomial'):return
    print('{} {} {}'.format(itr,sol,al))
    maindata=copy.deepcopy(EasyML_Page6.util.maindata)
    X_train, X_test, y_train, y_test = train_test_split(maindata.X, maindata.Y, stratify=maindata.Y,random_state=42)
    lr = LogisticRegression(max_iter=itr,multi_class=al,solver=sol)
    t0=time()
    lr.fit(X_train, y_train)
    Ac=lr.score(X_test, y_test)
    Tm=time()-t0
    EasyML_Page6.util.Xs.append(itr)
    EasyML_Page6.util.Ys.append(Ac*100)
    EasyML_Page6.util.Texts.append("Time = {}, Algo = {}, Solver = {}".format(Tm,al,sol))
    print('done')

def graphic():
    print('here')
    return {
        'data': [
            go.Scatter(
                x=np.asarray(EasyML_Page6.util.Xs),
                y=np.asarray(EasyML_Page6.util.Ys),
                text=np.asarray(EasyML_Page6.util.Texts),
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
                'title': 'Itr',
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
                'title': 'Time(Sc)',
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