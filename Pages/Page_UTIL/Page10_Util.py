from DataProcessor import dtf
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from EasyML_Init import EM_App
from Pages import EasyML_Page10
from Pages.Page_Graphics import Page10_SVM_Graphic


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
                        id='Page10_Dd_Label',
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
                        id='Page10_Bt_Label',
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
            html.Div(id='Page10_Algo',style={'background':'white','top':'25px'})

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

    def Page10_Algo_Maker(self,name):
        print('here2 {}'.format(self.isNone))
        if(self.isNone==True):
            return html.Div([])
        self.maindata.make_XY(name)

        return html.Div([

            html.Div(
                [
                    html.P(children='C = {}'.format(1.0),
                           id='Page10_C_l',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Slider(
                            id='Page10_C',
                            min=0.5,
                            max=100.0,
                            step=0.5,
                            value=1.0,
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
                    html.P(children='Gama = {}'.format(1.0/len(EasyML_Page10.util.maindata.available_indicators)),
                       id='Page10_Gama_l',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Slider(
                            id='Page10_Gama',
                            min=0.001,
                            max=1,
                            step=0.001,
                            value=1.0 / len(EasyML_Page10.util.maindata.available_indicators),
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
                    html.P(children='Degree = {}'.format(3),
                           id='Page10_Degree_l',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Slider(
                            id='Page10_Degree',
                            min=1,
                            max=10,
                            step=1,
                            value=3,
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
                    html.P(children='Kernel: ',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Dropdown(
                            id='Page10_Dd_Kernel',
                            options=[{'label': 'Linear', 'value': 'linear'},
                                     {'label': 'Polynomial', 'value': 'poly'},
                                     {'label': 'Sigmoid', 'value': 'sigmoid'},
                                     {'label': 'RBF', 'value': 'rbf'}],
                            value='poly', )],
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
                    html.P(children='Data: ',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(

                        [dcc.Dropdown(
                            id='Page10_Dd_Data',
                            options=[{'label': 'Original', 'value': 'ori'},
                                     {'label': 'Regularized', 'value': 'reg'}],
                            value='reg', )],
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
                        id='Page10_Bt_Algo',
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
                    dcc.Graph(id='Page10_graphic')
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



@EM_App.callback(Output('Page10_Algo', 'children'),
                 [dash.dependencies.Input('Page10_Dd_Label', 'value'),
                    dash.dependencies.Input('Page10_Bt_Label', 'n_clicks')])
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
    elif (click<=EasyML_Page10.util.N_Click_bt1):
        return html.Div([])
    else:
        EasyML_Page10.util.N_Click_bt1=click
        print('here')
        return EasyML_Page10.util.Page10_Algo_Maker(name)


#C
#gama
#Degree
#‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
#reg/ori

@EM_App.callback(Output('Page10_graphic', 'figure'),
              [Input('Page10_C', 'value'),
               Input('Page10_Gama', 'value'),
               Input('Page10_Degree', 'value'),
               Input('Page10_Dd_Kernel', 'value'),
               Input('Page10_Dd_Data', 'value'),
               Input('Page10_Bt_Algo', 'n_clicks')])
def display_value(c,ga,de,ke,da,click):
    print('{} {} {} {} {}'.format(c,ga,de,ke,da))
    if (click == None):
        return Page10_SVM_Graphic.dum()
    elif (click <= EasyML_Page10.util.N_Click_bt2):
        return Page10_SVM_Graphic.graphic()
    else:
        print('here')
        EasyML_Page10.util.N_Click_bt2 = click
        Page10_SVM_Graphic.algo(c, ga, de, ke, da)
        return Page10_SVM_Graphic.graphic()


@EM_App.callback(Output('Page10_C_l', 'children'),
              [Input('Page10_C', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'C ={}'.format(value)


@EM_App.callback(Output('Page10_Gama_l', 'children'),
              [Input('Page10_Gama', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Gama ={}'.format(value)

@EM_App.callback(Output('Page10_Degree_l', 'children'),
              [Input('Page10_Degree', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Degree ={}'.format(value)


