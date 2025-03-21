#!python3
# -*- coding: utf-8 -*-
#
#  дашборд 
# 
#  Evgeny S. Borisov <parser@mechanoid.su>
# 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# import os
import pandas as pd
import geopandas as gpd
# from shapely.geometry import Polygon
# import plotly.express as px
from dash import Dash, dcc, html, Input, Output
from dash_bootstrap_components import Table
import dash_leaflet as dl
# import dash_leaflet.express as dlx
# from dash.dash_table import DataTable
# import dash_bootstrap_components as dbc
# pd.options.plotting.backend = 'plotly'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
file_path='data/2025/df_flat.pkl'

id_header = 'header0'
id_footer = 'fotter0'
id_side = 'side0'
id_content = 'content0'
id_map = 'map0'

map_center_coo = [45.,33.,]
map_zoom = 9

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

style_header = {
     'position':'fixed', # Фиксированное положение 
     'height': '10%', 
     'background': '#FEDFC0',
     'border-bottom': '1px solid #7B5427',
     'width': '100%', # Ширина слоя
}

style_side = { 
    'top': '11%', # Расстояние от верхнего края
    'width': '250px', 
    'background': '#ECF5E4',
    'border-right': '1px solid #231F20',
    'bottom': '0', # Расстояние снизу 
    'position': 'absolute',
    'overflow': 'auto', 
    'padding': '0',
     'height': '50%', 
}

style_contnent = {
    'top': '11%', # Расстояние от верхнего края
    'left': '260px', # Расстояние от левого края 
    'bottom': '0',
    'right': '0',
    'position': 'absolute',
    'overflow': 'auto', 
    'background': '#2C20F0',
    'padding': '0',
     'height': '50%', 
}

style_footer = {
    'position':'fixed', # Фиксированное положение 
    'left': '0', 
    'bottom': '0', # Левый нижний угол 
    'padding': '0',
    #'background': '#39b54a', # Цвет фона
    'color': '#fff', # Цвет текста
    'width': '100%', # Ширина слоя
    'border-top': '1px solid #231F20',
}

style_map = {
    # 'top': '0', # Расстояние от верхнего края
    'width': '100%', 
    'height': '70%',
    # 'margin': 'auto',
    # "display": 'block',
    # 'height': '50vh',
}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
app = Dash()

def data_load(file_path=file_path):
    cols = ['title','address','priceM','dt','url']
    df = pd.read_pickle(file_path)
    df['dt'] = df['ts'].dt.date
    return df[cols]

def content(df):
    df = df[df['dt']==df['dt'].max()]
    df = df.sample(10)
    return Table.from_dataframe(df, striped=True, bordered=True, hover=True)

def map_():
    return dl.Map( children=[dl.TileLayer()], id=id_map, zoom=map_zoom, center=map_center_coo, style=style_map  )
    # app.layout = dl.Map(dl.TileLayer(), center=[56,10], zoom=6, style={'height': '50vh'})
    # return dl.Map( id=id_map, center=map_center_coo, zoom=6 ) 
    # return dl.Map( dl.TileLayer(), id=id_map, center=map_center_coo, zoom=6 ) 

app.layout = html.Div([
    html.Div( id=id_header, style=style_header,   children=['header'] ), # header
    html.Div( id=id_side,   style=style_side,     children=['side'],      ), # side_panel
    # html.Div( id=id_content, style=style_contnent, children=[ map_() ] , ), # contnent
    html.Div( id=id_content, style=style_contnent, children=[ 'contnent' ] , ), # contnent
    html.Div( id=id_footer, style=style_footer,   children=[  content(data_load())  ] ), # footer

    # html.Div( id=id_content, style=style_contnent, children=[ 'contnent' ] , ), # contnent
    # html.Div( id=id_footer, style=style_footer, children=[ 'footer' ] ), # footer
 
    #html.Div(children=[
    #    html.Div( id=id_side,    style=style_side,     children=['side'],      ), # side_panel
    #    html.Div( id=id_content, style=style_contnent, children=[ map_() ] , ), # contnent
    #]),
    # html.Div( id=id_footer, style=style_footer, children=[ content(data_load()) ] ), # footer
])


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
if __name__ == '__main__': 
    # app.run_server() 
    app.run_server( debug=True, use_reloader=False )






#     children=[
#         # html.Div( id=ID_DATA_TABLE, style={'background-color':'#0ce','height':'24vh'}, ),
#         html.Div(    
#             children=[
#                 html.Div( # левая панель
#                     style= { 'width':'40%','float':'left',},
#                     children = [
#                         html.Div(style= {'margin':'5px',}, children = [
#                             # выбор комнаты
#                             html.Div( dcc.Dropdown(id=ID_NROOM, options=nrooms, value=NROOM_DEFAULT,clearable=False), style= { 'width':'40%','float':'left',}, ),  
#                             # выбор района
#                             html.Div( dcc.Dropdown(id=ID_FRAME, options=[FRAME_NAME_DEFAULT] + area_index, value=FRAME_NAME_DEFAULT,clearable=False ), style= {'width':'60%','float':'right',}, ), 
#                             ]),
#                         # панель с диаграммами
#                         html.Div( id=ID_STAT, style={'overflow-y':'auto','height':'70vh','clear':'left'}, ),
#                         # html.Div( id=ID_DATA_TABLE, style={'overflow-y':'auto','height':'25vh','clear':'left'}, children=[ panel_data(),]),
#                     ]
#                 ),
#                 html.Div( # правая панель
#                     style={'width':'60%','float':'left',},
#                     children = [
#                         html.Div(children =[
#                         panel_map_control(prices),
#                         dl.Map(
#                             id=ID_MAP,
#                             center=MAP_CENTER_COO,
#                             style={ 'width':'100%', 'height':'70vh', 'margin':'auto', 'display':'block',},
#                             ) 
#                         ])
#                     ]
#                 ),
#             ]),
#             html.Div( id=ID_DATA_TABLE, style={'overflow-y':'auto','width':'100%','background-color':'#eee','height':'23vh','clear':'left' }, ),
#     ],
# )


# style_footer = { 'width':'100%','clear':'left','overflow-y':'auto','background-color':'#0fe', }
# style_map = { 'height':'70vh', 'width':'60%', } # 'width':'100%', 'margin':'auto', 'display':'block',},


# #header {
#     height: 80px; /* Высота слоя */
#     background: #FEDFC0; border-bottom: 2px solid #7B5427;
# }
# #header h1 { padding: 20px; margin: 0; }

# #sidebar { 
#     width: 150px; background: #ECF5E4; border-right: 1px solid #231F20;
#     top: 82px; /* Расстояние от верхнего края */ 
#     bottom: 0; /* Расстояние снизу  */
#     position: absolute;
#     overflow: auto; 
#     padding: 10px;
# }

# #content {
#     top: 82px; /* Расстояние от верхнего края */
#     left: 170px; /* Расстояние от левого края */ 
#     bottom: 0; right: 0;
#     position: absolute;
#     overflow: auto; 
#     padding: 10px;
# }

#  #footer {
#     position: fixed; /* Фиксированное положение */
#     left: 0; bottom: 0; /* Левый нижний угол */
#     padding: 10px; /* Поля вокруг текста */
#     background: #39b54a; /* Цвет фона */
#     color: #fff; /* Цвет текста */
#     width: 100%; /* Ширина слоя */
#    }

