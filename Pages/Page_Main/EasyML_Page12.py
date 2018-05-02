import base64
import io
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from dash.dependencies import Input, Output
import pandas as pd
import copy
from Pages.Page_UTIL import Static as st
from EasyML_Init import EM_App as app
from pandasql import sqldf

pdsql = lambda q: sqldf(q, globals())

layout = html.Div([
    html.H3
        (
            children='Dataframe Editor (SQL)',
            style={
                'textAlign': 'center',
                'color': 'white',
                'font-size': '40px',
                'background': 'royalblue'
            }
        ),
    dcc.Upload(
        id='page12_upload-data1',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select File #1')
        ]),
        style={
            'width': '98%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    dcc.Upload(
        id='page12_upload-data2',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select File #2')
        ]),
        style={
            'width': '98%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Button("Download table", id="page12_btn2", style={
        'background-color': '#7386D5',
        'border': '1%',
        'color': 'white',
        'font-size': '90%',
        'margin-left': '0.75%',
        'margin-right': '1%',
        'font-family': 'Helvetica'
    }),
    html.Button("Run Query", id="page12_btn3", style={
        'background-color': '#7386D5',
        'border': '1%',
        'color': 'white',
        'font-size': '90%',
        'font-family': 'Helvetica'
    }),
    dcc.Input(id='page12_queryBox', placeholder='Place query here...\n', type='text', style={
        'width': '100%', 'margin-top': '2%', 'margin-bottom': '2%'}),
    html.H5('', id='page12_downLink'),
    html.H5('', id='page12_testText'),
    html.Div(id='page12_output-data-upload1', style={
        'position': 'absolute', 'left': '1%', 'width': '49%'
    }),
    html.Div(id='page12_output-data-upload2', style={
        'position': 'absolute', 'left': '50.5%', 'width': '49%'
    }),
    html.Div(id='page12_test', style={
        'position': 'absolute', 'width': '90%', 'top': '130%', 'left': '5%'
    }),
    html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'})
])


def page12_parse_contents(contents, filename, datatime, i):
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

    if i == 1:
        st.a.tab1 = copy.deepcopy(df)

    elif i == 2:
        st.a.tab2 = copy.deepcopy(df)

    return html.Div([
        html.H5('table' + str(i)),
        dt.DataTable(rows=df.to_dict('records')),
        html.Hr()
    ])


@app.callback(Output('page12_output-data-upload1', 'children'),
              [Input('page12_upload-data1', 'contents'),
               Input('page12_upload-data1', 'filename'),
               Input('page12_upload-data1', 'last_modified')])
def page12_update_output1(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            page12_parse_contents(c, n, d, 1) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


@app.callback(Output('page12_output-data-upload2', 'children'),
              [Input('page12_upload-data2', 'contents'),
               Input('page12_upload-data2', 'filename'),
               Input('page12_upload-data2', 'last_modified')])
def page12_update_output2(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            page12_parse_contents(c, n, d, 2) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children



@app.callback(
    Output('page12_downLink', 'children'),
    [Input('page12_btn2', 'n_clicks')])
def page12_downloadTable(n_clicks):
    # Download table here
    df_3 = copy.deepcopy(st.a.tab3)
    print(df_3)
    try:
        df_3.to_csv("output_filename.csv", index=False, encoding='utf8', header=True)
    except Exception as e:
        # return df_3.to_html()
        return
    return


@app.callback(
    Output('page12_test', 'children'),
    [Input('page12_btn3', 'n_clicks'),
     Input('page12_queryBox', 'value')])
def page12_runQuery(n_clicks, value):
    if (n_clicks==None):
        return html.Div([])
    elif (n_clicks>st.a.clk):
        try:
            st.a.clk=n_clicks
            str2 = value
            table1= st.a.tab1
            table2 = st.a.tab2
            final_table=sqldf(str2,locals())
            st.a.tab3=copy.deepcopy(final_table)
            print(st.a.tab3)
            st.final.clk=n_clicks
            return html.Div([
                html.H5('New Table', style={'margin-top':'5%'}),
                dt.DataTable(rows=st.a.tab3.to_dict('records'),
                             row_selectable=True, filterable=True, sortable=True, selected_row_indices=[], ),
                html.Hr()
            ])
        except Exception as e:
            strr = str(e)
            parse = strr.split(")")
            parse1 = parse[1].split("[")
            print(e)
            return html.Div([
                html.H4(str(parse1[0]))], style={'margin-top': '5%'})
