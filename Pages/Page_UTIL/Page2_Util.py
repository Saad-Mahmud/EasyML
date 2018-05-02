from DataProcessor import DataFrame
from dash.dependencies import Input, Output,State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from EasyML_Init import EM_App
from Pages.Page_Main import EasyML_Page2 as EP
from Pages.Page_Graphics import Page2_Tabs_Layout as P2TL
from sklearn import preprocessing


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
                        row_selectable=False,
                        filterable=True,
                        editable=False,
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
                 html.Div(
                     [
                         html.Div([dcc.Dropdown(
                             options=[
                                 {'label': i, 'value': i} for i in EP.util.maindata.available_indicators
                             ],
                             multi=True,
                             value=None,
                             id='Page2_Labelcols',
                         )],style={
                                 'position': 'relative',
                                 'width': '40%',
                                 'float': 'left',
                                }),
                         html.Button(
                             'Encode to Integer',
                             type='submit',
                             id='Page2_Bt_Labelcols',
                             style={
                                 'position': 'relative',
                                 'width': '40%',
                                 'background-color': '#7386D5',
                                 'border': '1px',
                                 'float': 'right',
                                 'color': 'white',
                                 'font-size': '15px',
                                 'font-family': 'Helvetica'
                             }),
                     ],style={
                              'display': 'inline-block',
                              'position': 'relative',
                              'width': '100%',
                              'top': '50px',
                              'background': 'ghostwhite',
                          }),
                html.Div
                (
                  [
                      html.Div(
                          [
                              html.Button(
                                  'Delete Row With Null Value',
                                  type='submit',
                                  id='Page2_Bt_Delrows',
                                  style={
                                      'position': 'relative',
                                      'width': '40%',
                                      'background-color': '#7386D5',
                                      'border': '1px',
                                      'float': 'right',
                                      'color': 'white',
                                      'top': '5px',
                                      'font-size': '15px',
                                      'font-family': 'Helvetica'
                                  }),
                              html.Button(
                                  'Replace Null with Zero',
                                  type='submit',
                                  id='Page2_Bt_Fillrows',
                                  style={
                                      'position': 'relative',
                                      'width': '40%',
                                      'background-color': '#7386D5',
                                      'border': '1px',
                                      'float': 'left',
                                      'color': 'white',
                                      'top': '5px',
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
                                      'float': 'right',
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
                      html.Div([
                          dcc.Tabs(
                              tabs=[
                                      {'label': 'See Corelation', 'value': 0},
                                      {'label': 'See Distribution', 'value': 1},
                                      {'label': 'Download data', 'value': 2}
                              ],
                              value=None,
                              id='Page2_Tabs',
                              vertical=False
                          ),
                          html.Div(
                              id='Page2_GT_output',
                              style={
                                  'display': 'inline-block',
                                  'position': 'relative',
                                  'width': '100%',
                                  'background': 'ghostwhite',
                              }

                          ),
                      ], style={
                          'display': 'inline-block',
                          'position': 'relative',
                          'width': '100%',
                          'top': '100px',
                          'background': 'ghostwhite',
                          'fontFamily': 'Sans-Serif',
                          'margin-left': 'auto',
                          'margin-right': 'auto'
                      }),
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
            self.Bt_Fillrows = 0
            self.Bt_Delcols = 0
            self.Bt_Labelcols = 0
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
    [Input('Page2_Bt_Delrows', 'n_clicks'),
     Input('Page2_Bt_Fillrows', 'n_clicks'),
     Input('Page2_Bt_Labelcols', 'n_clicks'),
     Input('Page2_Labelcols', 'value')])
def Page2_delrowfun(clk1,clk2,clk3,val):
    if(clk1==None):clk1=0
    if(clk2 == None): clk2 = 0
    if (clk3 == None): clk3 = 0
    if(clk1<=EP.util.Bt_Delrows and clk2<=EP.util.Bt_Fillrows and clk3<=EP.util.Bt_Labelcols):
        return EP.util.maindata.df.to_dict('records')
    elif (clk1>EP.util.Bt_Delrows):
        EP.util.Bt_Delrows=clk1
        EP.util.maindata.df=EP.util.maindata.df.dropna(axis=0, how='any')
        return EP.util.maindata.df.to_dict('records')
    elif (clk2>EP.util.Bt_Fillrows):
        EP.util.Bt_Fillrows=clk2
        EP.util.maindata.df=EP.util.maindata.df.fillna(0)
        return EP.util.maindata.df.to_dict('records')
    elif(clk3>EP.util.Bt_Labelcols and val !=None):
        EP.util.Bt_Labelcols = clk3
        le = preprocessing.LabelEncoder()
        le.fit(EP.util.maindata.df[val])
        EP.util.maindata.df[val] = le.transform(EP.util.maindata.df[val])
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
