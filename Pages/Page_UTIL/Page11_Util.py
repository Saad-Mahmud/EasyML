from DataProcessor import dtf
import dash
from dash.dependencies import Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from EasyML_Init import EM_App
from Pages import EasyML_Page11
from Pages.Page_Graphics import Page11_AlgoDash


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
                    html.P(children='Select Model: ',
                            style={
                                'position':'relative',
                                'font-size':'23px',
                                'border':'1px solid black',
                                'float':'left',
                            }),
                    html.Div(
                        [dcc.Dropdown(
                        id='Page11_Dd_Model',
                        options=[{'label': 'Logistic Classifier', 'value': 'LR'},
                                 {'label': 'SVM', 'value': 'SVM'}],
                        value='SVM',)],
                        style={
                            'position': 'relative',
                            'width': '20%',
                            'left': '3%',
                            'border': '1px solid black',
                            'float': 'left',
                        }),
                    html.P(children='Select Label: ',
                           style={
                               'position': 'relative',
                               'font-size': '23px',
                               'border': '1px solid black',
                               'float': 'left',
                               'left':'6%'
                           }),
                    html.Div(
                        [dcc.Dropdown(
                            id='Page11_Dd_Label',
                            options=[{'label': i, 'value': i} for i in self.maindata.available_indicators],
                            value=None, )],
                        style={
                            'position': 'relative',
                            'width': '20%',
                            'left': '9%',
                            'border': '1px solid black',
                            'float': 'left',
                        }),
                    html.Button(
                        'Apply',
                        id='Page11_Bt_Model',
                        style={
                            'position': 'relative',
                            'width': '20%',
                            'left': '12%',
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
            ),
            html.Div(id='Page11_Algo',style=
            {
             'position':'relative',
              'top':'25px'
             }),


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
            self.N_Click_LR = 0
            self.N_Click_SVM = 0
            self.N_Click_DT = 0
            self.N_Click_RF = 0
            self.N_Click_DL1 = 0
            self.N_Click_DL2 = 0
            self.RankofF=[]
        return

    def Page11_Algo_Maker(self,name):
        print('here2 {}'.format(self.isNone))
        if(self.isNone==True):
            return html.Div([])
        self.maindata.make_XY(name)





@EM_App.callback(Output('Page11_Algo', 'children'),
                 [dash.dependencies.Input('Page11_Dd_Model', 'value'),
                    dash.dependencies.Input('Page11_Dd_Label', 'value'),
                    dash.dependencies.Input('Page11_Bt_Model', 'n_clicks')])
def update_ui(name,lab,click):
    print("Debug: {} {} & {}".format(lab,name,click))
    if(name==None):
        if (click != None): EasyML_Page11.util.N_Click_bt1 = click
        return [html.P("---------------- Select a Model---------------",
                       style={
            'font-size': '15px',
            'color': 'red'
        })]
    elif(lab==None):
        if(click!=None):EasyML_Page11.util.N_Click_bt1 = click
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
    elif (click<=EasyML_Page11.util.N_Click_bt1):
        return html.Div([])
    else:
        EasyML_Page11.util.N_Click_bt1=click
        EasyML_Page11.util.Page11_Algo_Maker(lab)
        if(name=='SVM'):return Page11_AlgoDash.SVMDash()
        else: return Page11_AlgoDash.LRDash()


