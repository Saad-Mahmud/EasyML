import base64
import datetime
import io
from time import time
import dash
import urllib.parse
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.manifold import Isomap
from sklearn.manifold import LocallyLinearEmbedding
from sklearn.manifold import MDS
from sklearn.manifold import SpectralEmbedding as SE
from sklearn.preprocessing import StandardScaler
from Pages.Page_UTIL import Page3_Util
from EasyML_Init import EM_App

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'text2': '#000000'
}

layout = html.Div([

    html.Div([

        #Title
        html.Div([
            html.H3
                (
                    children='Reduce Dimension of DataSet',
                    style={
                        'textAlign': 'center',
                        'color': 'white',
                        'font-size': '40px',
                        'background':'#6d7fcc'
                    }
                ),
            #Page CSV
            dcc.Upload
                (
                    id='Page3_upload-data',
                    children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select File')
                ]),
                style={
                    'width': '60%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'position':'relative',
                    'left':'20%'
                },
                # Allow multiple files to be uploaded
                multiple=False
            ),
            #Page Main Layout
            html.Div(id='Page3_output-data-upload'),

        ],
        style={
            'align':'center',
            'position':'relative',
            }
        )],
        style={
        'width':'95%',
        'left' : '20px',
        'position':'relative',
        'background': 'white',
        'top':'20px',
    }),
])


def parse_contents(contents, filename, date):
    Page3_Util.a.__init__()
    Page3_Util.a.addData(contents, filename, date)
    df2 = Page3_Util.a.maindata.df[:5]
    return html.Div([

        html.Div(
            [html.H5(filename + '(First 5 row)'),
             dt.DataTable(rows=df2.to_dict('records'))],
            style={
                'position': 'relative',
                'border': '1px',
                'top': '15px'
            }
        ),

        html.Div(
            [
                html.P(children='Label: ',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px',
                           'float': 'left',
                           'font-family': 'Helvetica'
                       }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page3_Dd_Label',
                        options=[{'label': i, 'value': i} for i in Page3_Util.a.maindata.available_indicators],
                        value=None, )],
                    style={
                        'position': 'relative',
                        'width': '20%',
                        'left': '10px',
                        'border': '1px',
                        'float': 'left',
                        'top': '3px'
                    }),
                html.P(children='Algo: ',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px',
                           'float': 'left',
                           'left': '40px',
                           'font-family': 'Helvetica'
                       }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page3_Dd_Algo',
                        options=[{'label': i, 'value': i} for i in ['PCA', 'Linear Embading', 'Isomap'
                            , 'TSNE', 'MDS', 'SpectralEmbedding'
                                                                    ]],
                        value=None, )],
                    style={
                        'position': 'relative',
                        'width': '20%',
                        'left': '50px',
                        'border': '1px',
                        'float': 'left',
                        'top': '3px'
                    }),
                html.Div(
                    [dcc.Dropdown(
                        id='Page3_Dd_Dimension',
                        options=[{'label': i + 1, 'value': i + 1} for i in
                                 range(len(Page3_Util.a.maindata.available_indicators) - 1)],
                        value=None, )],
                    style={
                        'position': 'relative',
                        'width': '20%',
                        'right': '5px',
                        'border': '1px',
                        'float': 'right',
                        'top': '3px'
                    }),
                html.P(children='Dimension: ',
                       style={
                           'position': 'relative',
                           'font-size': '23px',
                           'border': '1px',
                           'float': 'right',
                           'right': '15px',
                           'font-family': 'Helvetica'
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
                    'Download',
                    id='Page3_Bt_Apply',
                    style={
                        'position': 'relative',
                        'background-color': '#7386D5',
                        'width': '40%',
                        'right': '5px',
                        'border': '1px',
                        'float': 'right',
                        'color': 'white',
                        'font-size': '15px',
                        'font-family': 'Helvetica'
                    }),
                html.Div(id='Page3_Dlink')
            ],
            style={
                'display': 'inline-block',
                'position': 'relative',
                'width': '100%',
                'top': '50px',
                'background': 'ghostwhite'
            }
        ),
    ])

'''Gen Data'''

@EM_App.callback(Output('Page3_output-data-upload', 'children'),
              [Input('Page3_upload-data', 'contents'),
               Input('Page3_upload-data', 'filename'),
               Input('Page3_upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(list_of_contents, list_of_names, list_of_dates)]
        return children


def finalData(algo,lb,dm):

    Page3_Util.a.maindata.make_XY(lb)
    pca = LocallyLinearEmbedding(n_components=dm)
    if algo=='PCA':
        pca = PCA(n_components=dm)
    elif algo=='Linear Embading':
        pca = LocallyLinearEmbedding(n_components=dm)
    elif algo== 'Isomap':
        pca = Isomap(n_components=dm)
    elif algo== 'MDS':
        pca = MDS(n_components=dm)
    elif algo== 'SpectralEmbedding':
        pca = SE(n_components=dm)
    else:
        if dm==Page3_Util.a.maindata.N_features:dm=dm-1
        pca = TSNE(n_components=dm)

    principalComponents = pca.fit_transform(Page3_Util.a.maindata.X)
    principalDf = pd.DataFrame(data=principalComponents
                               , columns=["D{}".format(i) for i in range(dm)])
    finalDf = pd.concat([principalDf, Page3_Util.a.maindata.df[[lb]]], axis=1)
    csv_string = finalDf.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
    return csv_string


#Graph
@EM_App.callback(
    dash.dependencies.Output('Page3_Dlink', 'children'),
    [dash.dependencies.Input('Page3_Dd_Algo', 'value'),
    dash.dependencies.Input('Page3_Dd_Label', 'value'),
     dash.dependencies.Input('Page3_Dd_Dimension', 'value'),
     dash.dependencies.Input('Page3_Bt_Apply', 'n_clicks')])
def update_graph(algo,lb,dm,clk):
    #init Button
    if(algo== None): return html.Div([])
    if (lb == None): return html.Div([])
    if (dm == None): return html.Div([])
    if(clk==None):return html.Div([])
    if(clk<= Page3_Util.a.nlcik): return html.Div([])
    Page3_Util.a.nlcik=clk
    return [html.A(
        "Download Data({})".format(clk),
        id='download-link14',
        download="rawdata.csv",
        href=finalData(algo,lb,dm),
        target="_blank"
    )]



