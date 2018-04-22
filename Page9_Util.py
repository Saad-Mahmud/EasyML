from DataProcessor import dtf
import base64
import datetime
import io
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from EasyML_Init import EM_App
import EasyML_Page9
import Page9_MLP_Graphic

class putil():

    def page_contents(self):
        if (self.isNone==True):
            return html.Div()
        df2=self.maindata.df[:5]
        return html.Div([

            html.Div(
                [html.H5(self.maindata.filename + '(First 5 row)'),
                dt.DataTable(rows=df2.to_dict('records'))],
                style={
                    'position': 'relative',
                    'border' : '1px solid black',
                    'top': '15px'
                }
            ),

            html.Div(
                [
                    html.P(children='Select Label: ',
                            style={
                                'position':'relative',
                                'font-size':'23px',
                                'border':'1px',
                                'float':'left',
                                'font-family': 'Helvetica'
                            }),
                    html.Div(
                        [dcc.Dropdown(
                        id='Page9_Dd_Label',
                        options=[{'label': i, 'value': i} for i in self.maindata.available_indicators],
                        value=None,)],
                        style={
                            'position': 'relative',
                            'width': '20%',
                            'left': '3%',
                            'border': '1px solid black',
                            'float': 'left',
                        }),
                    html.Button(
                        'Apply',
                        id='Page9_Bt_Label',
                        style={
                            'position': 'relative',
                            'background-color': '#7386D5',
                            'width': '20%',
                            'left': '6%',
                            'border': '1px',
                            'float': 'left',
                            'color': 'white',
                            'font-size': '15px',
                            'font-family': 'Helvetica'
                        }),
                ],
                style={
                    'display': 'inline-block',
                    'position': 'relative',
                    'width': '100%',
                    'top': '50px',
                    'background': 'ghostwhite'
                }
            ),
            html.Div(id='Page9_Algo',style={'background':'white','top':'25px'})

        ],style={
            'position' : 'relative',
            'align': 'center'
        }
        )

    def __init__(self,contents=None, names=None, dates=None):
        print('')
        if(names==None):
            self.isNone=True
        else:
            self.isNone = False
            self.maindata=dtf.dtf(contents, names, dates)
            self.N_Click_bt1=0
            self.N_Click_bt2 = 0
            self.Xs=[]
            self.Ys=[]
            self.Texts=[]
        return

    def Page9_Algo_Maker(self,name):
        print('here2 {}'.format(self.isNone))
        if(self.isNone==True):
            return html.Div([])
        self.maindata.make_XY(name)

        return html.Div([

            html.Div(
                [
                    html.P(children='Hidden_layer_sizes = {}'.format(5),
                           id='Page9_Hidden_layer_sizes_l',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Slider(
                            id='Page9_Hidden_layer_sizes',
                            min=5,
                            max=400,
                            step=5,
                            value=5,
                        )],
                        style={
                            'position': 'relative',
                            'width': '65%',
                            'border': '1px',
                            'float': 'right',
                            'right': '5%',
                            'top': '12px'
                        }),
                ],    style={
                    'display': 'inline-block',
                    'position': 'relative',
                    'width': '100%',
                    'top': '50px',
                    'background': 'ghostwhite'
                }),

                html.Div(
                    [
                        html.P(children='Max iter = {}'.format(30),
                                id='Page9_Max_iter_l',
                               style={
                                   'position': 'relative',
                                   'font-size': '23px',
                                   'border': '1px',
                                   'float': 'left',
                                   'font-family': 'Helvetica'
                               }),
                        html.Div(
                            [dcc.Slider(
                                id='Page9_Max_iter',
                                min=30,
                                max=1200,
                                step=30,
                                value=30,
                            )],
                            style={
                                'position': 'relative',
                                'width': '65%',
                                'border': '1px',
                                'float': 'right',
                                'right': '5%',
                                'top': '12px'
                            }),
                    ],    style={
                    'display': 'inline-block',
                    'position': 'relative',
                    'width': '100%',
                    'top': '50px',
                    'background': 'ghostwhite'
                }
            ),


            html.Div(
                [
                    html.P(children='Alpha = {}'.format(0.001),
                   id='Page9_Alpha_l',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Slider(
                            id='Page9_Alpha',
                            min=0.001,
                            max=0.999,
                            step=0.005,
                            value=0.001,
                        )],
                        style={
                            'position': 'relative',
                            'width': '65%',
                            'border': '1px',
                            'float': 'right',
                            'right': '5%',
                            'top': '12px'
                        }),
                ],    style={
                    'display': 'inline-block',
                    'position': 'relative',
                    'width': '100%',
                    'top': '50px',
                    'background': 'ghostwhite'
                }
            ),

                html.Div(
                    [
                        html.P(children='Learning rate = {}'.format(0.001),
                           id='Page9_Learning_rate_init_l',
                               style={
                                   'position': 'relative',
                                   'font-size': '23px',
                                   'border': '1px',
                                   'float': 'left',
                                   'font-family': 'Helvetica'
                               }),
                        html.Div(
                            [dcc.Dropdown(
                                id='Page9_Dd_Learning_rate_init',
                                options=[{'label': 'Constant', 'value': 'constant'},
                                         {'label': 'Invscaling', 'value': 'invscaling'},
                                         {'label': 'Adaptive', 'value': 'adaptive'}],
                                value='constant', )],
                            style={
                                'position': 'relative',
                                'width': '30%',
                                'border': '1px',
                                'float': 'right',
                                'right': '5%',
                                'top': '3px'
                            }),
                        html.Div(
                            [dcc.Slider(
                                id='Page9_Learning_rate_init',
                                min=0.001,
                                max=0.999,
                                step=0.005,
                                value=0.001,
                            )],
                            style={
                                'position': 'relative',
                                'width': '30%',
                                'border': '1px',
                                'float': 'right',
                                'right': '10%',
                                'top': '12px'
                            }),

                    ],    style={
                    'display': 'inline-block',
                    'position': 'relative',
                    'width': '100%',
                    'top': '50px',
                    'background': 'ghostwhite'
                }
            ),

            html.Div(
                [
                    html.P(children='Activation Function: ',
                           id='Page8_Estimators_l',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Dropdown(
                            id='Page9_Dd_Activation',
                            options=[{'label': 'Identity', 'value': 'identity'},
                                     {'label': 'Logistic', 'value': 'logistic'},
                                     {'label': 'Tanh', 'value': 'tanh'},
                                     {'label': 'Relu', 'value': 'relu'}],
                            value='relu', )],
                        style={
                            'position': 'relative',
                            'width': '65%',
                            'border': '1px',
                            'float': 'right',
                            'right': '5%',
                            'top': '3px'
                        }),
                ],
                style={
                    'display': 'inline-block',
                    'position': 'relative',
                    'width': '100%',
                    'top': '50px',
                    'background': 'ghostwhite'
                }
            ),

            html.Div(
                [
                    html.P(children='Solver: ',
                           id='Page8_Estimators_l',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(

                        [dcc.Dropdown(
                            id='Page9_Dd_Solver',
                            options=[{'label': 'Stochastic gradient descent', 'value': 'sgd'},
                                     {'label': 'lbfgs', 'value': 'lbfgs'},
                                     {'label': 'Stochastic gradient descent(adam)', 'value': 'adam'}],
                            value='sgd', )],
                        style={
                            'position': 'relative',
                            'width': '65%',
                            'border': '1px',
                            'float': 'right',
                            'right': '5%',
                            'top': '3px'
                        }),
                ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '50px',
                'background': 'ghostwhite'
            }
        ),
            html.Div(
                [
                    html.Button(
                        'Apply',
                        id='Page9_Bt_Algo',
                        style={
                            'position': 'relative',
                            'width': '20%',
                            'background-color':'#7386D5',
                            'border': '1px',
                            'float': 'left',
                            'color': 'white',
                            'font-size': '15px',
                            'font-family':'Helvetica'
                        }),
                ],
                style={
                    'display': 'inline-block',
                    'position': 'relative',
                    'width': '100%',
                    'top': '50px',
                    'background':'ghostwhite',
                }
            ),

            html.Div(
                [
                    html.Div([
                        html.Div([html.H6('Layer Size Vs Accurecy(%)')], id='p8gl1', style={
                            'textAlign': 'center',
                            'font-size': '30px',
                            'color':'white',
                            'font-family':'Helvetica'
                        })
                    ]),
                    dcc.Graph(id='Page9_graphic')
                ],
                style={
                    'position': 'relative',
                    'border':'1px solid black',
                    'background':'#7386D5',
                    'width': '100%',
                    'top': '50px'
                }
            )

        ],style={
                'top': '20%'
            })



