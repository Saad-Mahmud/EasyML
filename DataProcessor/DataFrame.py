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
import copy

class dtf():

    def make_XY(self,name):
        print("Make_xy = {}".format(name))
        self.features = copy.deepcopy(self.available_indicators)
        self.features.remove(name)
        print("Make_xy = {}".format(self.features))
        self.labelname=name
        self.N_features=len(self.features)
        self.X = copy.deepcopy(self.df.loc[:, self.features].values)
        self.Y = copy.deepcopy(np.array(self.df[name]))
        self.unique_Y=np.unique(self.Y)
        print(self.N_features)
        print(self.unique_Y)
        print(self.X[:5])
        print(self.Y[:5])


    def parse_contents(self):
        content_type, content_string = self.contents.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in self.filename:
                # Assume that the user uploaded a CSV file
                self.df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in self.filename:
                # Assume that the user uploaded an excel file
                self.df = pd.read_excel(io.BytesIO(decoded))
        except Exception as e:
            print(e)

        self.available_indicators = list(self.df)


    def __init__(self,contents, filename, date):
        self.contents=contents
        self.filename=filename
        self.date=date
        self.parse_contents()
