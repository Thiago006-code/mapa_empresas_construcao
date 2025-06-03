import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os

# Dados detalhados para filtros e somatórios
detailed_data = [
    {'Local': 'Brasil', 'Tipo': 'Construção Civil', 'Porte': 'MEI', 'Quantidade': 1060054, 'Latitude': -14, 'Longitude': -52},
    {'Local': 'Brasil', 'Tipo': 'Construção Civil', 'Porte': 'ME', 'Quantidade': 489370, 'Latitude': -14, 'Longitude': -52},
    {'Local': 'Brasil', 'Tipo': 'Construção Civil', 'Porte': 'EPP', 'Quantidade': 86184, 'Latitude': -14, 'Longitude': -52},
    {'Local': 'Brasil', 'Tipo': 'Construção Civil', 'Porte': 'Demais', 'Quantidade': 59872, 'Latitude': -14, 'Longitude': -52},
    {'Local': 'Brasil', 'Tipo': 'Construção de Edifícios', 'Porte': 'MEI', 'Quantidade': 34, 'Latitude': -14, 'Longitude': -52},
    {'Local': 'Brasil', 'Tipo': 'Construção de Edifícios', 'Porte': 'ME', 'Quantidade': 112507, 'Latitude': -14, 'Longitude': -52},
    {'Local': 'Brasil', 'Tipo': 'Construção de Edifícios', 'Porte': 'EPP', 'Quantidade': 41038, 'Latitude': -14, 'Longitude': -52},
    {'Local': 'Brasil', 'Tipo': 'Construção de Edifícios', 'Porte': 'Demais', 'Quantidade': 32296, 'Latitude': -14, 'Longitude': -52},

    {'Local': 'Santa Catarina', 'Tipo': 'Construção Civil', 'Porte': 'MEI', 'Quantidade': 76807, 'Latitude': -27, 'Longitude': -50},
    {'Local': 'Santa Catarina', 'Tipo': 'Construção Civil', 'Porte': 'ME', 'Quantidade': 32637, 'Latitude': -27, 'Longitude': -50},
    {'Local': 'Santa Catarina', 'Tipo': 'Construção Civil', 'Porte': 'EPP', 'Quantidade': 4602, 'Latitude': -27, 'Longitude': -50},
    {'Local': 'Santa Catarina', 'Tipo': 'Construção Civil', 'Porte': 'Demais', 'Quantidade': 4351, 'Latitude': -27, 'Longitude': -50},
    {'Local': 'Santa Catarina', 'Tipo': 'Construção de Edifícios', 'Porte': 'ME', 'Quantidade': 6991, 'Latitude': -27, 'Longitude': -50},
    {'Local': 'Santa Catarina', 'Tipo': 'Construção de Edifícios', 'Porte': 'EPP', 'Quantidade': 2266, 'Latitude': -27, 'Longitude': -50},
    {'Local': 'Santa Catarina', 'Tipo': 'Construção de Edifícios', 'Porte': 'Demais', 'Quantidade': 3106, 'Latitude': -27, 'Longitude': -50},

    {'Local': 'Florianópolis', 'Tipo': 'Construção Civil', 'Porte': 'MEI', 'Quantidade': 5092, 'Latitude': -27.6, 'Longitude': -48.6},
    {'Local': 'Florianópolis', 'Tipo': 'Construção Civil', 'Porte': 'ME', 'Quantidade': 2143, 'Latitude': -27.6, 'Longitude': -48.6},
    {'Local': 'Florianópolis', 'Tipo': 'Construção Civil', 'Porte': 'EPP', 'Quantidade': 318, 'Latitude': -27.6, 'Longitude': -48.6},
    {'Local': 'Florianópolis', 'Tipo': 'Construção Civil', 'Porte': 'Demais', 'Quantidade': 711, 'Latitude': -27.6, 'Longitude': -48.6},
    {'Local': 'Florianópolis', 'Tipo': 'Construção de Edifícios', 'Porte': 'ME', 'Quantidade': 557, 'Latitude': -27.6, 'Longitude': -48.6},
    {'Local': 'Florianópolis', 'Tipo': 'Construção de Edifícios', 'Porte': 'EPP', 'Quantidade': 175, 'Latitude': -27.6, 'Longitude': -48.6},
    {'Local': 'Florianópolis', 'Tipo': 'Construção de Edifícios', 'Porte': 'Demais', 'Quantidade': 547, 'Latitude': -27.6, 'Longitude': -48.6},

    {'Local': 'Balneário Camboriú', 'Tipo': 'Construção Civil', 'Porte': 'MEI', 'Quantidade': 1653, 'Latitude': -26.9936, 'Longitude': -48.6352},
    {'Local': 'Balneário Camboriú', 'Tipo': 'Construção Civil', 'Porte': 'ME', 'Quantidade': 1130, 'Latitude': -26.9936, 'Longitude': -48.6352},
    {'Local': 'Balneário Camboriú', 'Tipo': 'Construção Civil', 'Porte': 'EPP', 'Quantidade': 230, 'Latitude': -26.9936, 'Longitude': -48.6352},
    {'Local': 'Balneário Camboriú', 'Tipo': 'Construção Civil', 'Porte': 'Demais', 'Quantidade': 361, 'Latitude': -26.9936, 'Longitude': -48.6352},
    {'Local': 'Balneário Camboriú', 'Tipo': 'Construção de Edifícios', 'Porte': 'ME', 'Quantidade': 303, 'Latitude': -26.9936, 'Longitude': -48.6352},
    {'Local': 'Balneário Camboriú', 'Tipo': 'Construção de Edifícios', 'Porte': 'EPP', 'Quantidade': 146, 'Latitude': -26.9936, 'Longitude': -48.6352},
    {'Local': 'Balneário Camboriú', 'Tipo': 'Construção de Edifícios', 'Porte': 'Demais', 'Quantidade': 331, 'Latitude': -26.9936, 'Longitude': -48.6352},
]

