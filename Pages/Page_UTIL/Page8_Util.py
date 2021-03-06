from DataProcessor import DataFrame
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from EasyML_Init import EM_App
from Pages.Page_Main import EasyML_Page8
from Pages.Page_Graphics import Page8_RF_Graphic


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
                        id='Page8_Dd_Label',
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
                        id='Page8_Bt_Label',
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
            html.Div(id='Page8_Algo',style={'background':'white','top':'25px'})

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

    def Page8_Algo_Maker(self,name):
        print('here2 {}'.format(self.isNone))
        if(self.isNone==True):
            return html.Div([])
        self.maindata.make_XY(name)

        return html.Div([

            html.Div(
                [
                    html.P(children='Estimators = {}'.format(1),
                           id='Page8_Estimators_l',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Slider(
                            id='Page8_Estimators',
                            min=1,
                            max=40,
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
                    html.P(children='Max Depth = {}'.format(2),
                           id='Page8_Maxdepth_l',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Slider(
                            id='Page8_Maxdepth',
                            min=2,
                            max=40,
                            step=1,
                            value=2,
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
                    html.P(children='Min Samples Split = {}'.format(2),
                           id='Page8_Mss_l',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Slider(
                            id='Page8_Mss',
                            min=2,
                            max=20,
                            step=1,
                            value=2,
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
                    html.P(children='Max Features = {}'.format(2),
                           id='Page8_MxF_l',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px',
                               'float': 'left',
                               'font-family': 'Helvetica'
                           }),
                    html.Div(
                        [dcc.Slider(
                            id='Page8_MxF',
                            min=1,
                            max=len(self.maindata.available_indicators) - 1,
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
                    html.Button(
                        'Apply',
                        id='Page8_Bt_Algo',
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
                        html.Div([html.H6('N_Estimators Vs Accurecy(%)')], id='p8gl1', style={
                            'textAlign': 'center',
                            'font-size': '30px',
                            'color':'white',
                            'font-family':'Helvetica'
                        })
                    ]),
                    dcc.Graph(id='Page8_graphic')
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


@EM_App.callback(Output('Page8_Algo', 'children'),
                 [dash.dependencies.Input('Page8_Dd_Label', 'value'),
                    dash.dependencies.Input('Page8_Bt_Label', 'n_clicks')])
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
    elif (click <= EasyML_Page8.util.N_Click_bt1):
        return html.Div([])
    else:
        EasyML_Page8.util.N_Click_bt1=click
        print('here')
        return EasyML_Page8.util.Page8_Algo_Maker(name)


@EM_App.callback(Output('Page8_graphic', 'figure'),
              [Input('Page8_Estimators', 'value'),
               Input('Page8_Maxdepth', 'value'),
               Input('Page8_Mss', 'value'),
               Input('Page8_MxF', 'value'),
               Input('Page8_Bt_Algo', 'n_clicks')
               ])
def display_value(es,dp,ms,mx,click):
    print('{} {} {} {} {}'.format(es,dp,ms,mx,click))
    if (click == None):
        return Page8_RF_Graphic.dum()
    elif (click <= EasyML_Page8.util.N_Click_bt2):
        return Page8_RF_Graphic.graphic()
    else:
        print('here')
        EasyML_Page8.util.N_Click_bt2 = click
        Page8_RF_Graphic.algo(es, dp, ms, mx)
        return Page8_RF_Graphic.graphic()


@EM_App.callback(Output('Page8_Estimators_l', 'children'),
              [Input('Page8_Estimators', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Estimators ={}'.format(value)


@EM_App.callback(Output('Page8_Maxdepth_l', 'children'),
              [Input('Page8_Maxdepth', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Max Depth ={}'.format(value)

@EM_App.callback(Output('Page8_Mss_l', 'children'),
              [Input('Page8_Mss', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Max Sample Split ={}'.format(value)

@EM_App.callback(Output('Page8_MxF_l', 'children'),
              [Input('Page8_MxF', 'value')])
def update_graphic(value):
    print(" Slider {}".format(value))
    return 'Max Feature ={}'.format(value)


