

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

    449644





<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>time</th>
      <th>borough</th>
      <th>zip code</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>location</th>
      <th>on street name</th>
      <th>cross street name</th>
      <th>off street name</th>
      <th>...</th>
      <th>contributing factor vehicle 2</th>
      <th>contributing factor vehicle 3</th>
      <th>contributing factor vehicle 4</th>
      <th>contributing factor vehicle 5</th>
      <th>unique key</th>
      <th>vehicle type code 1</th>
      <th>vehicle type code 2</th>
      <th>vehicle type code 3</th>
      <th>vehicle type code 4</th>
      <th>vehicle type code 5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td> 02/13/2015</td>
      <td> 21:45</td>
      <td>     MANHATTAN</td>
      <td> 10002</td>
      <td> 40.715622</td>
      <td>-73.994275</td>
      <td> (40.7156221, -73.9942752)</td>
      <td>     FORSYTH STREET</td>
      <td>   CANAL STREET</td>
      <td> NaN</td>
      <td>...</td>
      <td>             NaN</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> 3168577</td>
      <td> PASSENGER VEHICLE</td>
      <td>                       UNKNOWN</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 02/13/2015</td>
      <td> 21:45</td>
      <td>     MANHATTAN</td>
      <td> 10001</td>
      <td> 40.747535</td>
      <td>-73.988307</td>
      <td> (40.7475349, -73.9883068)</td>
      <td>     WEST 31 STREET</td>
      <td>       BROADWAY</td>
      <td> NaN</td>
      <td>...</td>
      <td> Fatigued/Drowsy</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> 3169163</td>
      <td>              TAXI</td>
      <td>                          TAXI</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 02/13/2015</td>
      <td> 21:45</td>
      <td>         BRONX</td>
      <td> 10462</td>
      <td> 40.833558</td>
      <td>-73.857732</td>
      <td> (40.8335582, -73.8577325)</td>
      <td> WESTCHESTER AVENUE</td>
      <td> PUGSLEY AVENUE</td>
      <td> NaN</td>
      <td>...</td>
      <td>     Unspecified</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> 3169251</td>
      <td> PASSENGER VEHICLE</td>
      <td> SPORT UTILITY / STATION WAGON</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 02/13/2015</td>
      <td> 21:44</td>
      <td>     MANHATTAN</td>
      <td> 10017</td>
      <td> 40.748800</td>
      <td>-73.969846</td>
      <td>  (40.7487997, -73.969846)</td>
      <td>     EAST 42 STREET</td>
      <td>       1 AVENUE</td>
      <td> NaN</td>
      <td>...</td>
      <td> Other Vehicular</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> 3169176</td>
      <td> PASSENGER VEHICLE</td>
      <td>             PASSENGER VEHICLE</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td> 02/13/2015</td>
      <td> 21:40</td>
      <td> STATEN ISLAND</td>
      <td> 10304</td>
      <td> 40.617295</td>
      <td>-74.080479</td>
      <td> (40.6172954, -74.0804791)</td>
      <td>   PARK HILL AVENUE</td>
      <td>  OSGOOD AVENUE</td>
      <td> NaN</td>
      <td>...</td>
      <td>     Unspecified</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> 3169614</td>
      <td> PASSENGER VEHICLE</td>
      <td>             PASSENGER VEHICLE</td>
      <td> NaN</td>
      <td> NaN</td>
      <td> NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 29 columns</p>
</div>




    #create datetime http://stackoverflow.com/questions/17978092/combine-date-and-time-columns-using-python-pandas
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])


    df = df[['datetime','latitude','longitude']]
    df = df[(df.datetime > '2014-01-01 00:00:01')] #query out only data from 2014 onward
    df = df.sort('datetime')
    df.to_csv(ouCSV,index=False)
    print len(df.index)

    192324



    df.head(5)




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>datetime</th>
      <th>latitude</th>
      <th>longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>228854</th>
      <td>2014-01-01 00:01:00</td>
      <td> 40.725432</td>
      <td>-73.996771</td>
    </tr>
    <tr>
      <th>228850</th>
      <td>2014-01-01 00:01:00</td>
      <td> 40.767889</td>
      <td>-73.981512</td>
    </tr>
    <tr>
      <th>228855</th>
      <td>2014-01-01 00:01:00</td>
      <td> 40.750844</td>
      <td>-73.978608</td>
    </tr>
    <tr>
      <th>229144</th>
      <td>2014-01-01 00:15:00</td>
      <td> 40.588646</td>
      <td>-73.992452</td>
    </tr>
    <tr>
      <th>228849</th>
      <td>2014-01-01 00:20:00</td>
      <td> 40.689019</td>
      <td>-73.986157</td>
    </tr>
  </tbody>
</table>
</div>



<iframe width='100%' height='520' frameborder='0'
src='http://nygeog.cartodb.com/viz/8df5425a-b6ed-
11e4-9539-0e4fddd5de28/embed_map' allowfullscreen webkitallowfullscreen
mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>
