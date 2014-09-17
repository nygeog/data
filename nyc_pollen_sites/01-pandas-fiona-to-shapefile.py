import pandas as pd

io1 = '/Users/danielmsheehan/Dropbox/GIS/Data/Municipal/USA/New_York/New_York_City/Pollen/NYCPS_lat_long_2013.csv'
io2 = '/Users/danielmsheehan/Dropbox/GIS/Data/Municipal/USA/New_York/New_York_City/Pollen/NYCPS_lat_long_2013_w.csv'

df = pd.read_csv(io1)
df.to_csv(io2, index=False)

from shapely.geometry import Point, mapping
from fiona import collection
 
schema = { 'geometry': 'Point', 'properties': { 'SITEID': 'str' } }#{ 'city': 'str', 'zip': 'str' } }
#url = df #"http://goo.gl/WFylXY"
#data = pd.read_csv(url)
data = df
with collection("/Users/danielmsheehan/Dropbox/GIS/Data/Municipal/USA/New_York/New_York_City/Pollen/nyc_pollen_sites.shp", "w", "ESRI Shapefile", schema) as output:
    for index, row in data.iterrows():
        point = Point(row['Longitude'], row['Latitude'])
        output.write({
            'properties': {'SITEID': row['SITEID']},#{'city': row['city'], 'zip': row['zip_code']},
            'geometry': mapping(point)
        })
          