@EM_App.callback(Output('Page9_Algo', 'children'),
                 [dash.dependencies.Input('Page9_Dd_Label', 'value'),
                    dash.dependencies.Input('Page9_Bt_Label', 'n_clicks')])
def update_ui(name,click):
    print("Debug: {} & {}".format(name,click))
    if(name==None):
        return [html.P("---------------- Select a Label---------------",
                       style={
            'font-size': '15px',
            'color': 'red'
        })]
    elif(click==None):
        return [html.P('',
                       style={
                           'font-size': '15px',
                           'font-color': 'red'
                       })]
    elif (click<=EasyML_Page9.util.N_Click_bt1):
        return html.Div([])
    else:
        EasyML_Page9.util.N_Click_bt1=click
        print('here')
        return EasyML_Page9.util.Page9_Algo_Maker(name)


#Page9_Hidden_layer_sizes
#Page9_Max_iter
#Page9_Dd_Activation
#Page9_Dd_Solver
#Page9_Alpha
#Page9_Learning_rate_init
#Page9_Dd_Learning_rate_init

@EM_App.callback(Output('Page9_graphic', 'figure'),
              [Input('Page9_Hidden_layer_sizes', 'value'),
               Input('Page9_Max_iter', 'value'),
               Input('Page9_Alpha', 'value'),
               Input('Page9_Learning_rate_init', 'value'),
               Input('Page9_Dd_Learning_rate_init', 'value'),
               Input('Page9_Dd_Activation', 'value'),
               Input('Page9_Dd_Solver', 'value'),
               Input('Page9_Bt_Algo', 'n_clicks')
               ])
def display_value(hls,itr,alp,lri,lrm,ac,sol,click):
    print('{} {} {} {} {} {} {}'.format(hls,itr,alp,lri,lrm,ac,sol))
    if (click == None):
        return Page9_MLP_Graphic.dum()
    elif (click <= EasyML_Page9.util.N_Click_bt2):
        return Page9_MLP_Graphic.graphic()
    else:
        print('here')
        EasyML_Page9.util.N_Click_bt2 = click
        Page9_MLP_Graphic.algo(hls,itr,alp,lri,lrm,ac,sol)
        return Page9_MLP_Graphic.graphic()


@EM_App.callback(Output('Page9_Hidden_layer_sizes_l', 'children'),
              [Input('Page9_Hidden_layer_sizes', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Hidden_layer_sizes ={}'.format(value)


@EM_App.callback(Output('Page9_Max_iter_l', 'children'),
              [Input('Page9_Max_iter', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Max iter ={}'.format(value)

@EM_App.callback(Output('Page9_Alpha_l', 'children'),
              [Input('Page9_Alpha', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Alpha ={}'.format(value)


@EM_App.callback(Output('Page9_Learning_rate_init_l', 'children'),
              [Input('Page9_Learning_rate_init', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Learning rate ={}'.format(value)


