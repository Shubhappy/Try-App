# # # import dash
# # # from dash import html, dcc, Dash, callback
# # # from dash import dash_table as dt
# # # from dash.dependencies import Input, Output
# # # from pandas import *
# # # import plotly.graph_objs as go
# # # import plotly.express as px
# # # import pandas as pd



# # # # df = pd.read_csv("C:\Users\USER\Desktop\Shubham\Try App\Data\Sales.Sales.Csv")

# # # df= pd.read_csv('C:\\Users\\USER\Desktop\Shubham\Try App\Data\Sales.Csv')

# # # # df['id'] = df['Months']
# # # # df.set_index('id', inplace=True, drop=False)



# # # app = Dash(__name__,title='Mxpertz') 

# # # app.layout=html.Div([

# # #      dt.DataTable(
# # #         id='select_month',
# # #         columns=[
# # #             {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
# # #             if i == "Customers" or i == "Orders_Placed" or i == "Item_Sold" or "Production_cost" or "Other_Cost" or "Inquiries" or "Lead" or "Opportunity"
# # #             else {"name": i, "id": i, "deletable": True, "selectable": True}
# # #             for i in df.columns],

# # #             data=df.to_dict('records'),  # the contents of the table
# # #             editable=True,              # allow editing of data inside all cells
# # #             filter_action="native",     # allow filtering of data by user ('native') or not ('none')
# # #             filter_options={'case':'insensitive'}, # make filter case insensitive  
# # #             sort_action="native",       # enables data to be sorted per-column by user or not ('none')
# # #             sort_mode="single",         # sort across 'multi' or 'single' columns
# # #             column_selectable="multi",  # allow users to select 'multi' or 'single' columns
# # #             row_selectable="single",     # allow users to select 'multi' or 'single' rows    
# # #             row_deletable=True,         # choose if user can delete a row (True) or not (False)
# # #             selected_columns=[],        # ids of columns that user selects
# # #             selected_rows=[],           # indices of rows that user selects
# # #             page_action="none",         # for display multi-row data in different pages select "native" 
# # #             fill_width=True,           # for resize column width
# # #             # style_cell={'minWidth': 0, 'maxWidth': 500, 'width': 1},    # ensure adequate header width when text is shorter than cell's text
# # #             ),

# # #             html.Br(),

# # #             html.Div(dcc.Graph(id='bar-container')),
         
            


# # #             ])


# # # # -------------------------------------------------------------------------------------
# # # # Create bar chart

# # # @callback(Output('bar-container', 'figure'),
# # #                 # Output('chart2', component_property='fig1'),
# # #               [Input('select_month', 'selected_rows'),
# # #               Input('select_month', "derived_virtual_data"),
# # #               Input('select_month','derived_virtual_selected_rows')])
# # # def build_graph(selected_rows,derived_virtual_data,derived_virtual_selected_rows):
# # #     print(derived_virtual_data)
    
    
# # #     revenue=df.Revenues.iloc[selected_rows]
# # #     target= df.Target.iloc[selected_rows]        

# # #     fig=go.Figure(go.Indicator(
# # #             customdata=[1,2,3,4,5],
# # #             mode = "number+gauge+delta", value = revenue,number={'valueformat':"0d"},visible=None,align='left',name="Revenue Generated",legendgrouptitle={'text' :'Revenue Generated'},
# # #             domain = {'x': [0, 0.5], 'y': [0, 1]},
# # #             title = {'text' :"<b>Sale (in ₹)</b>"},
# # #             delta = {'reference': target,'valueformat':"0d"},
# # #             gauge = {
# # #                     'shape': "angular",'bgcolor':'yellow','bar':{'line':{'width':1}},
# # #                     'axis': {'range': [None, 6000],'tickwidth': 1.5,'nticks':10,'ticksuffix':' ₹','ticks':"inside",'ticklen':5},
# # #                     'threshold': {
# # #                         'line': {'color': "red", 'width': 2},
# # #                         'thickness': 0.75,
# # #                         'value': target},
# # #                     }
# # #             ))
        
# # #     return fig


# # # if __name__=='__main__':
# # #     app.run_server(debug=True)




# # from dash import Dash, dash_table, dcc, html
# # from dash.dependencies import Input, Output, State
# # from pandas import *
# # import pandas as pd
# # import plotly.express as px
# # import plotly.graph_objs as go


# # app = Dash(__name__)

# # params = [
# # 'Months', 'Revenues', 'Target', 'Profit', 'Customers','Order Placed','Item Sold','Production Cost','Other Cost','Inquiries','Lead','Opportunities']


# # # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')



# # nmb_clicks = 0
# # app.layout = html.Div([
# #     # dcc.Store(id='click-memory', data = {'nmb_clicks': nmb_clicks}),
# #     html.Div([
# #         dcc.Input(
# #             id='adding-columns-name',
# #             placeholder='Enter a column name...',
# #             value='',
# #             style={'padding': 10}
# #         ),
# #         html.Button('Add Column', id='adding-columns-button', n_clicks=0)
# #     ], style={'height': 50}),

# #     # dash_table.DataTable(
# #     #     id='adding-rows-table',
# #     #     columns=[{"name": i, "id": i} for i in df.columns],
# #     #     data=df.to_dict('records'),
# #     #     editable=True,
# #     #     row_deletable=True
# #     # ),

# #     dash_table.DataTable(
# #         id='adding-rows-table',
# #         # columns=[{
# #         #     'name': 'Column {}'.format(i),
# #         #     'id': 'column-{}'.format(i),
# #         #     'deletable': True,
# #         #     'renamable': True
# #         # } for i in range(1, 10)],

# #         columns=([{'id': p, 'name': p} for p in params]),

