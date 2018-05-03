import plotly.graph_objs as go
from DataProcessor import DataFrame
class putil():
    def addData(self,contents, filename, date):
        self.maindata=DataFrame.dtf(contents, filename, date)
    def __init__(self):
        self.nlcik=0
        self.maindata=None

a=putil()

