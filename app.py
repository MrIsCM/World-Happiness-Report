import dash
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from color_themes import dark_mode

# global color_theme, color_template

# Initialize the Dash app with dark theme
app = dash.Dash(
    __name__, 
    title='Global Happiness Dashboard - Dark Mode',
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}]
)

data_file = "Data/Data_Happiness.xlsx"

# Read data
df = pd.read_excel(data_file)

# Add region category

region_mapping = {
    # Western Europe
    "Austria": "Western Europe",
    "Belgium": "Western Europe",
    "Cyprus": "Western Europe",
    "Denmark": "Western Europe",
    "Finland": "Western Europe",
    "France": "Western Europe",
    "Germany": "Western Europe",
    "Greece": "Western Europe",
    "Iceland": "Western Europe",
    "Ireland": "Western Europe",
    "Italy": "Western Europe",
    "Luxembourg": "Western Europe",
    "Malta": "Western Europe",
    "Netherlands": "Western Europe",
    "Norway": "Western Europe",
    "Portugal": "Western Europe",
    "Spain": "Western Europe",
    "Sweden": "Western Europe",
    "Switzerland": "Western Europe",
    "United Kingdom": "Western Europe",
    
    # Eastern Europe
    "Albania": "Eastern Europe",
    "Armenia": "Eastern Europe",
    "Azerbaijan": "Eastern Europe",
    "Belarus": "Eastern Europe",
    "Bosnia and Herzegovina": "Eastern Europe",
    "Bulgaria": "Eastern Europe",
    "Croatia": "Eastern Europe",
    "Czechia": "Eastern Europe",
    "Estonia": "Eastern Europe",
    "Georgia": "Eastern Europe",
    "Hungary": "Eastern Europe",
    "Kosovo": "Eastern Europe",
    "Latvia": "Eastern Europe",
    "Lithuania": "Eastern Europe",
    "Macedonia": "Eastern Europe",
    "Montenegro": "Eastern Europe",
    "North Macedonia": "Eastern Europe",
    "Poland": "Eastern Europe",
    "Republic of Moldova": "Eastern Europe",
    "Romania": "Eastern Europe",
    "Russian Federation": "Eastern Europe",
    "Serbia": "Eastern Europe",
    "Slovakia": "Eastern Europe",
    "Slovenia": "Eastern Europe",
    "Ukraine": "Eastern Europe",
    
    # North America
    "Canada": "North America",
    "United States": "North America",
    
    # South America
    "Argentina": "South America",
    "Belize": "South America",
    "Bolivia": "South America",
    "Brazil": "South America",
    "Chile": "South America",
    "Colombia": "South America",
    "Costa Rica": "South America",
    "Cuba": "South America",
    "Dominican Republic": "South America",
    "Ecuador": "South America",
    "El Salvador": "South America",
    "Guatemala": "South America",
    "Guyana": "South America",
    "Haiti": "South America",
    "Honduras": "South America",
    "Jamaica": "South America",
    "Mexico": "South America",
    "Nicaragua": "South America",
    "Panama": "South America",
    "Paraguay": "South America",
    "Peru": "South America",
    "Puerto Rico": "South America",
    "Suriname": "South America",
    "Trinidad and Tobago": "South America",
    "Uruguay": "South America",
    "Venezuela": "South America",
    
    # Middle East
    "Bahrain": "Middle East",
    "Iran": "Middle East",
    "Iraq": "Middle East",
    "Israel": "Middle East",
    "Jordan": "Middle East",
    "Kuwait": "Middle East",
    "Lebanon": "Middle East",
    "North Cyprus": "Middle East",
    "Oman": "Middle East",
    "Qatar": "Middle East",
    "Saudi Arabia": "Middle East",
    "State of Palestine": "Middle East",
    "Syria": "Middle East",
    "Türkiye": "Middle East",
    "United Arab Emirates": "Middle East",
    "Yemen": "Middle East",
    
    # Asia
    "Afghanistan": "Asia",
    "Bangladesh": "Asia",
    "Bhutan": "Asia",
    "Cambodia": "Asia",
    "China": "Asia",
    "Hong Kong SAR of China": "Asia",
    "India": "Asia",
    "Indonesia": "Asia",
    "Japan": "Asia",
    "Kazakhstan": "Asia",
    "Kyrgyzstan": "Asia",
    "Lao PDR": "Asia",
    "Malaysia": "Asia",
    "Maldives": "Asia",
    "Mongolia": "Asia",
    "Myanmar": "Asia",
    "Nepal": "Asia",
    "Pakistan": "Asia",
    "Philippines": "Asia",
    "Republic of Korea": "Asia",
    "Singapore": "Asia",
    "Sri Lanka": "Asia",
    "Taiwan Province of China": "Asia",
    "Tajikistan": "Asia",
    "Thailand": "Asia",
    "Turkmenistan": "Asia",
    "Uzbekistan": "Asia",
    "Viet Nam": "Asia",
    
    # Oceania
    "Australia": "Oceania",
    "New Zealand": "Oceania",
    
    # Africa
    "Algeria": "Africa",
    "Angola": "Africa",
    "Benin": "Africa",
    "Botswana": "Africa",
    "Burkina Faso": "Africa",
    "Burundi": "Africa",
    "Cameroon": "Africa",
    "Central African Republic": "Africa",
    "Chad": "Africa",
    "Comoros": "Africa",
    "Congo": "Africa",
    "Côte d’Ivoire": "Africa",
    "DR Congo": "Africa",
    "Djibouti": "Africa",
    "Egypt": "Africa",
    "Eswatini": "Africa",
    "Ethiopia": "Africa",
    "Gabon": "Africa",
    "Gambia": "Africa",
    "Ghana": "Africa",
    "Guinea": "Africa",
    "Kenya": "Africa",
    "Lesotho": "Africa",
    "Liberia": "Africa",
    "Libya": "Africa",
    "Madagascar": "Africa",
    "Malawi": "Africa",
    "Mali": "Africa",
    "Mauritania": "Africa",
    "Mauritius": "Africa",
    "Morocco": "Africa",
    "Mozambique": "Africa",
    "Namibia": "Africa",
    "Niger": "Africa",
    "Nigeria": "Africa",
    "Rwanda": "Africa",
    "Senegal": "Africa",
    "Sierra Leone": "Africa",
    "Somalia": "Africa",
    "Somaliland Region": "Africa",
    "South Africa": "Africa",
    "South Sudan": "Africa",
    "Sudan": "Africa",
    "Swaziland": "Africa",
    "Tanzania": "Africa",
    "Togo": "Africa",
    "Tunisia": "Africa",
    "Uganda": "Africa",
    "Zambia": "Africa",
    "Zimbabwe": "Africa"
}

