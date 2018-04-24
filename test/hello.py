
from DataProcessor import DataFrame
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import copy
from time import time
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from sklearn import datasets
iris = datasets.load_iris()

def algo(lr,dt,rf,gnb):
    print('{} {} {} {}'.format(lr,dt,rf,gnb))
    X = iris.data
    Y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X,Y, stratify=Y,random_state=42)

    ap = LogisticRegression()
    #ap2 = DecisionTreeClassifier()('dt', ap2),
    #ap3 = RandomForestClassifier(n_estimators=15)('rf', ap3),
    ap5 = GaussianNB()
    dt = VotingClassifier(estimators=[('lr', ap),   ('gnb', ap5)], voting='soft',weights=[1, 1])

    t0=time()
    dt.fit(X_train, y_train)
    Ac=dt.score(X_test, y_test)
    Tm=time()-t0