df_detalhado = pd.DataFrame(detailed_data)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Mapa Interativo - Total por Local', style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            html.Label('Local'),
            dcc.Dropdown(
                options=[{'label': loc, 'value': loc} for loc in df_detalhado['Local'].unique()],
                value=[],
                multi=True,
                id='local-dropdown'
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),

        html.Div([
            html.Label('Tipo'),
            dcc.Dropdown(
                options=[{'label': tipo, 'value': tipo} for tipo in df_detalhado['Tipo'].unique()],
                value=[],
                multi=True,
                id='tipo-dropdown'
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),

        html.Div([
            html.Label('Porte'),
            dcc.Dropdown(
                options=[{'label': porte, 'value': porte} for porte in df_detalhado['Porte'].unique()],
                value=[],
                multi=True,
                id='porte-dropdown'
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),
    ], style={'textAlign': 'center'}),

    dcc.Graph(id='mapa', style={'height': '800px'})
])

@app.callback(
    Output('mapa', 'figure'),
    Input('local-dropdown', 'value'),
    Input('tipo-dropdown', 'value'),
    Input('porte-dropdown', 'value')
)
def update_map(locais_selecionados, tipos_selecionados, portes_selecionados):
    filtered = df_detalhado.copy()

    if locais_selecionados:
        filtered = filtered[filtered['Local'].isin(locais_selecionados)]
    if tipos_selecionados:
        filtered = filtered[filtered['Tipo'].isin(tipos_selecionados)]
    if portes_selecionados:
        filtered = filtered[filtered['Porte'].isin(portes_selecionados)]

    group_cols = ['Local']
    if not locais_selecionados or len(set(filtered['Local'])) == 1:
        if tipos_selecionados:
            group_cols.append('Tipo')
        if portes_selecionados:
            group_cols.append('Porte')

    grouped = filtered.groupby(group_cols).agg({
        'Quantidade': 'sum',
        'Latitude': 'mean',
        'Longitude': 'mean'
    }).reset_index()

    # Colunas para mostrar no hover (sem Latitude e Longitude)
    hover_cols = group_cols + ['Quantidade']

    fig = px.scatter_geo(
        grouped,
        lat='Latitude',
        lon='Longitude',
        size='Quantidade',
        color='Local',
        custom_data=hover_cols,
        scope='south america',
        projection='natural earth',
        size_max=50
    )

    fig.update_layout(
        title='Quantidade Total por Local',
        geo=dict(
            showland=True,
            landcolor="LightGreen",
            showcountries=True,
            countrycolor="Black",
            lataxis_range=[-40, -5],
            lonaxis_range=[-80, -30],
        )
    )

    fig.update_traces(
        hovertemplate='<br>'.join([f'{col}: %{{customdata[{i}]}}' for i, col in enumerate(hover_cols)]) +
                      '<extra></extra>'
    )

    return fig

import os

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8050))
    app.run(host='0.0.0.0', port=port, debug=True)

