import datetime
import urllib
import math
import pandas as pd
from textwrap import wrap
import plotly.graph_objects as go
import dash_core_components as dcc

from assets.mappings import get_states, get_colors

def get_first_date():
    return datetime.date(2020, 4, 15)

def get_no_model_visual():
    return {
            "Shortage":"Baseline Ventilator Shortage",
            "Supply": "Current Ventilator Supply",
            "Demand":"Projected Ventilator Demand"
            }

def get_model_visual():
    return {
            "Shortage":" Optimized Shortage",
            "Supply": "Supply",
            "Demand":"Demand"
            }

def change2Percent(frac):
    return str(math.floor(100*frac))+'%'

def us_map(df,chosen_date,val,label_dict):
    if isinstance(chosen_date, str):
        chosen_date = datetime.datetime.strptime(chosen_date, '%Y-%m-%d').date()

    max_val = max(df.loc[df['State']!='US'][val])
    if max_val == 0:
        max_val = 500

    df = df.loc[df['Date']==chosen_date]
    df = df.loc[df['State']!='US']
    df = df.applymap(str)

    states = get_states()
    df.loc[:,'code'] = df.State.apply(lambda x: states[x])

    fig = go.Figure()

    df.loc[:,'text'] = df['State'] + '<br>' + \
                'Shortage ' + df['Shortage'] + '<br>' + \
                'Supply ' + df['Supply'] + '<br>' + \
                'Demand ' + df['Demand']

    bar_title = '{}'.format(label_dict[val])
    fig = go.Figure(data=go.Choropleth(
            locations=df['code'],
            z=df[val].astype(float),
            locationmode='USA-states',
            colorscale='Inferno_r',
            zmin = 0,
            zmax = max_val,
            autocolorscale=False,
            text=df['text'], # hover text
            marker_line_color='white', # line markers between states
            colorbar_title='<br>'.join(wrap(''.join([bar_title]), width=10)),
        ))

    title = '{} on {}'.format(label_dict[val], chosen_date.strftime('%b %d, %Y'))
    fig.update_layout(
            title_text='<br>'.join(wrap(''.join(['<b> ', title, ' </b>']), width=26)),
            geo = dict(
                scope='usa',
                projection=go.layout.geo.Projection(type = 'albers usa'),
                showlakes=True, # lakes
                lakecolor='rgb(255, 255, 255)'
            ),
        )

    graph = dcc.Graph(
        id='projection-map-vent',
        figure=fig
    )
    return graph

def us_timeline(df, title, with_opt):

    fig = go.Figure()
    colors = get_colors()
    if with_opt:

        # we want to keep the baseline shortage the same color as the prev. graph
        # and add a new color for the new shortage
        col_ind = [0,3]
        c = 0
        i = 0
        for val in df.columns:
            if val != "Date":
                fig.add_trace(go.Scatter(
                    x=df['Date'],
                    y=df[val].values,
                    legendgroup=i,
                    name=val.replace(' ','<br>'),
                    mode="lines+markers",
                    marker=dict(color=colors[col_ind[c]]),
                    line=dict(color=colors[col_ind[c]])
                ))
                c+=1
                i+=1

    else:
        state_cols = ["Shortage","Supply","Demand"]
        no_model_visual = get_no_model_visual()
        for i,val in enumerate(state_cols):
            fig.add_trace(go.Scatter(
                x=df['Date'],
                y=df[val].values,
                legendgroup=i,
                name=no_model_visual[val].replace(' ','<br>'),
                mode="lines+markers",
                marker=dict(color=colors[i]),
                line=dict(color=colors[i])
            ))
            i+=1

    fig.update_layout(
                height=550,
                title={
                    'text': '<br>'.join(wrap(''.join(['<b> ', title, ' </b>']), width=30)),
                    'y':0.96,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                title_font_size=20,
                xaxis={'title': "Date",'linecolor': 'lightgrey'},
                yaxis={'title': "Count",'linecolor': 'lightgrey'},
                legend_title='<b> Values Predicted </b>',
                margin={'l': 40, 'b': 40, 't': 40, 'r': 10},
                hovermode='closest',
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                legend={
                        "orientation": "h",
                        "xanchor": "center",
                        "y": -0.2,
                        "x": 0.5
                        },
                modebar={
                    'orientation': 'v',
                    'bgcolor': 'rgba(0,0,0,0)',
                    'color': 'lightgray',
                    'activecolor': 'gray'
                }
            )

    graph = dcc.Graph(
        id='projection-graph-vent',
        figure=fig
    )
    return graph
