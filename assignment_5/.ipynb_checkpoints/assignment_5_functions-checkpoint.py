#
#
from siphon.simplewebservice.iastate import IAStateUpperAir
from metpy.io import add_station_lat_lon
import datetime
import pandas

# get_raobs
# returns a pandas dataframe with RAOBs
# input = dt (a datetime object)

def get_raobs(dt: datetime.datetime) -> pandas.DataFrame:
    #collect the data
    data = IAStateUpperAir().request_all_data(dt)
    #add latitude and longitude data to the RAOBs
    data = add_station_lat_lon(data)
    return data

# select_press
def select_press(data: pandas.DataFrame, pressLvl) -> pandas.DataFrame:
    #use loc to grab rows where pressure equals requested pressure
    data = data.loc[data.pressure == pressLvl]
    
    return data





# returns a pandas dataframe with RAOB observations at the specified pressure level
# input = data (a RAOB pandas dataframe)
#       = press_lev (the pressure level requested in hPa)


