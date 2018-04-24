from DataProcessor import DataFrame
from dash.dependencies import Input, Output,State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from EasyML_Init import EM_App
from Pages.Page_Main import EasyML_Page2 as EP
from Pages.Page_Graphics import Page2_Tabs_Layout as P2TL


class putil():

    def page_contents(self):
         return html.Div(
             [
                 html.Div
                ([
                    html.H4(EP.util.maindata.filename),
                    dt.DataTable(
                        rows=EP.util.maindata.df.to_dict('records'),
                        # optional - sets the order of columns
                        columns=sorted(EP.util.maindata.df.columns),
                        row_selectable=True,
                        filterable=True,
                        #sortable=True,
                        selected_row_indices=[],
                        id='Page2_table'
                     ),
                ],
                className="container",
                style={
                    'position': 'relative',
                    'border': '1px',
                    'top': '15px',
                    'width':'95%'
                    }
                ),
                html.Div
                (
                  [
                      html.Div(
                          [
                              html.Button(
                                  'Delete Selected Row(s)',
                                  type='submit',
                                  id='Page2_Bt_Delrows',
                                  style={
                                      'position': 'relative',
                                      'width': '40%',

                                      'background-color': '#7386D5',
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
                              'background': 'ghostwhite',
                          }

                      ),
                      html.Div(
                          [
                              dcc.Dropdown(
                                  options=[
                                      {'label': i, 'value': i}for i in EP.util.maindata.available_indicators
                                  ],
                                  multi=True,
                                  value=None,
                                  id='Page2_Delcols',
                              ),
                              html.Button(
                                  'Delete Selected Column(s)',
                                  type='submit',
                                  id='Page2_Bt_Delcols',
                                  style={
                                      'position': 'relative',
                                      'width': '40%',

                                      'background-color': '#7386D5',
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
                              'background': 'ghostwhite',
                          }
                      ),
                      html.Div(
                          [
                              html.H6('I want to:')
                          ],
                          style={
                              'display': 'inline-block',
                              'position': 'relative',
                              'width': '100%',
                              'top': '100px',
                              'background': 'ghostwhite',
                          }
                      ),
                      html.Div(
                          [
                              dcc.Dropdown(
                                  options=[
                                      {'label': 'See Corelation', 'value': 0},
                                      {'label': 'See Distribution', 'value': 1},
                                      {'label': 'Download data', 'value': 2}
                                  ],
                                  value=None,
                                  id='Page2_Tabs'
                              ),
                          ],
                          style={
                              'display': 'inline-block',
                              'position': 'relative',
                              'width': '100%',
                              'top': '100px',
                              'background': 'ghostwhite',
                          }
                      ),
                      html.Div(
                          id='Page2_GT_output',
                          style={
                              'display': 'inline-block',
                              'position': 'relative',
                              'width': '100%',
                              'top': '100px',
                              'background': 'ghostwhite',
                          }

                      ),

                  ]
                )
            ],
             style={
                 'position': 'relative',
                 'align': 'center'
             }
         )

    def __init__(self,contents=None, names=None, dates=None):
        if(names==None):
            self.isNone=True
        else:

            print("{} {} {}".format(names, dates, contents))
            self.isNone = False
            self.maindata=DataFrame.dtf(contents, names, dates)
            self.Bt_Tab2 = 0
            self.Bt_Delrows = 0
            self.Bt_Delcols = 0
            self.Bt_Tab2_name=''
            self.Bt_Tab1_X = ''
            self.Bt_Tab1_Y = ''
            self.Bt_Tab1_T = ''
            self.Bt_Tab1 = 0
            self.Bt_Tab3 = 0
        return




@EM_App.callback(
    Output('Page2_GT_output', 'children'),
    [Input('Page2_Tabs', 'value')])
def page2_tabsfun(value):
    if(value==0):
        return P2TL.maketab1()
    elif(value==1):
        return P2TL.maketab2()
    elif(value==2):
        return P2TL.maketab3()
    else:
        return html.Div()
@EM_App.callback(
    Output('Page2_table', 'rows'),
    [Input('Page2_Bt_Delrows', 'n_clicks')],
    [State('Page2_table', 'selected_row_indices')])
def Page2_delrowfun(clk,delin):
    if(clk==None):return EP.util.maindata.df.to_dict('records')
    if(clk<=EP.util.Bt_Delrows):return EP.util.maindata.df.to_dict('records')
    else:
        EP.util.Bt_Delrows=clk
        EP.util.maindata.df=EP.util.maindata.df.drop(EP.util.maindata.df.index[delin])
        return EP.util.maindata.df.to_dict('records')

@EM_App.callback(
    Output('Page2_table', 'columns'),
    [Input('Page2_Bt_Delcols', 'n_clicks'),
     Input('Page2_Delcols', 'value')],
    [State('Page2_table', 'columns')])
def Page2_delrowfun(clk,delin,colmns):
    if(clk==None):return colmns
    if(clk<=EP.util.Bt_Delcols):return colmns
    if(delin==None):return colmns
    EP.util.Bt_Delcols=clk
    print('here')
    print(delin)
    print()
    dell=[]
    for i in delin:
        colmns.remove(i)
        try:
            EP.util.maindata.available_indicators.remove(i)
            dell.append(i)
        except:
            print('error del')
    print('her to del')
    print(dell)
    EP.util.maindata.df=EP.util.maindata.df.drop(dell,axis=1)
    print(EP.util.maindata.df.head())
    return colmns
@EM_App.callback(
    Output('Page2_Delcols', 'options'),
    [Input('Page2_Bt_Delcols', 'n_clicks'),
     Input('Page2_Delcols', 'value')],
     [State('Page2_table', 'columns')])
def Page2_dDDD(clk,VV,colmns):
    return [
        {'label': i, 'value': i} for i in colmns
    ]
@EM_App.callback(
    Output('Page2_Tabs', 'value'),
    [Input('Page2_Bt_Delcols', 'n_clicks')])
def Page2_dDDD(clk):
    return None
