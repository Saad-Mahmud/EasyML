from DataProcessor import dtf
import Page5_Util as putil
import base64
import datetime
import io
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from EasyML_Init import EM_App

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'text2': '#000000'
}

util=putil.putil()

layout = html.Div([
    html.Div([

        html.Div([
            html.H3
                (
                    children='K Nearest Neighbors Classifier',
                    style={
                        'textAlign': 'center',
                        'color': 'white',
                        'font-size': '40px',
                        'background':'#6d7fcc'
                    }
                ),
            dcc.Upload
                (
                    id='Page5_upload-data',
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
            html.Div(id='Page5_output-data-upload')
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

@EM_App.callback(Output('Page5_output-data-upload', 'children'),
              [Input('Page5_upload-data', 'contents'),
               Input('Page5_upload-data', 'filename'),
               Input('Page5_upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        global util
        util=putil.putil(list_of_contents, list_of_names, list_of_dates)
        children = [util.page_contents()]
        return children
    else:
        print('Problem on page 5')
