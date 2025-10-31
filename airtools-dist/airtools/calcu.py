## Reformat the files and save them 
import pandas as pd
from pathlib import Path
import numpy as np
from math import *
from airtools.functions import mean_rainfall, haversine

class TrajectoryCalculations:
    def __init__(self, timestamp, datafile):
        self.timestamp = timestamp
        # define filepath as the same in case of wanting to overwrite the csv
        self.filepath = datafile
        #update this so it can read both CSVs and dfs
        if isinstance(datafile, str):
            self.datafile = pd.read_csv(datafile)
        else:
            # already a DataFrame
            self.datafile = datafile

    
    def distance_travelled(self):
        #access the 10th column for lat; [1] for first, [-1] for last
        dist_travel = 0
        for i in range(len(self.datafile['traj_id'])):
            try:
                lat1 = self.datafile['lat'].iloc[i]
                lat2 = self.datafile['lat'].iloc[i+1]
                lon1 = self.datafile['lon'].iloc[i]
                lon2 = self.datafile['lon'].iloc[i+1]
                # print(f'set{i}:{lat1},{lon1}')

                base_dist = haversine(lat1, lat2, lon1, lon2)
                # print(f'set{i}: base horizontal distance: {base}')
                dist_travel = dist_travel + base_dist
                # print(f' new total distance: {dist_travel}')

            except IndexError:
                print('all calculated')
                break
        print(f'The total distance travelled: {dist_travel} km')
        return dist_travel
    
    def boundary_position(self):
        boundlaypos = 0
        index = 0
        #create a new column indicating whether below or above boundary layer
        self.datafile['bounlaypos'] = pd.Series(dtype='int')
        for i in range(len(self.datafile['traj_id'])):
            #boundary layer height

            bl = self.datafile['mixdepth'].iloc[i]
            #altitude air parcel
            alt = self.datafile['alt'].iloc[i]
            # print(f'for set {1} the boundlay: {bl} and the alt: {alt} ')
            if alt < bl: #this means the air parcel is below the boundary layer
                boundlaypos = boundlaypos
                index= index+1
                self.datafile['bounlaypos'].iloc[i] = 0
                # print(f'nothing added to the boundlaypos: {boundlaypos}')
            elif alt > bl: #this means the air parcel is above the boundary layer
                boundlaypos = boundlaypos+1
                index = index+1
                self.datafile['bounlaypos'].iloc[i] = 1
                # print(f'added to the boundlaypos: {boundlaypos}')
        print(self.datafile['bounlaypos']) 
        #overwrite the original csv
        self.datafile.to_csv(self.filepath, index=False)   
        pcAboveBL = boundlaypos/index * 100
        print(f'The air parcel is above the boundary layer {pcAboveBL}% of the time')
        return pcAboveBL


    def rainfall_stats(self):
        acc_rainfall = 0
        rainfall_values = []
        for i in range(len(self.datafile['traj_id'])):
            rain = self.datafile['rainfall'].iloc[i]
            rainfall_values.append(rain)
            acc_rainfall = acc_rainfall + rain
        average_rainfall = mean_rainfall(rainfall_values)
        print(f' The total rainfall experienced by this air parcel is {acc_rainfall}')
        print(f' The average rainfall experienced by this air parcel is {average_rainfall}')
        return rainfall_values, average_rainfall

### TEST the functions ####
# #define the trajectory 
# firstTraj = TrajectoryCalculations('Aug20120801', '/home/bvissel/trajectory-analysis/trajectories/formatted_data/colgateaug0500summer2012080717.csv')

# #execute the methods
# DistTravel_Aug2012 = firstTraj.distance_travelled()
# print(DistTravel_Aug2012)

# BoundaryLayerMet = firstTraj.boundary_position()
# print(BoundaryLayerMet)

# RainfallStats = firstTraj.rainfall_stats()
# print(RainfallStats)
    

        
        
        


    






            
