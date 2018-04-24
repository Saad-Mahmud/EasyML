from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from EasyML_Init import EM_App
from Pages.Page_Main import EasyML_Page11
from Pages.Page_Graphics import Page11_Ranker


def Page11_Butto_Init():
    EasyML_Page11.util.N_Click_LR = 0
    EasyML_Page11.util.N_Click_SVM = 0
    EasyML_Page11.util.N_Click_DT = 0
    EasyML_Page11.util.N_Click_RF = 0
    EasyML_Page11.util.N_Click_DL1 = 0
    EasyML_Page11.util.N_Click_DL2 = 0

def SVMDash():
    Page11_Butto_Init()
    return html.Div([
        html.Div(
            [
                html.P(children='C = {}'.format(1.0),
                       id='Page11_C_l',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px solid black',
                           'float': 'left',
                       }),
                html.Div(
                    [dcc.Slider(
                        id='Page11_C',
                        min=0.5,
                        max=100.0,
                        step=0.5,
                        value=1.0,
                    )],
                    style={
                        'position': 'relative',
                        'width': '30%',
                        'left': '3%',
                        'border': '1px solid black',
                        'float': 'left',
                    }),
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '20px'
            }
        ),

        html.Div(
            [
                html.P(children='Gama = {}'.format(1.0 / len(EasyML_Page11.util.maindata.available_indicators)),
                       id='Page11_Gama_l',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px solid black',
                           'float': 'left',
                       }),
                html.Div(
                    [dcc.Slider(
                        id='Page11_Gama',
                        min=0.001,
                        max=1,
                        step=0.001,
                        value=1.0 / len(EasyML_Page11.util.maindata.available_indicators),
                    )],
                    style={
                        'position': 'relative',
                        'width': '30%',
                        'left': '3%',
                        'border': '1px solid black',
                        'float': 'left',
                    }),
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '20px'
            }
        ),

        html.Div(
            [
                html.P(children='Degree = {}'.format(3),
                       id='Page11_Degree_l',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px solid black',
                           'float': 'left',
                       }),
                html.Div(
                    [dcc.Slider(
                        id='Page11_Degree',
                        min=1,
                        max=10,
                        step=1,
                        value=3,
                    )],
                    style={
                        'position': 'relative',
                        'width': '30%',
                        'left': '3%',
                        'border': '1px solid black',
                        'float': 'left',
                    }),
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '20px'
            }
        ),

        html.Div(
            [
                html.P(children='Kernel: ',
                       style={

                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px solid black',
                           'float': 'left',
                       }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page11_Dd_SVM_Kernel',
                        options=[{'label': 'Linear', 'value': 'linear'},],
                        value='linear', )],
                    style={
                        'position': 'relative',
                        'width': '20%',
                        'left': '3%',
                        'border': '1px solid black',
                        'float': 'left',
                    }),
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '20px'
            }
        ),
        html.Div([
            html.P(children='Data: ',
                   style={

                       'position': 'relative',
                       'font-size': '23px',
                       'border': '1px solid black',
                       'float': 'left',
                   }),
            html.Div(
                [dcc.Dropdown(
                    id='Page11_Dd_SVM_Data',
                    options=[{'label': 'Original', 'value': 'ori'},
                             {'label': 'Regularized', 'value': 'reg'}],
                    value='reg', )],
                style={
                    'position': 'relative',
                    'width': '20%',
                    'left': '3%',
                    'border': '1px solid black',
                    'float': 'left',
                }),
        ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '20px'
            }
        ),
        html.Div(
            [
                html.Button(
                    'Apply',
                    id='Page11_Bt_SVM',
                    style={
                        'position': 'relative',
                        'width': '20%',

                        'border': '1px solid black',
                        'float': 'left',
                    }),
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '20px'
            }
        ),
        html.Div(id='Page11_SVM_Rank', style=
        {
            'position': 'relative',
            'top': '40px',
        })

    ])


@EM_App.callback(Output('Page11_SVM_Rank', 'children'),
              [Input('Page11_C', 'value'),
               Input('Page11_Gama', 'value'),
               Input('Page11_Degree', 'value'),
               Input('Page11_Dd_SVM_Kernel', 'value'),
               Input('Page11_Dd_SVM_Data', 'value'),
               Input('Page11_Bt_SVM', 'n_clicks')
               ])
