from DataProcessor import DataFrame
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from EasyML_Init import EM_App
from Pages.Page_Main import EasyML_Page5
from Pages.Page_Graphics import Page5_KNN_Graphic


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
                    'border' : '1px',
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
                        id='Page5_Dd_Label',
                        options=[{'label': i, 'value': i} for i in self.maindata.available_indicators],
                        value=None,)],
                        style={
                            'position': 'relative',
                            'width': '20%',
                            'left': '3%',
                            'border': '1px',
                            'float': 'left',
                            'top': '3px'
                        }),
                    html.Button(
                        'Apply',
                        id='Page5_Bt_Label',
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
            html.Div(id='Page5_Algo',style={'background':'white','top':'25px'})

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
            self.maindata=DataFrame.dtf(contents, names, dates)
            self.N_Click_bt1=0
            self.N_Click_bt2 = 0
            self.Xs=[]
            self.Ys=[]
            self.Texts=[]
        return

    def Page5_Algo_Maker(self,name):
        print('here2 {}'.format(self.isNone))
        if(self.isNone==True):
            return html.Div([])
        self.maindata.make_XY(name)

        return html.Div([
            html.Div([

            html.P(children='Value of K = {}'.format(1),
                    id='Page5_NN_Label',
                   style={
                       'position': 'relative',
                       'font-size': '23px',
                       'border': '1px',
                       'float': 'left',
                       'font-family': 'Helvetica'
                   }),
            html.Div(
                [dcc.Slider(
                    id='Page5_NN',
                    min=1,
                    max=30,
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
            html.Div([

                html.P(children='Select Weights: ',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px',
                           'float': 'left',
                           'font-family': 'Helvetica'
                       }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page5_Dd_KNNweight',
                        options=[{'label': 'Uniform', 'value': 'uniform'},
                                 {'label': 'Distance', 'value': 'distance'},
                                 ],
                        value='uniform', )],
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
            html.Div([

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
                        id='Page5_Dd_KNNalgorithm',
                        options=[{'label': 'BallTree', 'value': 'ball_tree'},
                                 {'label': 'KDTree', 'value': 'kd_tree'},
                                 {'label': 'Brute-Force', 'value': 'brute'},
                                 {'label': 'Help Me', 'value': 'auto'}],
                        value='auto', )],
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
            html.Div([

                html.P(children='Distance: ',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px',
                           'float': 'left',
                           'font-family': 'Helvetica'
                       }),
                html.Div(
                        [dcc.Dropdown(
                            id='Page5_Dd_KNNdistance',
                            options=[{'label': 'Manhattan_distance', 'value': 1},
                                     {'label': 'Euclidean_distance', 'value': 2},
                                     {'label': 'Minkowski_distance', 'value': 3},
                                     ],
                            value=2, )],
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
                        id='Page5_Bt_Algo',
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
                        html.Div([html.H6('K Vs Accurecy(%)')], id='p5gl1',  style={
                            'textAlign': 'center',
                            'font-size': '30px',
                            'color':'white',
                            'font-family':'Helvetica'
                        })
                    ]),
                    dcc.Graph(id='Page5_graphic')
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
            }
        )


@EM_App.callback(Output('Page5_Algo', 'children'),
                 [dash.dependencies.Input('Page5_Dd_Label', 'value'),
                    dash.dependencies.Input('Page5_Bt_Label', 'n_clicks')])
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
    elif (click <= EasyML_Page5.util.N_Click_bt1):
        return html.Div([])
    else:
        EasyML_Page5.util.N_Click_bt1=click
        print('here')
        return EasyML_Page5.util.Page5_Algo_Maker(name)


@EM_App.callback(Output('Page5_graphic', 'figure'),
              [Input('Page5_NN', 'value'),
               Input('Page5_Dd_KNNweight', 'value'),
               Input('Page5_Dd_KNNalgorithm', 'value'),
               Input('Page5_Dd_KNNdistance', 'value'),
               Input('Page5_Bt_Algo', 'n_clicks')
               ])
def display_value(Kn,Wg,Al,Dm,click):
    print('{} {} {} {} {}'.format(Kn,Wg,Al,Dm,click))
    if (click == None):
        return Page5_KNN_Graphic.dum()
    elif (click <= EasyML_Page5.util.N_Click_bt2):
        return Page5_KNN_Graphic.graphic()
    else:
        print('here')
        EasyML_Page5.util.N_Click_bt2 = click
        Page5_KNN_Graphic.algo(Kn, Wg, Al, Dm)
        return Page5_KNN_Graphic.graphic()



@EM_App.callback(Output('Page5_NN_Label', 'children'),
              [Input('Page5_NN', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Value of K = {}'.format(value)


