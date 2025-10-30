import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

class Traj:
    """
    Class trajectory, methods for formatting and visualising hysplit output.
    Parameters: filename, a path to a single trajectory HYSPLIT output file. File should be generated using steps in README.md file and GenTraj.generate_traj() function.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        if not isinstance(self.filepath, str):
            raise TypeError("File path must be a string")
        if not os.path.exists(self.filepath):
            raise ValueError("Path to trajectory file does not exist")

    def format(self):
        """Function for formatting trajectory output"""
        header_row = pd.read_csv(self.filepath, nrows=8, header=None, sep=r'\s+')
        
        if 'pressure' not in header_row.iloc[7].values:
            raise ValueError(f"The file {self.filepath} does not contain 'pressure' in row 8.")
        
        df = pd.read_csv(self.filepath, skiprows=8, sep = r'\s+', 
                            names = ['hey','you','year','month','day','hour','go','away','time_step','lat', 'lon', 'alt', 
                                    'pressure','pot_temp', 'temp', 'precip', 'bl_height', 'rel_humid', 
                                    'spc_humid'])
        df=df.drop(labels=['hey','you','go','away'], axis=1)
        df.attrs["source"] = "Traj_output"
        return df

    def plot_traj(self, title, var, extent):
        """Function for visualising trajectory output"""
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        
        traj_df = self.format()
        
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




        





