from Pages.Page_Main import EasyML_Page14
from sklearn.feature_selection import VarianceThreshold
import copy
import dash_html_components as html
import dash_core_components as dcc
import urllib.parse
from dash.dependencies import Input, Output,State
from EasyML_Init import EM_App
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import plotly.graph_objs as go

def createTable():
    selector = VarianceThreshold()
    selector.fit(EasyML_Page14.util.maindata.X)
    print(EasyML_Page14.util.maindata.X)
    print(selector.variances_)
    ls=[{'Feature':EasyML_Page14.util.maindata.features[i],
         'Variance':selector.variances_[i]} for i in range(EasyML_Page14.util.maindata.N_features)
        ]
    print(ls)
    EasyML_Page14.util.tab1= html.Div([
            html.Div([
                 dt.DataTable(
                     rows=ls,
                     row_selectable=True,
                     editable=False,
                     filterable=True,
                     # sortable=True,
                     selected_row_indices=[],
                     id='Page14_table'
                 ),
             ],
             className="container",
                style={
                    'position': 'relative',
                    'background': '#7386D5',
                    'width': '100%',
                }
            ),
            html.Div(
                [
                    html.Div(
                    id='Page14_Dlink',
                        style={
                            'position': 'relative',
                            'width': '40%',
                            'float': 'left',
                            'color': 'white',
                            'font-size': '25px',
                            'left':'20px',
                            'font-family': 'Helvetica'
                        }
                    ),
                    html.Button(
                        'Download',
                        type='submit',
                        id='Page14_Bt_Download',
                        style={
                            'position': 'relative',
                            'width': '20%',
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
        ],
    )
    data = [go.Histogram(y=selector.variances_)]
    layout = go.Layout(
        title='Varinace',
        xaxis=dict(
            title='Count'
        ),
        yaxis=dict(
            title='Variance'
        ),
        bargap=0.2,
        bargroupgap=0.1
    )
    fig = go.Figure(data=data, layout=layout)
    EasyML_Page14.util.tab2= html.Div([
                dcc.Graph(
                    id='Page14_Dis_Graph',
                    figure=fig
                )
    ])


def finalData(ls):
    dff = copy.deepcopy(EasyML_Page14.util.maindata.df)
    ff = []
    ff.append(EasyML_Page14.util.maindata.labelname)
    for i in ls:
        ff.append(i)
    print(ff)
    dff = dff[ff]
    print(dff.head())
    csv_string = dff.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
    return csv_string

@EM_App.callback(
    Output('Page14_Dlink', 'children'),
    [Input('Page14_Bt_Download', 'n_clicks')],
    [State('Page14_table', 'selected_row_indices'),
     State('Page14_table', 'rows')])
def Page2_delrowfun(clk,delin,rows):
    print(delin)
    print(rows)
    ls=[]
    for i in delin:
        ls.append(rows[i]['Feature'])
    if(clk==None):return [html.A()]
    return  [html.A(
            "Download Data({})".format(clk),
            id='download-link14',
            download="rawdata.csv",
            href=finalData(ls),
            target="_blank"
        )]