regions = [
    "Western Europe", "Eastern Europe", "North America", "South America", "Africa", "Middle East", "Asia", "Oceania", "Other"
]

display_names = {
    'Explained by: Log GDP per capita'          : 'GDP per Capita',
    'Explained by: Social support'              : 'Social Support',
    'Explained by: Healthy life expectancy'     : 'Healthy Life Expectancy',
    'Explained by: Freedom to make life choices': 'Freedom',
    'Explained by: Generosity'                  : 'Generosity',
    'Explained by: Perceptions of corruption'   : 'Corruption',
}

df['Region'] = df['Country name'].map(region_mapping).fillna('Other')


color_theme, color_template = dark_mode(app)


# App layout
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("Global Happiness Dashboard", style={'textAlign': 'center', 'color': color_theme['text']}),
        html.P("Interactive exploration of happiness factors around the world", 
               style={'textAlign': 'center', 'color': color_theme['secondary_text']})
    ], style={'padding': '20px', 'backgroundColor': color_theme['card_background']}),
    
    # ----------------------------------------------
    #               Control Panel
    # ----------------------------------------------
    html.Div([
        html.Div([
            html.Label("Select Year:", style={'color': color_theme['text']}),
            dcc.Slider(
                id='year-slider',
                min=df['Year'].min(),
                max=df['Year'].max(),
                value=df['Year'].max(),
                marks={str(year): {"label": str(year), "style": {"color": color_theme['text']}} for year in df['Year'].unique()},
                step=None
            )
        ], style={'width': '100%', 'padding': '10px'}),
        
        html.Div([
            html.Label("Select Region:", style={'color': color_theme['text']}),
            dcc.Dropdown(
                id='region-dropdown',
                options=[{'label': 'All Regions', 'value': 'all'}] + 
                        [{'label': region, 'value': region} for region in regions],
                value='all',
                clearable=False,
                className='dash-dropdown'
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
        
        html.Div([
            html.Label("Select Factor:", style={'color': color_theme['text']}),
            dcc.Dropdown(
                id='factor-dropdown',
                options=[
                    {'label': 'GDP per Capita', 'value': 'Explained by: Log GDP per capita'},
                    {'label': 'Social Support', 'value': 'Explained by: Social support'},
                    {'label': 'Healthy Life Expectancy', 'value': 'Explained by: Healthy life expectancy'},
                    {'label': 'Freedom', 'value': 'Explained by: Freedom to make life choices'},
                    {'label': 'Generosity', 'value': 'Explained by: Generosity'},
                    {'label': 'Corruption', 'value': 'Explained by: Perceptions of corruption'}
                ],
                value='Explained by: Log GDP per capita',
                clearable=False,
                className='dash-dropdown'
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
    ], style={'backgroundColor': color_theme['control_background'], 'padding': '20px', 'borderRadius': '5px'}),
    
    # Main Visualizations
    # First Row
    html.Div([
        # Map
        html.Div([
            html.H3("Happiness Around the World", style={'textAlign': 'center', 'color': color_theme['text']}),
            dcc.Graph(id='happiness-map')
        ], style={'width': '100%', 'display': 'inline-block', 'padding': '10px'}),
    ], style={'display': 'flex', 'flexWrap': 'wrap'}),
    
    # Second Row
    html.Div([
        # Scatter Plot
        html.Div([
            html.H3("Happiness vs Selected Factor", style={'textAlign': 'center', 'color': color_theme['text']}),
            dcc.Graph(id='happiness-scatter')
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
        
        # Bar Chart
        html.Div([
            html.H3("Top 10 Happiest Countries", style={'textAlign': 'center', 'color': color_theme['text']}),
            dcc.Graph(id='happiness-bar')
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'})
    ], style={'display': 'flex', 'flexWrap': 'wrap'}),
    
    # Third Row
    html.Div([
        # Time Series
        html.Div([
            html.H3("Happiness Trend Over Time", style={'textAlign': 'center', 'color': color_theme['text']}),
            html.P("Click on countries in the map or bar chart to add them to the trend chart:", 
                   style={'textAlign': 'center', 'color': color_theme['secondary_text']}),
            dcc.Graph(id='happiness-time-series')
        ], style={'width': '100%', 'display': 'inline-block', 'padding': '10px'}),
    ]),
    
    # Fourth Row (Radar Chart and Details)
    html.Div([
        # Country Detail with Radar Chart
        html.Div([
            html.H3("Country Profile", style={'textAlign': 'center', 'color': color_theme['text']}),
            html.P("Click on a country in any chart to see detailed profile", 
                   style={'textAlign': 'center', 'color': color_theme['secondary_text']}),
            dcc.Graph(id='country-radar')
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
        
        # Statistics Panel
        html.Div([
            html.H3("Summary Statistics", style={'textAlign': 'center', 'color': color_theme['text']}),
            html.Div(id='stats-panel', 
                     style={'padding': '15px', 'backgroundColor': color_theme['card_background'], 
                            'borderRadius': '5px', 'color': color_theme['text']})
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'})
    ], style={'display': 'flex', 'flexWrap': 'wrap'}),
    
    # Store for selected countries
    dcc.Store(id='selected-countries', data=[]),
    
    # Footer
    html.Div([
        html.P("Data based on World Happiness Report - Created with Dash and Plotly",
               style={'textAlign': 'center', 'fontStyle': 'italic', 'color': color_theme['secondary_text']})
    ], style={'padding': '20px', 'marginTop': '20px', 'backgroundColor': color_theme['card_background']})
], style={'maxWidth': '1200px', 'margin': '0 auto', 'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif'})


# -------------------------------------------------
#                   Callbacks
# -------------------------------------------------

# World map graph
@callback(
    Output('happiness-map', 'figure'),
    [Input('year-slider', 'value'),
     Input('region-dropdown', 'value')]
)
def update_map(selected_year, selected_region):
    # Filter data by year
    filtered_df = df[df['Year'] == selected_year]
    
    # Apply region filter if not 'all'
    if selected_region != 'all':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    
    # Create choropleth map
    fig = px.choropleth(
        filtered_df,
        locations='Country name',
        locationmode='country names',
        color='Ladder score',
        hover_name='Country name',
        projection='natural earth',
        color_continuous_scale='Plasma',
        range_color=[1, 10],
        title=f'Happiness Score by Country ({selected_year})',
        height=500
    )
    
    fig.update_layout(
        template=color_template,
        coloraxis_colorbar=dict(
            title='Happiness<br>Score',
            thicknessmode="pixels",
            thickness=20
        ),
        margin=dict(l=0, r=0, t=50, b=0),
        geo=dict(
            showframe=False,
            showcoastlines=True,
            showcountries=True,
            countrycolor='#444444',
            bgcolor=color_theme['background']
        )
    )
    
    return fig


# Scatter plot
# Happiness vs selected factor
@callback(
    Output('happiness-scatter', 'figure'),
    [Input('year-slider', 'value'),
     Input('region-dropdown', 'value'),
     Input('factor-dropdown', 'value')]
)
def update_scatter(selected_year, selected_region, selected_factor):
    # Filter data by year
    filtered_df = df[df['Year'] == selected_year]
    
    # Apply region filter if not 'all'
    if selected_region != 'all':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    
    # Create scatter plot
    fig = px.scatter(
        filtered_df,
        x=selected_factor,
        y='Ladder score',
        color='Region',
        hover_name='Country name',
        size='Ladder score',
        size_max=15,
        opacity=0.7,
        height=400,
        color_discrete_sequence=px.colors.qualitative.Bold,
        title=f'Happiness Score vs {display_names[selected_factor]} ({selected_year})'
    )
    
    # Add trendline
    fig.update_layout(
        template=color_template,
        xaxis_title=display_names[selected_factor],
        yaxis_title='Happiness Score',
        legend_title='Region'
    )
    
    # Add trendline
    fig.add_traces(
        px.scatter(
            filtered_df,
            x=selected_factor,
            y='Ladder score',
            trendline='ols'
        ).data[1]
    )
    
    return fig

# Bar graph
@callback(
    Output('happiness-bar', 'figure'),
    [Input('year-slider', 'value'),
     Input('region-dropdown', 'value')]
)
def update_bar(selected_year, selected_region):
    # Filter data by year
    filtered_df = df[df['Year'] == selected_year]
    
    # Apply region filter if not 'all'
    if selected_region != 'all':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    
    # Sort and get top 10
    top_df = filtered_df.sort_values('Ladder score', ascending=False).head(10)
    
    # Create bar chart
    fig = px.bar(
        top_df,
        x='Country name',
        y='Ladder score',
        color='Region',
        text='Ladder score',
        height=400,
        color_discrete_sequence=px.colors.qualitative.Bold,
        title=f'Top 10 Happiest Countries ({selected_year})',
        range_y=[0, 10],
    )
    
    fig.update_traces(
        texttemplate='%{text:.2f}',
        textposition='outside'
    )
    
    fig.update_layout(
        template=color_template,
        xaxis_title='Country',
        yaxis_title='Happiness Score',
        xaxis={'categoryorder':'total descending'}
    )
    
    return fig

# Selected countries
@callback(
    [Output('selected-countries', 'data')],
    [Input('happiness-map', 'clickData'),
     Input('happiness-bar', 'clickData'),
     Input('happiness-scatter', 'clickData')],
    [Input('selected-countries', 'data')]
)
def update_selected_countries(map_click, bar_click, scatter_click, current_countries):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        return [current_countries]
    
    
    # Determine which input triggered the callback
    input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    # Process the appropriate clickData
    if input_id == 'happiness-map' and map_click:
        country = map_click['points'][0]['location']
    elif input_id == 'happiness-bar' and bar_click:
        country = bar_click['points'][0]['x']
    elif input_id == 'happiness-scatter' and scatter_click:
        country = scatter_click['points'][0]['hovertext']
    else:
        return [current_countries]
    
    # Update the list (add if not present, remove if already selected)
    countries = current_countries.copy()
    if country in countries:
        countries.remove(country)
    else:
        # Limit to 5 countries maximum
        if len(countries) >= 5:
            countries.pop(0)  # Remove the oldest one
        countries.append(country)
    
    return [countries]

@callback(
    Output('happiness-time-series', 'figure'),
    [Input('selected-countries', 'data')]
)
def update_time_series(countries):
    if not countries:
        # Show all regions averaged if no country is selected
        time_df = df.groupby(['Year', 'Region'])['Ladder score'].mean().reset_index()
        fig = px.line(
            time_df,
            x='Year',
            y='Ladder score',
            color='Region',
            height=400,
            color_discrete_sequence=px.colors.qualitative.Bold,
            title='Average Happiness Score by Region (2011-2022)'
        )
    else:
        # Filter by selected countries
        time_df = df[df['Country name'].isin(countries)].sort_values('Year')
        fig = px.line(
            time_df,
            x='Year',
            y='Ladder score',
            color='Country name',
            height=400,
            color_discrete_sequence=px.colors.qualitative.Bold,
            title='Happiness Score Trends for Selected Countries (2011-2024)',
            markers=True
        )
    
    fig.update_layout(
        template=color_template,
        xaxis_title='Year',
        yaxis_title='Ladder score',
        xaxis=dict(dtick=1)  # Show every year
    )
    
    return fig

# Radar chart
@callback(
    Output('country-radar', 'figure'),
    [Input('selected-countries', 'data'),
     Input('year-slider', 'value')]
)
def update_radar_chart(countries, selected_year):
    # If no country selected, show empty chart with message
    if not countries:
        fig = go.Figure()
        fig.add_annotation(
            text="Click on a country in any chart to see detailed profile",
            xref="paper", yref="paper",
            x=0.5, y=0.5,
            showarrow=False,
            font=dict(size=16, color=color_theme['text'])
        )
        fig.update_layout(
            template=color_template,
            height=400
        )
        return fig
    
    # Use the most recently selected country
    country = countries[-1]


    # Filter data for the selected country and year
    country_data = df[(df['Country name'] == country) & (df['Year'] == selected_year)].iloc[0]
    
    # Get the factors for radar chart
    categories = [
        'Explained by: Log GDP per capita',
        'Explained by: Social support',
        'Explained by: Healthy life expectancy',
        'Explained by: Freedom to make life choices',
        'Explained by: Generosity',
        'Explained by: Perceptions of corruption'
    ]
    
    # Format category names for display
    category_names = [display_names[cat] for cat in categories]
    
    # Extract values
    values = [country_data[cat] for cat in categories]

    # Normalize values to [0, 1] for radar chart
    max_values = df[categories].max().values

    values_norm = [value / max_value for value, max_value in zip(values, max_values)]
    
    # Create radar chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values_norm,
        theta=category_names,
        fill='toself',
        name=country,
        line=dict(color=color_theme['accent'])
    ))
    
    fig.update_layout(
        template=color_template,
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1],
                color=color_theme['secondary_text']
            ),
            angularaxis=dict(
                color=color_theme['text']
            ),
            bgcolor=color_theme['background']
        ),
        title=f"{country}'s Happiness Factors ({selected_year})",
        height=400
    )
    
    return fig

@callback(
    Output('stats-panel', 'children'),
    [Input('year-slider', 'value'),
     Input('region-dropdown', 'value'),
     Input('selected-countries', 'data')]
)
def update_stats_panel(selected_year, selected_region, selected_countries):
    # Filter data by year
    filtered_df = df[df['Year'] == selected_year]
    
    # Apply region filter if not 'all'
    if selected_region != 'all':
        region_df = filtered_df[filtered_df['Region'] == selected_region]
    else:
        region_df = filtered_df
    
    # Compute statistics
    global_avg = filtered_df['Ladder score'].mean()
    region_avg = region_df['Ladder score'].mean() if not region_df.empty else 0
    highest_country = filtered_df.loc[filtered_df['Ladder score'].idxmax()]['Country name']
    highest_score = filtered_df['Ladder score'].max()
    
    # Country-specific stats if any selected
    country_stats = []
    if selected_countries:
        country = selected_countries[-1]  # Most recently selected
        country_data = filtered_df[filtered_df['Country name'] == country]
        
        if not country_data.empty:
            country_row = country_data.iloc[0]
            score = country_row['Ladder score']
            rank = filtered_df['Ladder score'].rank(ascending=False)[country_data.index[0]]
            percentile = (len(filtered_df) - rank + 1) / len(filtered_df) * 100
            
            country_stats = [
                html.Hr(style={'borderColor': '#444444'}),
                html.H4(f"Selected Country: {country}", style={'color': color_theme['text']}),
                html.P([
                    html.Strong("Happiness Score: ", style={'color': color_theme['accent']}), 
                    html.Span(f"{score:.2f}", style={'color': color_theme['text']}),
                    html.Br(),
                    html.Strong("Global Rank: ", style={'color': color_theme['accent']}), 
                    html.Span(f"{int(rank)} of {len(filtered_df)} countries", style={'color': color_theme['text']}),
                    html.Br(),
                    html.Strong("Percentile: ", style={'color': color_theme['accent']}), 
                    html.Span(f"{percentile:.1f}%", style={'color': color_theme['text']})
                ])
            ]
    
    # Build stats panel content
    stats_content = [
        html.H4(f"Global Statistics ({selected_year})", style={'color': color_theme['text']}),
        html.P([
            html.Strong("Global Average Happiness: ", style={'color': color_theme['accent']}), 
            html.Span(f"{global_avg:.2f}", style={'color': color_theme['text']}),
            html.Br(),
            html.Strong(f"{'Region' if selected_region != 'all' else 'Selected Region'} Average: ", style={'color': color_theme['accent']}), 
            html.Span(f"{region_avg:.2f}" if selected_region != 'all' else "All Regions", style={'color': color_theme['text']}),
            html.Br(),
            html.Strong("Happiest Country: ", style={'color': color_theme['accent']}), 
            html.Span(f"{highest_country} ({highest_score:.2f})", style={'color': color_theme['text']}),
            html.Br(),
            html.Strong("Number of Countries: ", style={'color': color_theme['accent']}), 
            html.Span(f"{len(filtered_df)}", style={'color': color_theme['text']})
        ])
    ] + country_stats
    
    return stats_content

# Run the app
if __name__ == '__main__':
    app.run(debug=True)