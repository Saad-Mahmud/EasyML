from Pages.Page_Main import EasyML_Page5
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import copy
from time import time
import plotly.graph_objs as go
import numpy as np


def algo(Kn,Wg,Al,Dm):
    print('{} {} {} {}'.format(Kn,Wg,Al,Dm))
    maindata=copy.deepcopy(EasyML_Page5.util.maindata)
    X_train, X_test, y_train, y_test = train_test_split(maindata.X, maindata.Y, stratify=maindata.Y,random_state=42)
    knn = KNeighborsClassifier(n_neighbors=Kn,weights=Wg,algorithm=Al,p=Dm)
    t0=time()
    knn.fit(X_train, y_train)
    Ac=knn.score(X_test, y_test)
    Tm=time()-t0
    EasyML_Page5.util.Xs.append(Kn)
    EasyML_Page5.util.Ys.append(Ac * 100)
    EasyML_Page5.util.Texts.append("Time = {}, Algo = {}, Distance = {}, Weight={}".format(Tm, Al, Dm, Wg))
    print('done')

def graphic():
    print('here')
    return {
        'data': [
            go.Scatter(
                x=np.asarray(EasyML_Page5.util.Xs),
                y=np.asarray(EasyML_Page5.util.Ys),
                text=np.asarray(EasyML_Page5.util.Texts),
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
                'title': 'K',
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
                'title': 'K',
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