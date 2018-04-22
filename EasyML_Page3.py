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
from sklearn.preprocessing import StandardScaler

from EasyML_Init import EM_App

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'text2': '#000000'
}

layout = html.Div([

    html.Div([

        html.Div([
            html.H3(children='Model Analysis',
                    style={
                        'textAlign': 'center',
                        'color': colors['text2'],
                        'font-size': '40px'
                    }),
            dcc.Upload(
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
            html.Div(id='Page3_output-data-upload')
        ],
        style={
        'align':'center',
        'position':'relative',
        }
        )
    ], style={
        'width':'95%',
        'left' : '20px',
        'position':'relative',
        'background': 'white',
        'top':'20px',
    }
    ),

    ],
)

page1df = pd.DataFrame()
timeneede=0.0
itrsz=[]
timeofitr=[]
errorofitr=[]
done=''
curfilename=''
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
    global done
    global curfilename
    curfilename=filename
    dr_maker()
    done=filename
    return html.Div([

        #html.H5(filename),
        #html.H6(datetime.datetime.fromtimestamp(date)),

        # Use the DataTable prototype component:
        # github.com/plotly/dash-table-experiments
        #dt.DataTable(rows=df.to_dict('records')),

        #html.Hr(),
        html.Button('Generate', id='Page3_button',style={
            'textAlign': 'center'}),
        html.Div
        ([
            html.Div([
                html.Div([html.H6('Time VS. Dimension')],id='p3gl1',style={
            'textAlign': 'center',
            'color': colors['text2'],
            'font-size':'30px'
        })
            ]),
            dcc.Graph(id='Page3_indicator-graphic1')
        ]),
        html.Hr(),

      html.Div
        ([
            html.Div([
                html.Div([html.H6('Error VS. Dimension')],id='p3gl2',style={
            'textAlign': 'center',
            'color': colors['text2'],
            'font-size':'30px'
        })
            ]),
            dcc.Graph(id='Page3_indicator-graphic2')
        ]),

    ])


@EM_App.callback(Output('Page3_output-data-upload', 'children'),
              [Input('Page3_upload-data', 'contents'),
               Input('Page3_upload-data', 'filename'),
               Input('Page3_upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(list_of_contents, list_of_names, list_of_dates)]
        return children


def dr_maker():
    global done
    global curfilename
    if(done==curfilename):return
    features = list(page1df)
    print(features)
    features.remove('label')
    print(features)
    print('\n\n')
    x = page1df.loc[:, features].values
    y = page1df.loc[:, ['label']].values
    x = StandardScaler().fit_transform(x)
    global itrsz
    global timeofitr
    global errorofitr
    print(len(x[0]))
    itrsz=[]
    timeofitr=[]
    errorofitr=[]
    i=0
    while(i<len(x[0])+1):
        print(i)
        pca = PCA(n_components=i)
        t0= time()
        principalComponents = pca.fit_transform(x)
        t1= time()
        t1=t1-t0
        itrsz.append(i)
        timeofitr.append(t1*1000)
        pp=(pca.explained_variance_ratio_)
        err=0.0
        for j in pp:
            err=err+j
        errorofitr.append((1.0-err)*100)
        if(i<10):i=i+1
        elif(i<100):i=i+10
        elif(i<1000):i=i+100
    done=True
    return

@EM_App.callback(
    dash.dependencies.Output('Page3_indicator-graphic1', 'figure'),
    [dash.dependencies.Input('Page3_button', 'n_clicks')])
def update_graph(n_clicks):

    global itrsz
    global  timeofitr
    print(itrsz)
    print(timeofitr)
    xx = np.array(itrsz)
    yy = np.array(timeofitr)

    return {
        'data': [
            go.Scatter(
                x=xx,
                y=yy,
                text='(Dimension,Time)',
                mode='lines+markers',
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'color': 'RED',
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )],
        'layout': go.Layout(
            xaxis={
                'title': 'Dimension',
                'type': 'linear'
            },
            yaxis={
                'title': 'Time(MS)',
                'type': 'linear'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

@EM_App.callback(
    dash.dependencies.Output('Page3_indicator-graphic2', 'figure'),
    [dash.dependencies.Input('Page3_button', 'n_clicks')])
def update_graph(n_clicks):
    global itrsz
    global errorofitr
    xx = np.array(itrsz)
    yy = np.array(errorofitr)

    return {
        'data': [
            go.Scatter(
                x=xx,
                y=yy,
                text='(Dimension,Error)',
                mode='lines+markers',
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'color': 'RED',
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )],
        'layout': go.Layout(
            xaxis={
                'title': 'Dimension',
                'type': 'linear'
            },
            yaxis={
                'title': 'Error(%)',
                'type': 'linear'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }
