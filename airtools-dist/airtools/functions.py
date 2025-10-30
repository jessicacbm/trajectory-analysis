#functions used in calcu.ipynb
import numpy as np
from math import *

def haversine(lat1, lat2, lon1, lon2):
    #convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    #haversine formula
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    base = c * r
    return base


def mean_rainfall(data):
    return np.mean(data)

# def boundarylayer_position(bl_height, altitude):
#     if altitude > bl_height:
#         BLP = BLP + 1
#     elif altitude < bl_height:
#         BLP = BLP