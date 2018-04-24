from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from EasyML_Init import EM_App
from Pages.Page_Main import EasyML_Page1, EasyML_Page2, EasyML_Page3, EasyML_Page4, EasyML_Page5, EasyML_Page6, \
    EasyML_Page7, EasyML_Page8, EasyML_Page9, EasyML_Page10, EasyML_Page11, EasyML_Page12, EasyML_Page13
from Pages.Page_Index import Index_Page

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'text2': '#000000'
}


EM_App.layout = html.Div([

    dcc.Location(id='EasyML_Main_Url', refresh=False),
    html.Div(id='EasyML_Main_page-content'),
    html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'}),

    html.Hr(style={'position':'relative','float':'bottom','top':'500px'})
    ],
    style={
    }
)
EM_App.title='EasyML'





@EM_App.callback(Output('EasyML_Main_page-content', 'children'),
              [Input('EasyML_Main_Url', 'pathname')])
def display_page(pathname):
    if(pathname=='/test/page1'):
        return EasyML_Page1.layout
    elif (pathname == '/test/page2'):
        return EasyML_Page2.layout
    elif (pathname == '/test/page3'):
        return EasyML_Page3.layout
    elif (pathname == '/test/page4'):
        return EasyML_Page4.layout
    elif (pathname == '/test/page5'):
        return EasyML_Page5.layout
    elif (pathname == '/test/page6'):
        return EasyML_Page6.layout
    elif (pathname == '/test/page7'):
        return EasyML_Page7.layout
    elif (pathname == '/test/page8'):
        return EasyML_Page8.layout
    elif (pathname == '/test/page9'):
        return EasyML_Page9.layout
    elif (pathname == '/test/page10'):
        return EasyML_Page10.layout
    elif (pathname == '/test/page11'):
        return EasyML_Page11.layout
    elif (pathname == '/test/page12'):
        return EasyML_Page12.layout
    elif (pathname == '/test/page13'):
        return EasyML_Page13.layout
    else:
        return Index_Page.layout




if __name__ == '__main__':
    EM_App.run_server(debug=True)