#%%
# importing necessary libraries
import plotly.graph_objs as go
import plotly.offline as offline
#%%
#function takes the dataframe and target variable as arguments

def parallelcordinates(dataframe,target):

   df = dataframe
   col = df.columns
   
   attributes = []
   for i in col:
      x = dict(range = [df[i].min(),df[i].max()],label = i, values = df[i]) 
      attributes.append(x)
   
   
   data = [
       go.Parcoords(
          line = dict(color = target,
                     colorscale = 'Jet',
                     showscale = True,
                      cmin = target.min(),
                      cmax = target.max()),
           dimensions = attributes
       )
   ]
   
   layout = go.Layout(
       plot_bgcolor = '#E5E5E5',
       paper_bgcolor = '#E5E5E5'
   )
   
   fig = go.Figure(data = data, layout = layout)
   result = offline.plot(fig, filename = 'fromheatmap', auto_open=True)
   
   return result

#%%

import pandas as pd
dataframe = pd.read_excel("nonull.xlsx")
target = dataframe['fraud']
parallelcordinates(dataframe,target)


