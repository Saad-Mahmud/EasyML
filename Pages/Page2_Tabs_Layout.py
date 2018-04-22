from DataProcessor import dtf,Color
import base64
import datetime
import io
import dash
from dash.dependencies import Input, Output,State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from EasyML_Init import EM_App
from Pages import EasyML_Page2 as EP
import urllib.parse
import copy




def maketab2():
    return html.Div([
        html.Div(
            [
                html.P(children='Select Column: ',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px',
                           'float': 'left',
                       }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page2_Dd_Tab2',
                        options=[{'label': i, 'value': i} for i in EP.util.maindata.available_indicators],
                        value=None, )],
                    style={
                        'position': 'relative',
                        'width': '20%',
                        'left': '3%',
                        'border': '1px',
                        'float': 'left',
                    }),
                html.Button(
                    'Apply',
                    id='Page2_Bt_Tab2',
                    style={
                        'position': 'relative',
                        'width': '40%',
                        'background-color': '#7386D5',
                        'border': '1px',
                        'float': 'right',
                        'color': 'white',
                        'right':'15%',
                        'font-size': '15px',
                        'font-family': 'Helvetica'
                    }),
                dcc.Graph(id='Page2_Tab2_Graph',
                          style={
                              'display': 'inline-block',
                              'position': 'relative',
                              'width': '100%',
                              'top': '10px',
                              'background': 'ghostwhite',
                          }
                          )
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '10px'
            }
        ),
    ])

@EM_App.callback(
    Output('Page2_Tab2_Graph', 'figure'),
    [Input('Page2_Dd_Tab2', 'value'),
     Input('Page2_Bt_Tab2', 'n_clicks')])
def page2_tabs2fun(value,clk):
    print("{}".format(value))
    if(value==None):return {}
    elif(clk==None):return {}
    elif(clk<=EP.util.Bt_Tab2):
        return maketab2graph()
    else:
        EP.util.Bt_Tab2_name=value
        EP.util.Bt_Tab2=clk
        return maketab2graph()

def maketab2graph():
    df=pd.value_counts(EP.util.maindata.df[EP.util.Bt_Tab2_name].values, sort=False)
    XX=np.array(df.keys().tolist())
    YY=np.array(df.tolist())
    return {
    'data': [

            go.Bar(
                x=XX,
                y=YY,
                text=XX,
                marker=dict(
                    color='#6d7fcc',
                    line=dict(
                        color='rgb(8,48,107)',
                        width=0.5,
                    )
                ),
                opacity=0.6)

            ],
    'layout': go.Layout(
            title=EP.util.Bt_Tab2_name,
            hovermode='closest'
        )
    }

def maketab1():
    return html.Div([
        html.Div(
            [
                html.P(children='X: ',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px',
                           'float': 'left',
                       }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page2_Dd_Tab11',
                        options=[{'label': i, 'value': i} for i in EP.util.maindata.available_indicators],
                        value=None, )],
                    style={
                        'position': 'relative',
                        'width': '20%',
                        'left': '1%',
                        'border': '1px',
                        'float': 'left',
                    }),
                html.P(children='Y: ',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px',
                           'float': 'left',
                           'left':'4%'
                       }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page2_Dd_Tab12',
                        options=[{'label': i, 'value': i} for i in EP.util.maindata.available_indicators],
                        value=None, )],
                    style={
                        'position': 'relative',
                        'width': '20%',
                        'left': '5%',
                        'border': '1px',
                        'float': 'left',
                    }),
                html.P(children='Label: ',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px',
                           'float': 'left',
                           'left': '8%'
                       }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page2_Dd_Tab13',
                        options=[{'label': i, 'value': i} for i in EP.util.maindata.available_indicators],
                        value=None, )],
                    style={
                        'position': 'relative',
                        'width': '20%',
                        'left': '9%',
                        'border': '1px',
                        'float': 'left',
                    }),
                html.Button(
                    'Apply',
                    id='Page2_Bt_Tab1',
                    style={
                        'position': 'relative',
                        'width': '15%',
                        'background-color': '#7386D5',
                        'border': '1px',
                        'float': 'right',
                        'color': 'white',
                        'right':'2%',
                        'font-size': '15px',
                        'font-family': 'Helvetica'
                    }),
                dcc.Graph(id='Page2_Tab1_Graph',
                          style={
                              'display': 'inline-block',
                              'position': 'relative',
                              'width': '100%',
                              'top': '10px',
                              'background': 'ghostwhite',
                          }
                          )
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '10px'
            }
        ),
    ])

