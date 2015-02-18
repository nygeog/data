
# coding: utf-8

# In[12]:

import pandas as pd

#csv_path = 'https://raw.githubusercontent.com/nygeog/data/master/nyc_crashes/data/NYPD_Motor_Vehicle_Collisions.csv'
inCSV = 'data/NYPD_Motor_Vehicle_Collisions.csv'
ouCSV = 'data/nypd_mv_collisions.csv'

df = pd.read_csv(inCSV).rename(columns=lambda x: x.lower())

#drop ones w/out valid lat #super lazy, just grabbing lat's above 35
df = df[(df.latitude > 35)]
#print df.dtypes 
print len(df.index)
df.head(5)


# In[13]:

#create datetime http://stackoverflow.com/questions/17978092/combine-date-and-time-columns-using-python-pandas
df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])


# In[14]:

df = df[['datetime','latitude','longitude']]
df = df[(df.datetime > '2014-01-01 00:00:01')] #query out only data from 2014 onward
df = df.sort('datetime')
df.to_csv(ouCSV,index=False)
print len(df.index)


# In[15]:

df.head(5)


# <iframe width='100%' height='520' frameborder='0' src='http://nygeog.cartodb.com/viz/8df5425a-b6ed-11e4-9539-0e4fddd5de28/embed_map' allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>
