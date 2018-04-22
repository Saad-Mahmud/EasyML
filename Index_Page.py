from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import base64
import datetime
import io
from EasyML_Init import EM_App
from flask import Flask

layout = html.Div([

    html.Div([
        html.A(children='Dimension Reduction 2D', href='/test/page1',
            style={
            'text-align': 'center',
            'font-size':'20px',
            'color': 'black',
            'font-family': 'Consolas'
        })],
        style={
        'left' : '35%',
        'position':'relative',
        }
    ),
    html.Div([
        html.A(children='Quick View', href='/test/page2',
            style={
            'text-align': 'center',
            'font-size':'20px',
            'color': 'black',
            'font-family': 'Consolas'
        })],
        style={
        'top': '5px',
        'left' : '35%',
        'position':'relative',
        }
    ),
    html.Div([
        html.A(children='PCA Analysis', href='/test/page3',
            style={
            'text-align': 'center',
            'font-size':'20px',
            'color': 'black',
            'font-family': 'Consolas'
        })],
        style={
        'top': '10px',
        'left' : '35%',
        'position':'relative',
        }
    ),
    html.Div([
        html.A(children='Dimension Reduction 3D', href='/test/page4',
            style={
            'text-align': 'center',
            'font-size':'20px',
            'color': 'black',
            'font-family': 'Consolas'
        })],
        style={
        'top': '10px',
        'left' : '35%',
        'position':'relative',
        }
    ),
    html.Div([
        html.A(children='K Neighbors Classifier Analysis', href='/test/page5',
            style={
            'text-align': 'center',
            'font-size':'20px',
            'color': 'black',
            'font-family': 'Consolas'
        })],
        style={
        'top': '10px',
        'left' : '35%',
        'position':'relative',
        }
    ),
    html.Div([
        html.A(children='Logistic Regression Classifier Analysis', href='/test/page6',
            style={
            'text-align': 'center',
            'font-size':'20px',
            'color': 'black',
            'font-family': 'Consolas'
        })],
        style={
        'top': '10px',
        'left' : '35%',
        'position':'relative',
        }
    ),
    html.Div([
        html.A(children='Decision Tree Classifier Analysis', href='/test/page7',
            style={
            'text-align': 'center',
            'font-size':'20px',
            'color': 'black',
            'font-family': 'Consolas'
        })],
        style={
        'top': '10px',
        'left' : '35%',
        'position':'relative',
        }
    ),
    html.Div([
        html.A(children='Random Forest Classifier Analysis', href='/test/page8',
            style={
            'text-align': 'center',
            'font-size':'20px',
            'color': 'black',
            'font-family': 'Consolas'
        })],
        style={
        'top': '10px',
        'left' : '35%',
        'position':'relative',
        }
    ),
    html.Div([
        html.A(children='3-layered Perceptron Classifier Analysis', href='/test/page9',
            style={
            'text-align': 'center',
            'font-size':'20px',
            'color': 'black',
            'font-family': 'Consolas'
        })],
        style={
        'top': '10px',
        'left' : '35%',
        'position':'relative',
        }
    ),
    html.Div([
        html.A(children='SVM Classifier Analysis', href='/test/page10',
            style={
            'text-align': 'center',
            'font-size':'20px',
            'color': 'black',
            'font-family': 'Consolas'
        })],
        style={
        'top': '10px',
        'left' : '35%',
        'position':'relative',
        }
    ),
    html.Div([
        html.A(children='Recursive Feature Elimination(Feature Selection)', href='/test/page11',
            style={
            'text-align': 'center',
            'font-size':'20px',
            'color': 'black',
            'font-family': 'Consolas'
        })],
        style={
        'top': '10px',
        'left' : '35%',
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
)
