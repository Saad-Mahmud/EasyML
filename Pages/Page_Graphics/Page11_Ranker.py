from Pages.Page_Main import EasyML_Page11
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import copy
import dash_html_components as html
import dash_core_components as dcc
from sklearn.svm import SVC
import urllib.parse
from EasyML_Init import EM_App
import dash
from dash.dependencies import Input, Output,State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

def LRAlgo():
    maindata=copy.deepcopy(EasyML_Page11.util.maindata)
    lr = LogisticRegression(max_iter=200)
    lr = RandomForestClassifier()
    rfe = RFE(lr)
    rfe = rfe.fit(maindata.X,maindata.Y)
    print(rfe.ranking_)
    EasyML_Page11.util.RankofF=[]
    EasyML_Page11.util.RankofF=[(maindata.features[i], rfe.ranking_[i]) for i in range(maindata.N_features)]
    EasyML_Page11.util.RankofF=sorted(EasyML_Page11.util.RankofF, key=lambda rf: rf[1])
    print(EasyML_Page11.util.RankofF)
    print('done')

def RFAlgo():
    maindata=copy.deepcopy(EasyML_Page11.util.maindata)
    lr = RandomForestClassifier()
    rfe = RFE(lr)
    rfe = rfe.fit(maindata.X,maindata.Y)
    print(rfe.ranking_)
    EasyML_Page11.util.RankofF=[]
    EasyML_Page11.util.RankofF=[(maindata.features[i], rfe.ranking_[i]) for i in range(maindata.N_features)]
    EasyML_Page11.util.RankofF=sorted(EasyML_Page11.util.RankofF, key=lambda rf: rf[1])
    print(EasyML_Page11.util.RankofF)
    print('done')

def SVMAlgo():
    maindata=copy.deepcopy(EasyML_Page11.util.maindata)
    if(True):
        min_train = maindata.X.min(axis=0)
        range_train = 0.1+(maindata.X - min_train).max(axis=0)
        maindata.X = (maindata.X - min_train) / range_train

    dt = SVC(random_state=42,kernel='linear')
    rfe = RFE(dt)
    rfe = rfe.fit(maindata.X,maindata.Y)
    print(rfe.ranking_)
    EasyML_Page11.util.RankofF=[]
    EasyML_Page11.util.RankofF=[(maindata.features[i], rfe.ranking_[i]) for i in range(maindata.N_features)]
    EasyML_Page11.util.RankofF=sorted(EasyML_Page11.util.RankofF, key=lambda rf: rf[1])
    print(EasyML_Page11.util.RankofF)
    print('done')


def finalData(data):
    dff = copy.deepcopy(EasyML_Page11.util.maindata.df)
    ff=[]
    ff.append(EasyML_Page11.util.maindata.labelname)
    for i in data:
        ff.append(i)
    print(ff)
    dff=dff[ff]
    print(dff.head())
    csv_string = dff.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
    return csv_string

def finalDataR(l,r):
    dff = copy.deepcopy(EasyML_Page11.util.maindata.df)
    ff=[]
    ff.append(EasyML_Page11.util.maindata.labelname)
    for i in range(l,r+1):
        ff.append(EasyML_Page11.util.RankofF[i][0])
    print(ff)
    dff=dff[ff]
    print(dff.head())
    csv_string = dff.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
    return csv_string

def ranklist():
    ls = [{'Feature': i[0],'Rank': i[1]} for i in EasyML_Page11.util.RankofF]

    return html.Div([
        html.Div([
            html.Div([
                dt.DataTable(
                    rows=ls,
                    row_selectable=True,
                    editable=False,
                    filterable=True,
                    # sortable=True,
                    selected_row_indices=[],
                    id='Page11_table'
                ),
            ],
                className="container",
                style={
                    'position': 'relative',
                    'background': '#7386D5',
                    'width': '100%',
                    'top':'50px'
                }
            ),
            html.Div(
                [
                    html.Div(
                        id='Page11_Dlink',
                        style={
                            'position': 'relative',
                            'width': '40%',
                            'float': 'left',
                            'color': 'white',
                            'font-size': '25px',
                            'left': '20px',
                            'font-family': 'Helvetica'
                        }
                    ),
                    html.Button(
                        'Download',
                        type='submit',
                        id='Page11_Bt_Download',
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
        ),
    ])



def dum():
    html.Div([])


@EM_App.callback(
    Output('Page11_Dlink', 'children'),
    [Input('Page11_Bt_Download', 'n_clicks')],
    [State('Page11_table', 'selected_row_indices'),
     State('Page11_table', 'rows')])
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