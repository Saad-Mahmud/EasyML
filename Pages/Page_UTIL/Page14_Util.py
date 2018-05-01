from DataProcessor import DataFrame
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from EasyML_Init import EM_App
from Pages.Page_Main import EasyML_Page14
from Pages.Page_Graphics import Page14_Table

class putil():

    def page_contents(self):
        if (self.isNone==True):
            return html.Div()
        df2=self.maindata.df[:5]
        return html.Div([

            html.Div(
                [html.H5(self.maindata.filename + '(First 5 row)'),
                dt.DataTable(rows=df2.to_dict('records'),
                             editable=False)],
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
                        id='Page14_Dd_Label',
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
                        id='Page14_Bt_Label',
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
            html.Div(id='Page14_Algo',style={'background':'white','top':'25px'}),


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
            self.tab1=html.Div([])
            self.tab2=html.Div([])

        return

    def Page14_Algo_Maker(self,name):
        print('here2 {}'.format(self.isNone))
        if(self.isNone==True):
            return html.Div([])
        self.maindata.make_XY(name)
        Page14_Table.createTable()
        return html.Div([
        dcc.Tabs(
            tabs=[
                {'label': 'Variance Table', 'value': 1},
                {'label': 'Variance Distribution', 'value': 2},
            ],
            value=1,
            id='Page14_Tabs',
            vertical=False
        ),
        html.Div(id='Page14_Tabs_output')
    ], style={
        'width': '100%',
        'fontFamily': 'Sans-Serif',
        'margin-left': 'auto',
        'margin-right': 'auto'
    })


@EM_App.callback(Output('Page14_Algo', 'children'),
                 [dash.dependencies.Input('Page14_Dd_Label', 'value'),
                    dash.dependencies.Input('Page14_Bt_Label', 'n_clicks')])
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
    elif (click <= EasyML_Page14.util.N_Click_bt1):
        return html.Div([])
    else:
        EasyML_Page14.util.N_Click_bt1=click
        print('here')
        return EasyML_Page14.util.Page14_Algo_Maker(name)




@EM_App.callback(Output('Page14_Tabs_output', 'children'), [Input('Page14_Tabs', 'value')])
def display_content(value):
    if(value==1):return EasyML_Page14.util.tab1
    else: return EasyML_Page14.util.tab2