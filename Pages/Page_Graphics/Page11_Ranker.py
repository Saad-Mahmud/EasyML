from Pages import EasyML_Page11
from sklearn.feature_selection import RFE
from DataProcessor import dtf
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import copy
import dash_html_components as html
import dash_core_components as dcc
from time import time
from sklearn.svm import SVC
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import urllib.parse
import dash
from dash.dependencies import Input, Output
from EasyML_Init import EM_App

def LRAlgo(itr,sol,al):
    if(sol=='liblinear' and al=='multinomial'):return
    print('{} {} {}'.format(itr,sol,al))
    maindata=copy.deepcopy(EasyML_Page11.util.maindata)
    lr = LogisticRegression(max_iter=itr,multi_class=al,solver=sol)
    rfe = RFE(lr)
    rfe = rfe.fit(maindata.X,maindata.Y)
    print(rfe.ranking_)
    EasyML_Page11.util.RankofF=[]
    EasyML_Page11.util.RankofF=[(maindata.features[i],rfe.ranking_[i])for  i in range(maindata.N_features)]
    EasyML_Page11.util.RankofF=sorted(EasyML_Page11.util.RankofF, key=lambda rf: rf[1])
    print(EasyML_Page11.util.RankofF)
    print('done')

def SVMAlgo(c,g,d,k,dp):

    print('{} {} {} {} {}'.format(c,g,d,k,dp))
    maindata=copy.deepcopy(EasyML_Page11.util.maindata)
    if(dp=='reg'):
        min_train = maindata.X.min(axis=0)
        range_train = 0.1+(maindata.X - min_train).max(axis=0)
        maindata.X = (maindata.X - min_train) / range_train

    dt = SVC(random_state=42,C=c,gamma=g,degree=d,kernel=k)
    rfe = RFE(dt)
    rfe = rfe.fit(maindata.X,maindata.Y)
    print(rfe.ranking_)
    EasyML_Page11.util.RankofF=[]
    EasyML_Page11.util.RankofF=[(maindata.features[i],rfe.ranking_[i])for  i in range(maindata.N_features)]
    EasyML_Page11.util.RankofF=sorted(EasyML_Page11.util.RankofF, key=lambda rf: rf[1])
    print(EasyML_Page11.util.RankofF)
    print('done')


def finalData(data):
    dff = copy.deepcopy(EasyML_Page11.util.maindata.df)
    ff=[]
    ff.append(EasyML_Page11.util.maindata.labelname)
    for i in data:
        ff.append(i)
    print(ff)
    dff=dff[ff]
    print(dff.head())
    csv_string = dff.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
    return csv_string

def finalDataR(l,r):
    dff = copy.deepcopy(EasyML_Page11.util.maindata.df)
    ff=[]
    ff.append(EasyML_Page11.util.maindata.labelname)
    for i in range(l,r+1):
        ff.append(EasyML_Page11.util.RankofF[i][0])
    print(ff)
    dff=dff[ff]
    print(dff.head())
    csv_string = dff.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
    return csv_string

def ranklist():


    return html.Div([
        html.H6("Download Option:"),
        dcc.Dropdown(
            options=[
                {'label': 'Select Range', 'value': 0},
                {'label': 'Select Manually', 'value': 1},
            ],
            value=None,
            id='Page11_Dlop'
        ),
        html.Div(id='Page11_Dlink1'),
        html.Div(id='Page11_Dlink2'),
        html.Div(id='Page11_Flist')
    ])



def dum():
    html.Div([])


@EM_App.callback(Output('Page11_Frange_l', 'children'),
              [Input('Page11_Frange', 'value')])
def update_graphic(value):
    print(" Slider {} {}".format(value[0],value[1]))
    return 'Select Range [ {} - {} ]: '.format(value[0]+1,value[1]+1)


@EM_App.callback(Output('Page11_Flist', 'children'),
              [Input('Page11_Dlop', 'value')])
def update_graphic(value):
    if(value==0):
        return html.Div([
            html.Button(
                'Get Download link',
                id='Page11_Bt_Rdl',
                style={
                    'position': 'relative',
                    'width': '18%',
                    'border': '1px solid black',
                    'float': 'left',
                }),
            html.P(children='Select Range [ {} - {} ]: '.format(1, 3),
                   id='Page11_Frange_l',
                   style={
                       'position': 'relative',
                       'font-size': '23px',
                       'border': '1px solid black',
                       'left':'10%',
                       'float': 'left',
                   }),
                html.Div(
                    [dcc.RangeSlider(
                        id='Page11_Frange',
                        count=1,
                        min=0,
                        max=EasyML_Page11.util.maindata.N_features - 1,
                        step=1,
                        value=[0, 2]
                    )],
                    style={
                        'position': 'relative',
                        'width': '28%',
                        'top':'10px',
                        'left':'12%',
                        'border': '1px solid black',
                        'float': 'left',
                    }),
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '25px'
            }
        )
    elif(value==1):
        return html.Div([
            html.Button(
                'Get Download link',
                id='Page11_Bt_Sdl',
                style={
                    'position': 'relative',
                    'width': '18%',
                    'border': '1px solid black',
                    'float': 'left',
                }),
            html.P(children='Select Manually(Ranked):',
                   style={
                       'position': 'relative',
                       'font-size': '23px',
                       'border': '1px solid black',
                       'left': '10%',
                       'float': 'left',
                   }),
            html.Div(
                [
                    dcc.Checklist(
                        options=[
                            {'label': '{} [{}]'.format(i[0],i[1]), 'value': i[0]} for i in EasyML_Page11.util.RankofF
                        ],
                        values=[],
                        id='Page11_Fsel',
                    )
                ],
                style={
                    'position': 'relative',
                    'width': '20%',
                    'left': '20%',
                    'border': '1px solid black',
                    'float': 'left',
                }),

        ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '25px'
            }
        )

@EM_App.callback(Output('Page11_Dlink1', 'children'),
              [Input('Page11_Bt_Rdl', 'n_clicks'),
               Input('Page11_Frange', 'value')])
def dlink1(value,rng):
    if(value==None):
        return html.Div([])
    elif (value <= EasyML_Page11.util.N_Click_DL1):
        return html.Div([])
    else:
        EasyML_Page11.util.N_Click_DL1=value
        return  [html.A(
            "Download Data(Range)({})".format(value),
            id='download-link',
            download="rawdata.csv",
            href=finalDataR(rng[0],rng[1]),
            target="_blank"
        )]

@EM_App.callback(Output('Page11_Dlink2', 'children'),
              [Input('Page11_Bt_Sdl', 'n_clicks'),
               Input('Page11_Fsel', 'values')])
def dlink2(value,rng):
    if(rng==None):
        return html.Div([])
    if(value==None):
        return html.Div([])
    elif(value <= EasyML_Page11.util.N_Click_DL2):
        return html.Div([])
    else:
        EasyML_Page11.util.N_Click_DL2=value
        return  [html.A(
            "Download Data(Manual)({})".format(value),
            id='download-link',
            download="rawdata.csv",
            href=finalData(rng),
            target="_blank"
        )]
