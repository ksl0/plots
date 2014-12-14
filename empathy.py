#!/urs/bin/env
# 
# program to model 
# supposedly start out with 100% knowledge

import plotly.plotly as py
from plotly.graph_objs import *
from secret import*
import numpy as np
from operator import add

total_knowledge = 94.5 
total_empathy = 10 
knowledge = [] 
action =[]  
noise1 = np.random.normal(0,4,20)
noise2 = np.random.normal(0,1,20)
for i in range(1,21): 
  knowledge.append(total_knowledge)
  action.append(total_empathy*0.70)
  total_empathy = 1.1*total_empathy
  total_knowledge -=   3

py.sign_in('jamn_chick', key)

years = range(2014,2034)
y_data = knowledge
y2 = action 

trace1 = Scatter(
    x=years,
    y= map(add,y_data, noise1), 
    name='Knowledge',
    marker=Marker(
      color ='rgb(16,63,173)'),
)
trace2 = Scatter(
    x=years,
    y=map(add,y2,noise2),
    name='Action',
    marker=Marker(
        color= 'rgb(246,10,44)'), 
    yaxis='y2'
)

data = Data([trace1, trace2])

layout = Layout(
    title='A 20 Year Model',
    xaxis=XAxis(
        title=""
    ),
    yaxis=YAxis(
        title='percentage of retention'
    ),
    yaxis2=YAxis(
        overlaying='y',
        side ='right'
    ) 
)

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='empathy')
py.image.save_as(fig, 'feels.png')
