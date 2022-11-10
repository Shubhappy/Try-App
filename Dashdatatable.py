from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output, State
from pandas import *
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from random import randint


app = Dash(__name__)

app.layout = html.Div([
    
    html.Div([
        dcc.Input(
            id='adding-columns-name',
            placeholder='Enter a column name...',
            value='',
            style={'padding': 10}
        ),
        html.Button('Add Column', id='adding-columns-button', n_clicks=0)
    ], style={'height': 50}),

   
    dash_table.DataTable(
        id='adding-rows-table',
      
        columns = [
    dict(id='Month', name='Month'),
    dict(id='Revenue', name='Revenues', type='numeric'),
    dict(id='Target', name='Target', type='numeric')
],

        data = [
        dict(Month='Month name', Revenue=1, Target=1)
             
        for j in range(1)],       

        editable=True,
        export_columns='all',
        export_format='xlsx',
        export_headers='display',
        row_deletable=True
    ),

    html.Div([html.Button('Add Row for data entry', id='adding-rows-button', n_clicks=0),],style={'height': 50}),
    html.Br(),
    html.Div([
    html.Div(id='bar-container',className='bar-contain'),    
    html.Div(id='bar-container2',className='bar-contain'),
    ],className='bar_div'),
    dcc.Store(id='click-memory',data=[],storage_type='memory'),
])

# -------------------------------------------------------------------------------------
# Storing row data
@app.callback(Output('click-memory', 'data'),
             Input('adding-rows-table', 'data'),
             prevent_initial_call=True
            #  Input('bar-container', component_property='children')]
            )
def store_data(data):
    
    return data

# -------------------------------------------------------------------------------------
#Adding data in row
@app.callback(Output('adding-rows-table', 'data'),
             Input('adding-rows-button', 'n_clicks'),
             [State('click-memory', 'data'),
             State('adding-rows-table', 'columns')])
def update_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows

# -------------------------------------------------------------------------------------
# Adding data in column
@app.callback(Output('adding-rows-table', 'columns'),
             Input('adding-columns-button', 'n_clicks'),
             State('adding-columns-name', 'value'),
              State('adding-rows-table', 'columns'))
def update_columns(n_clicks, value,columns):             
    if n_clicks != 0:
        columns.append({
            'id': value, 'name': value,
            'renamable': True, 'deletable': True
        })         
    return columns

# -------------------------------------------------------------------------------------
# Plotting Monthly Revenue bar chart
@app.callback(
    Output('bar-container', component_property='children'),
    Input('adding-rows-table', 'derived_virtual_data'),
    Input('adding-rows-table', 'derived_virtual_selected_rows'),
    Input('adding-rows-table', 'columns'),
    prevent_initial_call=True)
 

def display_output(all_rows_data,selected_row_indices,columns):
    
    df = pd.DataFrame(all_rows_data,columns=['Month','Revenue','Target'])
           
    return[dcc.Graph(
            id='graph',
            figure=px.bar(
                    df,
                    x='Month',
                    y='Revenue',
                    )
                    .update_traces(width=0.1)
                    .update_layout(title="Revenue per Month")
                      )]

# -------------------------------------------------------------------------------------
# Plotting Monthly Target bar chart
@app.callback(
    Output('bar-container2', component_property='children'),
    Input('adding-rows-table', 'derived_virtual_data'),
    Input('adding-rows-table', 'derived_virtual_selected_rows'),
    Input('adding-rows-table', 'columns'),
    prevent_initial_call=True) 

def display_output(all_rows_data,selected_row_indices,columns):
    
    df = pd.DataFrame(all_rows_data,columns=['Month','Revenue','Target'])
           
    return[dcc.Graph(
            id='graph2',
            figure=px.bar(
                    df,
                    x='Month',
                    y='Target',
                    )
                    .update_traces(width=0.1)
                    .update_layout(title="Monthly Target")
                      )]

# -------------------------------------------------------------------------------------
# Initialize the app
if __name__ == '__main__':
    app.run_server(debug=True)


