import pysplit
from datetime import datetime #make sure you have pysplit in your virtual environment, pip install pysplit

class Inputs:
    def __init__(self, lat, lon, height, start_time, duration, hysplit_working, 
                 hysplit_exec, meteo_dir, output_dir, basename):
        """
        Inputs to run trajectory model on.
        Parameters:
        - lat, lon: starting (geographic) coorinates
        - height: starting altitude, m
        - start_time: trajectory launch time, string datetime format
        - duration: how long to run trajectory for, hours, negative indicates backwards trajectory
        - meteo_dir: directory where meteorological data is stored
        - output_dir: directory to place output from hysplit
        """
        self.lat = lat
        self.lon = lon
        self.height = height
        self.start_time = start_time
        self.duration = duration
        self.meteo_dir = meteo_dir
        self.output_dir = output_dir
        self.basename = basename
        self.hysplit_working = hysplit_working
        self.hysplit_exec = hysplit_exec

    def __str__(self):
        return f"lat: {self.lat}, lon: {self.lon}, height: {self.height} m, start time: {self.start_time}"

class Trajectory:
    """Generating a single trajectory using PYSPLIT package"""
    def __init__(self, inputs: Inputs):  #assumes inputs will be an instance of class Inputs
        self.inputs = inputs
    
    def generate_traj(self):
        #converting start time to datetime object
        start_time = datetime.strptime(self.inputs.start_time, "%Y-%M-%D %H:%M:%S")
        #spatial and temporal inputs
        coordinates = (self.inputs.lat, self.inputs.lon)
        altitudes = self.inputs.height
        years = start_time.year
        months = start_time.month
        hours = start_time.hour
        hours = start_time.hour
        monthslice = slice(start_time.day-1, start_time.day, 1)
        run = self.inputs.duration
        #inputs related to directories (user must have necessary files for this to work)
        hysplit_working = self.inputs.hysplit_working
        output_dir = self.inputs.output_dir
        meteo_dir = self.inputs.meteo_dir
        hysplit_exec = self.inputs.hysplit_exec
        #basename for outputfile
        basename = self.inputs.basename
        #call pysplit and generate trajectory
        pysplit.generate_bulktraj(basename, hysplit_working, output_dir, meteo_dir, years,
                      months, hours, altitudes, coordinates, run,
                      meteoyr_2digits=True, outputyr_2digits=False,
                      monthslice=slice(0, 32, 1), meteo_bookends=([4, 5], [1]),
                      get_reverse=False, get_clipped=False,
                      hysplit=hysplit_exec)


        




    