def display_value(c,g,d,k,dp,click):
    print('{} {} {} {} {} {}'.format(c,g,d,k,dp,click))
    if (click == None):
        return Page11_Ranker.dum()
    elif (click <= EasyML_Page11.util.N_Click_SVM):
        return Page11_Ranker.dum()
    else:
        EasyML_Page11.util.N_Click_SVM=click
        Page11_Ranker.SVMAlgo(c, g, d, k, dp)
        return Page11_Ranker.ranklist()

@EM_App.callback(Output('Page11_C_l', 'children'),
              [Input('Page11_C', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'C ={}'.format(value)


@EM_App.callback(Output('Page11_Gama_l', 'children'),
              [Input('Page11_Gama', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Gama ={}'.format(value)

@EM_App.callback(Output('Page11_Degree_l', 'children'),
              [Input('Page11_Degree', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Degree ={}'.format(value)

def LRDash():
    Page11_Butto_Init()
    return html.Div([
        html.Div(
            [
                html.P(children='Number of Iteration = {}'.format(10),
                       id='Page11_LR_Itr_l',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px solid black',
                           'float': 'left',
                       }),
                html.Div(
                    [dcc.Slider(
                        id='Page11_LR_Itr',
                        min=10,
                        max=300,
                        step=1,
                        value=1,
                    )],
                    style={
                        'position': 'relative',
                        'width': '30%',
                        'left': '3%',
                        'border': '1px solid black',
                        'float': 'left',
                    }),
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '20px'
            }
        ),
        html.Div(
            [
                html.P(children='Select Solver: ',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px solid black',
                           'float': 'left',
                       }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page11_Dd_LRsolver',
                        options=[{'label': 'newton-cg', 'value': 'newton-cg'},
                                 {'label': 'lbfgs', 'value': 'lbfgs'},
                                 {'label': 'liblinear(OVR only)', 'value': 'liblinear'},
                                 {'label': 'sag', 'value': 'sag'},
                                 ],
                        value='liblinear', )],
                    style={
                        'position': 'relative',
                        'width': '20%',
                        'left': '3%',
                        'border': '1px solid black',
                        'float': 'left',
                    }),
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '20px'
            }
        ),
        html.Div(
            [
                html.P(children='Select Algorithm: ',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px solid black',
                           'float': 'left',
                       }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page11_Dd_LRalgorithm',
                        options=[{'label': 'One-vs-Rest', 'value': 'ovr'},
                                 {'label': 'Multinomial', 'value': 'multinomial'}],
                        value='ovr', )],
                    style={
                        'position': 'relative',
                        'width': '20%',
                        'left': '3%',
                        'border': '1px solid black',
                        'float': 'left',
                    }),
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '20px'
            }
        ),

        html.Div(
            [
                html.Button(
                    'Apply',
                    id='Page11_Bt_LR',
                    style={
                        'position': 'relative',
                        'width': '20%',

                        'border': '1px solid black',
                        'float': 'left',
                    }),
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '20px'
            }
        ),
        html.Div(id='Page11_LR_Rank', style=
        {
            'position': 'relative',
            'top': '40px',
        })
    ],style={'position':'relative','top':'5%'})



@EM_App.callback(Output('Page11_LR_Rank', 'children'),
              [Input('Page11_LR_Itr', 'value'),
               Input('Page11_Dd_LRsolver', 'value'),
               Input('Page11_Dd_LRalgorithm', 'value'),
               Input('Page11_Bt_LR', 'n_clicks')
               ])
def display_value(itr,sol,al,click):
    print('{} {} {} {}'.format(itr,sol,al,click))
    if (click == None):
        return Page11_Ranker.dum()
    elif (click <= EasyML_Page11.util.N_Click_LR):
        return Page11_Ranker.dum()
    else:
        print('here')
        EasyML_Page11.util.N_Click_LR = click
        Page11_Ranker.LRAlgo(itr, sol, al)
        return Page11_Ranker.ranklist()



@EM_App.callback(Output('Page11_LR_Itr_l', 'children'),
              [Input('Page11_LR_Itr', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Number of Iteration ={}'.format(value)


