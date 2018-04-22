import plotly.graph_objs as go
class putil():
    def __init__(self):
        self.nlcik=0
        self.graph= {
        'data': [],
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

a=putil()

