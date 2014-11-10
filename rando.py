import plotly.plotly as py
from plotly.graph_objs import *
from water_readin import  *
from secret import*
# Fill in with your personal username and API key
# or, use this public demo account
py.sign_in('jamn_chick', key)

years = range(1999,2014)
y_data = water

trace1 = Bar(
    x=years,
    y=water,
    name='Water',
    marker=Marker(
      color ='rgb(171,202,244)'),
)
trace2 = Scatter(
    x=years,
    y=cost,
    name='Cost',
    marker=Marker(
        color= 'rgb(248,95,0)'), 
    yaxis='y2'
)

data = Data([trace1, trace2])
layout = Layout(
    title='Pomona Water Usage',
    xaxis=XAxis(
        title=""
    ),
    yaxis=YAxis(
        title='Water Usage - gallons'
    ),
    yaxis2=YAxis(
        title='Cost - $',
        overlaying='y',
        side='right'
    )     
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='water_2')
py.image.save_as(fig, 'pomona_water.png')
