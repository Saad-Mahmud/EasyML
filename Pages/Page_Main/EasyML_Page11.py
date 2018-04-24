from Pages.Page_UTIL import Page11_Util as putil
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
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
                    children='Recursive Feature Elimination',
                    style={
                        'textAlign': 'center',
                        'color': colors['text2'],
                        'font-size': '40px'
                    }
                ),
            dcc.Upload
                (
                    id='Page11_upload-data',
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
            html.Div(id='Page11_output-data-upload')
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

@EM_App.callback(Output('Page11_output-data-upload', 'children'),
              [Input('Page11_upload-data', 'contents'),
               Input('Page11_upload-data', 'filename'),
               Input('Page11_upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        global util
        util=putil.putil(list_of_contents, list_of_names, list_of_dates)
        children = [util.page_contents()]
        return children
    else:
        print('Problem on page 11')
