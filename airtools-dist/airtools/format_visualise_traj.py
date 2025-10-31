import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from pathlib import Path
import numpy as np
from math import *
from .functions import mean_rainfall, haversine

class ProcessTraj:
    """Functions for formatting trajectory output and calculating variables"""
    @staticmethod
    def format(filepath):
        df = pd.read_csv(filepath, skiprows=8, sep = r'\s+', 
                            names = ['hey','you','year','month','day','hour','go','away','time_step','lat', 'lon', 'alt', 
                                    'pressure','pot_temp', 'temp', 'precip', 'bl_height', 'rel_humid', 
                                    'spc_humid'])
        df=df.drop(labels=['hey','you','go','away'], axis=1)
        df.attrs["source"] = "Traj_output"
        return df
    
    @staticmethod
    def distance_travelled(traj_df):
        """function for calculating the distance the trajectory travelled"""
        dist_travel = 0
        for i in range(len(traj_df['lat'])):
            try:
                lat1 = traj_df['lat'].iloc[i]
                lat2 = traj_df['lat'].iloc[i+1]
                lon1 = traj_df['lon'].iloc[i]
                lon2 = traj_df['lon'].iloc[i+1]

                base_dist = haversine(lat1, lat2, lon1, lon2)
                dist_travel = dist_travel + base_dist

            except IndexError:
                print('all calculated')
                break
        print(f'The total distance travelled: {dist_travel} km')
        return dist_travel     

    @staticmethod
    def boundary_position(traj_df):
        """Function for calculating the percentage of time the air parcel was above the boundary layer"""

        traj_df['bl'] = (traj_df['alt'] > traj_df['bl_height']).astype(int)

        pcAboveBL = np.sum(traj_df['bl'])/len(traj_df['traj_id'])*100

        print(f'The air parcel is above the boundary layer {pcAboveBL}% of the time')

        return pcAboveBL
    
    @staticmethod
    def rainfall_stats(traj_df):
        acc_rainfall = 0
        rainfall_values = []
        for i in range(len(traj_df['lat'])):
            rain = traj_df['precip'].iloc[i]
            rainfall_values.append(rain)
            acc_rainfall = acc_rainfall + rain
        average_rainfall = mean_rainfall(rainfall_values)
        print(f' The total rainfall experienced by this air parcel is {acc_rainfall} mm')
        print(f' The average rainfall experienced by this air parcel is {average_rainfall}  mm/hr')
        return rainfall_values, average_rainfall

class Traj(ProcessTraj):
    """
    Class trajectory HYSPLIT output, and a method for visualising output.
    Parameters: filepath, a path to the file that HYSPLIT directly outputs
    """
    def __init__(self, filepath):
        self.filepath = filepath
        if not isinstance(self.filepath, str):
            raise TypeError("File path must be a string")
        if not os.path.exists(self.filepath):
            raise ValueError("Path to trajectory file does not exist")
        
    def show(self):
        print(ProcessTraj.format(self.filepath))
        
    def plot_traj(self, title, var, extent):
        """Function for visualising trajectory output"""
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        
        traj_df = ProcessTraj.format(self.filepath)

        fig, ax = plt.subplots(figsize=(10,6), subplot_kw={'projection': ccrs.PlateCarree()})

        ax.set_extent(extent)
        plot = ax.scatter(traj_df['lon'], traj_df['lat'], transform = ccrs.PlateCarree(), s=12, 
                   c=traj_df[var], cmap='plasma')
        
        ax.set_title(title)
        ax.coastlines()
        ax.stock_img()
        cbar = plt.colorbar(plot, ax=ax)
        cbar.set_label(var)

        plt.savefig(title+".png")

    def distance_travelled(self):
        """function for calculating the distance the trajectory travelled"""
        traj_df = ProcessTraj.format(self.filepath)

        return ProcessTraj.distance_travelled(traj_df)
        
    def boundary_position(self):
        """Function for calculating the percentage of time the air parcel was above the boundary layer"""
        traj_df = ProcessTraj.format(self.filepath)

        return ProcessTraj.boundary_position(traj_df)

    def rainfall_stats(self):
        """Function for calculating average and cumulative rainfall along the trajectory"""
        traj_df = ProcessTraj.format(self.filepath)
        return ProcessTraj.rainfall_stats(traj_df)






        





