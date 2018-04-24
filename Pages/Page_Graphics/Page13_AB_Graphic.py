from Pages.Page_Main import EasyML_Page13
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import copy
from time import time
import plotly.graph_objs as go
import numpy as np


def algo(lr,ne,al):
    print('{} {} {}'.format(lr,ne,al))
    maindata=copy.deepcopy(EasyML_Page13.util.maindata)
    X_train, X_test, y_train, y_test = train_test_split(maindata.X, maindata.Y, stratify=maindata.Y,random_state=42)

    ap = DecisionTreeClassifier()
    if(al==2):
        ap = RandomForestClassifier(n_estimators=15, random_state=42)
    elif(al==3):
        ap = LogisticRegression()
    dt = AdaBoostClassifier(base_estimator=ap, n_estimators=ne,learning_rate=lr,random_state=42)
    t0=time()
    dt.fit(X_train, y_train)
    Ac=dt.score(X_test, y_test)
    Tm=time()-t0
    EasyML_Page13.util.Xs.append(ne)
    EasyML_Page13.util.Ys.append(Ac * 100)
    EasyML_Page13.util.Texts.append("Time = {}, learning_rate = {}".format(Tm, lr))
    print('done')

def graphic():
    print('here')
    return {
        'data': [
            go.Scatter(
                x=np.asarray(EasyML_Page13.util.Xs),
                y=np.asarray(EasyML_Page13.util.Ys),
                text=np.asarray(EasyML_Page13.util.Texts),
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
                'title': 'n_estimators',
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
                'title': 'n_estimators',
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