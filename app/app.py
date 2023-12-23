from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

from function_to_app.charts_function import charts
from function_to_app.preprocessing_function import preprocessing_func

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
data = preprocessing_func.get_data()
app.layout = html.Div(children=[

    html.Div([
        html.H1("Contaminated Soils Dashboard"),
        html.P("Information about contaminated soils in Israel."),
        dcc.Markdown(
            '''
            **Description:**

            This dashboard provides information about contaminated soils in Israel. 
            You can explore the data and find more details on the [official government database](https://data.gov.il/dataset/contaminatedterrains).
            '''
        ),
    ], style={'margin': '20px'}),
    dcc.Graph(figure=charts.create_administrative_status_chart(data))
])
if __name__ == '__main__':
    app.run_server(debug=True)
