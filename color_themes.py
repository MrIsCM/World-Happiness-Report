import plotly.express as px
import plotly.graph_objects as go

def dark_mode(app):
    # Define color scheme for dark mode
    color_theme = {
        'background': '#121212',
        'card_background': '#1E1E1E',
        'control_background': '#2C2C2C',
        'text': '#FFFFFF',
        'secondary_text': '#AAAAAA',
        'accent': '#BB86FC',
        'chart_colors': px.colors.sequential.Plasma
    }

    # Template for dark mode Plotly figures
    color_template = go.layout.Template()
    color_template.layout.plot_bgcolor = color_theme['background']
    color_template.layout.paper_bgcolor = color_theme['card_background']
    color_template.layout.font.color = color_theme['text']
    color_template.layout.xaxis.gridcolor = '#444444'
    color_template.layout.yaxis.gridcolor = '#444444'
    color_template.layout.xaxis.linecolor = '#444444'
    color_template.layout.yaxis.linecolor = '#444444'

    # Custom dark mode CSS
    app.index_string = '''
    <!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
            <style>
                body {
                    background-color: #121212;
                    color: #FFFFFF;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 0;
                }
                .dash-dropdown .Select-control {
                    background-color: #2C2C2C !important;
                    color: white !important;
                    border: 1px solid #444444 !important;
                }
                .dash-dropdown .Select-menu-outer {
                    background-color: #2C2C2C !important;
                    color: white !important;
                    border: 1px solid #444444 !important;
                }
                .dash-dropdown .Select-value-label {
                    color: white !important;
                }
                .dash-dropdown .Select-placeholder {
                    color: #AAAAAA !important;
                }
                .dash-dropdown .Select-menu-outer .Select-option:hover {
                    background-color: #444444 !important;
                }
                .rc-slider-track {
                    background-color: #BB86FC !important;
                }
                .rc-slider-handle {
                    border-color: #BB86FC !important;
                    background-color: #BB86FC !important;
                }
                .rc-slider-dot-active {
                    border-color: #BB86FC !important;
                }
                .rc-slider-mark-text {
                    color: #AAAAAA !important;
                }
            </style>
        </head>
        <body>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
    '''

    return color_theme, color_template

def light_mode(app):
    # Define color scheme for light mode
    light_colors = {
        'background': '#F5F5F5',
        'card_background': '#FFFFFF',
        'control_background': '#EFEFEF',
        'text': '#333333',
        'secondary_text': '#666666',
        'accent': '#0078D7',
        'chart_colors': px.colors.sequential.Viridis
    }

    # Template for light mode Plotly figures
    color_template = go.layout.Template()
    color_template.layout.plot_bgcolor = light_colors['background']
    color_template.layout.paper_bgcolor = light_colors['card_background'] 
    color_template.layout.font.color = light_colors['text']
    color_template.layout.xaxis.gridcolor = '#DDDDDD'
    color_template.layout.yaxis.gridcolor = '#DDDDDD'
    color_template.layout.xaxis.linecolor = '#CCCCCC'
    color_template.layout.yaxis.linecolor = '#CCCCCC'

    # Custom light mode CSS
    app.index_string = '''
    <!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
            <style>
                body {
                    background-color: #F5F5F5;
                    color: #333333;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 0;
                }
                .dash-dropdown .Select-control {
                    background-color: #EFEFEF !important;
                    color: #333333 !important;
                    border: 1px solid #DDDDDD !important;
                }
                .dash-dropdown .Select-menu-outer {
                    background-color: #FFFFFF !important;
                    color: #333333 !important;
                    border: 1px solid #DDDDDD !important;
                }
                .dash-dropdown .Select-value-label {
                    color: #333333 !important;
                }
                .dash-dropdown .Select-placeholder {
                    color: #666666 !important;
                }
                .dash-dropdown .Select-menu-outer .Select-option:hover {
                    background-color: #E6E6E6 !important;
                }
                .rc-slider-track {
                    background-color: #0078D7 !important;
                }
                .rc-slider-handle {
                    border-color: #0078D7 !important;
                    background-color: #0078D7 !important;
                }
                .rc-slider-dot-active {
                    border-color: #0078D7 !important;
                }
                .rc-slider-mark-text {
                    color: #666666 !important;
                }
            </style>
        </head>
        <body>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
    '''
    return light_colors, color_template
