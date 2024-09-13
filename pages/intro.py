import pandas as pd
import dash
from dash import html, dash_table, dcc
import plotly.graph_objects as go

dash.register_page(__name__, path='/', name="Home Page", order=1)

####################### LOAD DATASET #############################
df = pd.read_excel('Trust Me Im a Cat.xlsx', sheet_name='Weekly Points')

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    dash_table.DataTable(data=df.to_dict('records'),
                         page_size=30,
                         editable=True,
                         style_cell={"background-color": "black", "border": "solid 1px white", "color": "white", "font-size": "20px", "text-align": "left"},
                         style_header={"background-color": "black", "font-weight": "bold", "color": "white", "padding": "10px", "font-size": "20px"},
                         style_table={'background-color': 'black'}
                        ),
])