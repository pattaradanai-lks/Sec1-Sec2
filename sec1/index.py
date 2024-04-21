import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
from apps import scatter_layout, histogram_layout, line_layout, treemap_layout

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define URL to layout mapping
PAGE_CONTENT = {
    '/apps/scatter_layout': scatter_layout.layout,
    '/apps/histogram_layout': histogram_layout.layout,
    '/apps/treemap_layout': treemap_layout.layout,
    '/apps/line_layout': line_layout.layout,
    '/': "Please choose a link"
}

# the style arguments for the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Scatter", href="/apps/scatter_layout", active="exact"),
                dbc.NavLink("Histogram", href="/apps/histogram_layout", active="exact"),
                dbc.NavLink("Treemap", href="/apps/treemap_layout", active="exact"),
                dbc.NavLink("LineChart", href="/apps/line_layout", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    return PAGE_CONTENT.get(pathname, [
        html.H1("404: Not found", className="text-danger"),
        html.Hr(),
        html.P(f"The pathname {pathname} was not recognised..."),
    ])

if __name__ == '__main__':
    app.run_server(debug=False)
