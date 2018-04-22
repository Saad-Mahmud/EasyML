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
import EasyML_Page6
import Page6_LR_Graphic

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
                        id='Page6_Dd_Label',
                        options=[{'label': i, 'value': i} for i in self.maindata.available_indicators],
                        value=None,)],
                        style={
                            'position': 'relative',
                            'width': '20%',
                            'left': '3%',
                            'border': '1px',
                            'float': 'left',
                            'top' : '3px'
                        }),
                    html.Button(
                        'Apply',
                        id='Page6_Bt_Label',
                        style={
                            'position': 'relative',
                            'background-color': '#7386D5',
                            'width': '20%',
                            'left': '6%',
                            'border': '1px',
                            'float': 'left',
                            'color': 'white',
                            'font-size':'15px',
                            'font-family': 'Helvetica'
                        }),
                ],
                style={
                    'display': 'inline-block',
                    'position': 'relative',
                    'width': '100%',
                    'top': '50px',
                    'background':'ghostwhite'
                }
            ),
            html.Div(id='Page6_Algo',style={'background':'white','top':'25px'})

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

    def Page6_Algo_Maker(self,name):
        print('here2 {}'.format(self.isNone))
        if(self.isNone==True):
            return html.Div([])
        self.maindata.make_XY(name)

        return html.Div([
            html.Div(
                [
                    html.P(children='Number of Iteration = {}'.format(10),
                           id='Page6_Itr_Label',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Slider(
                            id='Page6_Itr',
                            min=10,
                            max=300,
                            step=1,
                            value=1,
                        )],
                        style={
                            'position': 'relative',
                            'width': '65%',
                            'border': '1px',
                            'float': 'right',
                            'right': '5%',
                            'top': '12px'
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
                    html.P(children='Select Solver: ',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(

                        [dcc.Dropdown(
                            id='Page6_Dd_LRsolver',
                            options=[{'label': 'newton-cg', 'value': 'newton-cg'},
                                     {'label': 'lbfgs', 'value': 'lbfgs'},
                                     {'label': 'liblinear(OVR only)', 'value': 'liblinear'},
                                     {'label': 'sag', 'value': 'sag'},
                                     ],
                            value='liblinear', )],
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
                    html.P(children='Select Algorithm: ',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Dropdown(
                            id='Page6_Dd_LRalgorithm',
                            options=[{'label': 'One-vs-Rest', 'value': 'ovr'},
                                     {'label': 'Multinomial', 'value': 'multinomial'}],
                            value='ovr', )],
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
                        id='Page6_Bt_Algo',
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
                        html.Div([html.H6('Maxtr Vs Accurecy(%)')], id='p6gl1', style={
                            'textAlign': 'center',
                            'font-size': '30px',
                            'color':'white',
                            'font-family':'Helvetica'
                        })
                    ]),
                    dcc.Graph(id='Page6_graphic')
                ],
                style={
                    'position': 'relative',
                    'border':'1px solid black',
                    'background':'#7386D5',
                    'width': '100%',
                    'top': '50px'
                }
            ),
        ],
            style={
                'top': '20%'
            })


@EM_App.callback(Output('Page6_Algo', 'children'),
                 [dash.dependencies.Input('Page6_Dd_Label', 'value'),
                    dash.dependencies.Input('Page6_Bt_Label', 'n_clicks')])
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
    elif (click<=EasyML_Page6.util.N_Click_bt1):
        return html.Div([])
    else:
        EasyML_Page6.util.N_Click_bt1=click
        print('here')
        return EasyML_Page6.util.Page6_Algo_Maker(name)


@EM_App.callback(Output('Page6_graphic', 'figure'),
              [Input('Page6_Itr', 'value'),
               Input('Page6_Dd_LRsolver', 'value'),
               Input('Page6_Dd_LRalgorithm', 'value'),
               Input('Page6_Bt_Algo', 'n_clicks')
               ])
def display_value(itr,sol,al,click):
    print('{} {} {} {}'.format(itr,sol,al,click))
    if (click == None):
        return Page6_LR_Graphic.dum()
    elif (click <= EasyML_Page6.util.N_Click_bt2):
        return Page6_LR_Graphic.graphic()
    else:
        print('here')
        EasyML_Page6.util.N_Click_bt2 = click
        Page6_LR_Graphic.algo(itr,sol,al)
        return Page6_LR_Graphic.graphic()



@EM_App.callback(Output('Page6_Itr_Label', 'children'),
              [Input('Page6_Itr', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Number of Iteration ={}'.format(value)


