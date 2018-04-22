import base64
import datetime
import io
from time import time
import dash
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
from EasyML_Init import EM_App
from Pages import Page1_Util



colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'text2': '#000000'
}

layout=html.Div([
    html.Div([

        html.Div([
            html.H3
                (
                    children='Dimensionality Reduction',
                    style={
                        'textAlign': 'center',
                        'color': 'white',
                        'font-size': '40px',
                        'background':'#6d7fcc'
                    }
                ),
            dcc.Upload
                (
                    id='Page1_upload-data',
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
            html.Div(id='Page1_output-data-upload'),
            dcc.Interval(
                id='Page1_interval-component',
                interval=1*1000, # in milliseconds
                n_intervals=0
            )

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
page1df = pd.DataFrame()
timeneede=0.0
def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    available_indicators = list(df)
    global page1df
    page1df = df
    global timeneede
    df2=df[:5]
    return html.Div([

        html.Div([
            html.H4(filename),
            dt.DataTable(rows=df2.to_dict('records'))],
            style={
                'position': 'relative',
                'border': '1px',
                'top': '15px',
                'width': '100%'
            }
        ),

        html.Hr(),

        html.Div
            ([

            html.Div([

                html.Div([
                    html.H6('Select Algorithm'),
                    dcc.Dropdown(
                        id='Page1_algorithm',
                        options=[{'label': i, 'value': i} for i in ['PCA','Linear Embading','Isomap'
                                                                    ,'TSNE','MDS','SpectralEmbedding'
                                                                    ]],
                        value=''
                    )
                ],style={
                        'display': 'inline-block',
                        'position': 'relative',
                        'width': '100%',
                        'top': '50px',
                    }),

                html.Div([
                    html.H6('Select Tag'),
                    dcc.Dropdown(
                        id='Page1_marker_text',
                        options=[{'label': i, 'value': i} for i in available_indicators],
                        value=''
                    )
                ],style={
                        'display': 'inline-block',
                        'position': 'relative',
                        'width': '100%',
                        'top': '50px',
                    }),
                html.Div([
                    html.H6("Algorithm Run Time: {}".format(timeneede)),
                ],id='Page1_runtime',style={
                        'display': 'inline-block',
                        'position': 'relative',
                        'width': '100%',
                        'top': '50px',
                    }),

                html.Div([
                    html.Button(
                        'Apply',
                        type='submit',
                        id='Page1_Bt_Apply',
                        style={
                            'position': 'relative',
                            'width': '100%',

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
                    }
                ),

            ],
            style={'width': '20%', 'display': 'inline-block'}),
            dcc.Graph(id='Page1_indicator-graphic',
                      style={'width': '75%',
                             'float': 'right',
                             'display': 'inline-block',
                             'border':'1px solid black'
                             }),

        ]),

        # horizontal line
        # For debugging, display the raw contents provided by the web browser
    ])


@EM_App.callback(Output('Page1_output-data-upload', 'children'),
              [Input('Page1_upload-data', 'contents'),
               Input('Page1_upload-data', 'filename'),
               Input('Page1_upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(list_of_contents, list_of_names, list_of_dates)]
        return children


def dr_maker(algo):
    features = list(page1df)
    features.remove('label')
    #print(features)
    #print('\n\n')
    x = page1df.loc[:, features].values
    y = page1df.loc[:, ['label']].values
    x = StandardScaler().fit_transform(x)
    #print(x)
    #print('\n\n')
    #print(y)
    #print('\n\n')

    pca = LocallyLinearEmbedding(n_components=2)
    if algo=='PCA':
        pca = PCA(n_components=2)
    elif algo=='Linear Embading':
        pca = LocallyLinearEmbedding(n_components=2)
    elif algo== 'Isomap':
        pca = Isomap(n_components=2)
    elif algo== 'MDS':
        pca = MDS(n_components=2)
    elif algo== 'SpectralEmbedding':
        pca = SE(n_components=2)
    else:
        pca = TSNE(n_components=2)

    t0= time()
    principalComponents = pca.fit_transform(x)
    t1= time()
    principalDf = pd.DataFrame(data=principalComponents
                               , columns=['principal component 1', 'principal component 2'])
    #print(principalDf.head(5))
    #print('\n\n')
    t1=t1-t0
    global timeneede
    timeneede=t1
    print(algo)
    print(t1)
    finalDf = pd.concat([principalDf, page1df[['label']]], axis=1)
    #print(finalDf.head(5))
    #print('\n\n')
    return finalDf

@EM_App.callback(
    dash.dependencies.Output('Page1_indicator-graphic', 'figure'),
    [dash.dependencies.Input('Page1_algorithm', 'value'),
     dash.dependencies.Input('Page1_marker_text', 'value'),
     dash.dependencies.Input('Page1_Bt_Apply', 'n_clicks')])
def update_graph(algo_name, text_type,clk):

    if(algo_name == None): return Page1_Util.a.graph
    if (text_type == None): return Page1_Util.a.graph
    if(clk==None):return Page1_Util.a.graph
    if(clk<=Page1_Util.a.nlcik): return Page1_Util.a.graph

    print(clk)
    Page1_Util.a.nlcik=clk
    df =dr_maker(algo_name)
    xx = np.array(df['principal component 1'])
    yy = np.array(df['principal component 2'])
    textt = np.array(df[text_type])
    unitag=np.unique(textt)
    tag_map = {}
    for i in range(len(unitag)):
        tag_map[unitag[i]] = i
    diflistx=[]
    diflisty = []
    diflistt = []

    colo=['#bcbd22','#7f7f7f','#e377c2','#1f77b4','#ff7f0e','#2ca02c','#d62728','#17becf','#9467bd','#8c564b']
    for i in range(len(unitag)):
        tmpx=[]
        tmpy = []
        tmpt = []
        for j in range(len(xx)):
            if textt[j]==unitag[i]:
                tmpx.append(xx[j])
                tmpy.append(yy[j])
                tmpt.append(textt[j])
        diflistt.append(tmpt)
        diflistx.append(tmpx)
        diflisty.append(tmpy)

    tracelist=[]

    Page1_Util.a.graph= {
        'data': [
            go.Scatter(
                x=diflistx[i],
                y=diflisty[i],
                text=diflistt[i],
                mode='markers',
                name=unitag[i],
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'color': colo[i],
                    'line': {'width': 0.5, 'color': 'white'}
                }
            ) for i in range(len(unitag))],
        'layout': go.Layout(
            xaxis={
                'title': 'Component 1',
                'type': 'linear'
            },
            yaxis={
                'title': 'Component 2',
                'type': 'linear'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }
    return Page1_Util.a.graph


@EM_App.callback(Output('Page1_runtime', 'children'),
              [Input('Page1_interval-component', 'n_intervals')])
def update_metrics1(n):
    return html.H6("Algorithm Run Time: {}".format(timeneede))