@EM_App.callback(
    Output('Page2_Tab1_Graph', 'figure'),
    [Input('Page2_Dd_Tab11', 'value'),
     Input('Page2_Dd_Tab12', 'value'),
     Input('Page2_Dd_Tab13', 'value'),
     Input('Page2_Bt_Tab1', 'n_clicks'),])
def update_graph(X,Y,T,clk):

    if(X==None):return {}
    elif(clk==None):return {}
    elif (Y == None):return {}
    elif (T == None):return {}

    elif(clk<=EP.util.Bt_Tab1):
        return maketab1graph()
    else:
        EP.util.Bt_Tab1_X = X
        EP.util.Bt_Tab1_Y = Y
        EP.util.Bt_Tab1_T = T
        EP.util.Bt_Tab1=clk
        return maketab1graph()


def maketab1graph():
    X = np.array(EP.util.maindata.df[EP.util.Bt_Tab1_X])
    Y = np.array(EP.util.maindata.df[EP.util.Bt_Tab1_Y])
    T = np.array(EP.util.maindata.df[EP.util.Bt_Tab1_T])
    k = np.unique(T)
    Cmp = Color.makecolor(k)
    Xmp={i:[] for i in k}
    Ymp = {i: [] for i in k}
    for i in range(len(X)):
        Xmp[T[i]].append(X[i])
        Ymp[T[i]].append(Y[i])
    return {
        'data': [
            go.Scatter(
                x=Xmp[i],
                y=Ymp[i],
                text=i,
                mode='markers',
                name=i,
                marker={
                    'size': 15,
                    'color':Cmp[i],
                    'opacity': 0.5,
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )for i in k],
        'layout': go.Layout(
            xaxis={
                'title': EP.util.Bt_Tab1_X
            },
            yaxis={
                'title': EP.util.Bt_Tab1_Y
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

def maketab3():
    return html.Div([
        html.Div(
            [
                html.P(children='Label: ',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px',
                           'float': 'left',
                       }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page2_Dd_Tab31',
                        options=[{'label': i, 'value': i} for i in EP.util.maindata.available_indicators],
                        value=None, )],
                    style={
                        'position': 'relative',
                        'width': '20%',
                        'left': '1%',
                        'border': '1px',
                        'float': 'left',
                    }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page2_Dd_Tab32',
                        options=[{'label': 'Original', 'value': 0},{'label': 'Normalized', 'value': 1} ],
                        value=0, )],
                    style={
                        'position': 'relative',
                        'width': '20%',
                        'left': '5%',
                        'border': '1px',
                        'float': 'left',
                    }),
                html.Div([
                    html.Button(
                        'Get Download Link',
                        id='Page2_Bt_Tab3',
                        style={
                            'background-color': '#7386D5',
                            'border': '1px',
                            'color': 'white',
                            'font-size': '15px',
                            'font-family': 'Helvetica'
                        }),
                    html.Div(id='Page2_Dlink1'),

                ],style={
                            'position': 'relative',
                            'float': 'right',
                            'right': '2%',
                            'width':'30%'
                }),
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '10px'
            }
        ),
    ])

def finalData(rng1,rng2):
    if(rng2==0):
        csv_string = EP.util.maindata.df.to_csv(index=False, encoding='utf-8')
        csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
        return csv_string
    else:
        dff = copy.deepcopy(EP.util.maindata.df)
        lab=dff[rng1]
        dff=dff.drop(rng1,axis=1)
        print(dff.head)
        dff = (dff - dff.mean())
        print(dff.head)
        print((dff.max() - dff.min()))
        dff = dff/ (dff.max() - dff.min())
        dff[rng1]=lab
        print(dff.head())
        csv_string = dff.to_csv(index=False, encoding='utf-8')
        csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
        return csv_string

@EM_App.callback(Output('Page2_Dlink1', 'children'),
              [Input('Page2_Bt_Tab3', 'n_clicks'),
               Input('Page2_Dd_Tab31', 'value'),
               Input('Page2_Dd_Tab32', 'value')])
def Page2_dlink(value,rng1,rng2):
    print("{} {} {}".format(value,rng1,rng2))
    if(rng1==None):
        return html.Div([])
    if(value==None):
        return html.Div([])
    if (rng2 == None):
        return html.Div([])
    elif(value <= EP.util.Bt_Tab3):
        return html.Div([])
    else:
        EP.util.Bt_Tab3=value
        print('asdasd')
        return  [html.A(
            "Download Data(Manual)({})".format(value),
            id='download-link',
            download="rawdata.csv",
            href=finalData(rng1,rng2),
            target="_blank"
        )]
