import EasyML_Page9
from DataProcessor import dtf
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import copy
from time import time
import plotly.graph_objs as go
import numpy as np
import pandas as pd

def algo(hls,itr,alp,lri,lrm,ac,sol):
    print('{} {} {} {} {} {} {}'.format(hls,itr,alp,lri,lrm,ac,sol))
    maindata=copy.deepcopy(EasyML_Page9.util.maindata)
    X_train, X_test, y_train, y_test = train_test_split(maindata.X, maindata.Y, stratify=maindata.Y,random_state=42)
    dt = MLPClassifier(
        random_state=42,max_iter=itr,hidden_layer_sizes=(hls,),alpha=alp,learning_rate_init=lri,
    learning_rate=lrm,activation=ac,solver=sol,)
    t0=time()
    dt.fit(X_train, y_train)
    Ac=dt.score(X_test, y_test)
    Tm=time()-t0
    EasyML_Page9.util.Xs.append(hls)
    EasyML_Page9.util.Ys.append(Ac*100)
    EasyML_Page9.util.Texts.append(
        "Time = {}, M_itr = {} , alph = {}, learing_rate = {}, activtor = {}, solver = {}".format(Tm,itr,alp,lri,ac,sol))
    print('done')

def graphic():
    print('here')
    return {
        'data': [
            go.Scatter(
                x=np.asarray(EasyML_Page9.util.Xs),
                y=np.asarray(EasyML_Page9.util.Ys),
                text=np.asarray(EasyML_Page9.util.Texts),
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