# #         data=[
# #             {'column-{}'.format(i):
# #              0 for i in range(1, 5)}
# #             # for j in range(1)
# #         ],
# #         editable=True,
# #         export_columns='all',
# #         export_format='xlsx',
# #         export_headers='display',
# #     ),

# #     html.Div([html.Button('Add Row', id='adding-rows-button', n_clicks=0),],style={'height': 50}),
# #     html.Br(),
# #     #  html.Div(id='bar-container', style={'border':'2px solid black', 'height':'600px'}),
# #     dcc.Graph(id='bar-container')
# # ])


# # # -------------------------------------------------------------------------------------
# # # Adding data in column
# # @app.callback(Output('adding-rows-table', 'columns'),
# #              Input('adding-columns-button', 'n_clicks'),
# #              State('adding-columns-name', 'value'),
# #               State('adding-rows-table', 'columns'))
# # def update_columns(n_clicks, value,columns):             
# #     if n_clicks != 0:
# #         columns.append({
# #             'id': value, 'name': value,
# #             'renamable': True, 'deletable': True
# #         })
# #         # print(columns)
    
# #     return columns

# # # -------------------------------------------------------------------------------------
# # # Adding data in row
# # @app.callback(Output('adding-rows-table', 'data'),
# #              Input('adding-rows-button', 'n_clicks'),
# #              [State('adding-rows-table', 'data'),
# #              State('adding-rows-table', 'columns')])
# # def update_row(n_clicks, rows, columns):
    
# #     if n_clicks > 0:
# #         rows.append({c['id']: '' for c in columns})
# #     return rows

# # # -------------------------------------------------------------------------------------
# # # Adding data and update the graphs
# # @app.callback(
# #     Output('bar-container', 'figure'),
# #     Input('adding-rows-table', 'derived_virtual_data'),
# #     Input('adding-rows-table', 'derived_virtual_selected_rows'))
# # def display_output(all_rows_data, selected_row_indices):
# #      dff = pd.DataFrame(all_rows_data)

# #      if "Months" in dff and "Revenues" in dff:
# #         return (#dcc.Graph(id='graph',
# #                           px.bar(
# #                           dff,
# #                           x="Months",
# #                           y='Revenues',
# #                           labels={"Revenues": "Revenue"}
# #                      )
# #                     #   .update_traces(marker_color=colors, hovertemplate="<b>%{y}%</b><extra></extra>")
# #                       )
    




# # # # -------------------------------------------------------------------------------------
# # # # Storing data
# # # @app.callback(Output('click-memory', 'data'),
# # #              [Input('adding-columns-button', 'n_clicks')],
# # #              [Input('adding-rows-button', 'n_clicks')],
# # #              [State('click-memory', 'data')])
# # # def on_data(click,row_click, data):
# # #     if click != 0:
# # #         nmb_clicks = nmb_clicks+1
    
# # #     return nmb_clicks
    
# # #     if row_click != 0:
# # #         data['nmb_clicks'] = data['nmb_clicks'] + 1
        
# # #     return data

# # if __name__ == '__main__':
# #     app.run_server(debug=True)

# from dash import Dash, dcc, html
# from dash.dependencies import Output, Input, State
# from dash.exceptions import PreventUpdate

# # This stylesheet makes the buttons and table pretty.
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
   
#     dcc.Store(id='local', storage_type='local'),
    
#     html.Table([
#         html.Thead([
#             html.Tr(html.Th('Click to store in:', colSpan="3")),
#             html.Tr([
                
#                 html.Th(html.Button('localStorage', id='local-button')),
                
#             ]),
#             html.Tr([
               
#                 html.Th('Local clicks'),
                
#             ])
#         ]),
#         html.Tbody([
#             html.Tr([
               
#                 html.Td(0, id='local-clicks'),
               
#             ])
#         ])
#     ])
# ])

# # Create two callback for every store.
# for store in ('local'):

#     # add a click to the appropriate store.
#     @app.callback(Output(store, 'data'),
#                   Input('{}-button'.format(store), 'n_clicks'),
#                   State(store, 'data'))
#     def on_click(n_clicks, data):
#         if n_clicks is None:
#             # prevent the None callbacks is important with the store component.
#             # you don't want to update the store for nothing.
#             raise PreventUpdate

#         # Give a default data dict with 0 clicks if there's no data.
#         data = data or {'clicks': 0}

#         data['clicks'] = data['clicks'] + 1
#         return data

#     # output the stored clicks in the table cell.
#     @app.callback(Output('{}-clicks'.format(store), 'children'),
#                   # Since we use the data prop in an output,
#                   # we cannot get the initial data on load with the data prop.
#                   # To counter this, you can use the modified_timestamp
#                   # as Input and the data as State.
#                   # This limitation is due to the initial None callbacks
#                   # https://github.com/plotly/dash-renderer/pull/81
#                   Input(store, 'modified_timestamp'),
#                   State(store, 'data'))
#     def on_data(ts, data):
#         if ts is None:
#             raise PreventUpdate

#         data = data or {}

#         return data.get('clicks', 0)


# if __name__ == '__main__':
#     app.run_server(debug=True, port=8077, threaded=True)

import dash
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

x = 5

app.layout = html.Div([
    dcc.Store(id='memory-data', data = {'the-data': x}),
    html.Div([
        html.Button('click me', id='add-button')
    ]),
    html.Div(id='debug-out'),
])

@app.callback(Output('debug-out', 'children'),
             [Input('add-button', 'n_clicks')],
             [State('memory-data', 'data')])
def button_pressed(clicks, data):
    # if clicks!=0:
        # data =data + 10
    print(data)
    return data

if __name__ == '__main__':
    app.run_server(debug=True)