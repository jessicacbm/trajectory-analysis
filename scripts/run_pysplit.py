import pysplit
from datetime import datetime
import os
import pandas as pd

class Inputs:
    def __init__(self, lat, lon, height, start_datetime: str, duration: int, hysplit_working: str, 
                 hysplit_exec: str, meteo_dir: str, output_dir: str, basename: str):
        """
        Inputs to run trajectory model on.
        Parameters:
        - lat, lon: starting (geographic) coorinates
        - height: starting altitude, m
        - start_time: trajectory launch time, YYYY-MM-DD HH:MM:SS
        - duration: how long to run trajectory for, hours, negative indicates backwards trajectory
        - meteo_dir: directory where meteorological data is stored
        - output_dir: directory to place output from hysplit
        """
        if not isinstance(start_datetime, str):
            raise TypeError("start_datetime must be a string in format YYYY-MM-DD HH:MM:SS")
        
        try:
            self.start_datetime = datetime.strptime(start_datetime, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("Trajectory start datetime must be in the format 'YYYY-MM-DD HH:MM:SS' ")
        
        self.lat = lat
        self.lon = lon
        self.height = height
        self.duration = duration
        self.meteo_dir = meteo_dir
        self.output_dir = output_dir
        self.basename = basename
        self.hysplit_working = hysplit_working
        self.hysplit_exec = hysplit_exec

        if not os.path.isdir(self.meteo_dir):
            raise ValueError("Meteorological data directory does not exist")
        
        if len(os.listdir(self.meteo_dir)) == 0:
            raise ValueError("Meteorological data directory is empty")

    def __str__(self):
        return f"lat: {self.lat}, lon: {self.lon}, height: {self.height} m, start time: {self.start_time}"

class GenTraj:
    """Generating a single trajectory using PYSPLIT package, outputting 2-D csv file"""
    def __init__(self, inputs: Inputs):
        if not isinstance(inputs, Inputs):
            raise TypeError("Inputs must be pre-defined using inputs = Inputs(lat, lon, height, ....)")
        self.inputs = inputs

    def generate_traj(self):
        """Will generate single HYSPLIT trajectory and output file in specified output_dir"""
        basename = self.inputs.basename
        hysplit_working = self.inputs.hysplit_working
        output_dir = self.inputs.output_dir
        meteo_dir = self.inputs.meteo_dir
        years = [self.inputs.start_datetime.year]
        months = [self.inputs.start_datetime.month]
        hours = [self.inputs.start_datetime.hour]
        altitudes = [self.inputs.height]
        coordinates = (self.inputs.lat, self.inputs.lon)
        run = self.inputs.duration
        monthslicer = slice(self.inputs.start_datetime.day-1, self.inputs.start_datetime.day, 1)
        #inputs related to directories (user must have necessary files for this to work)
        hysplit_exec = self.inputs.hysplit_exec
        #call pysplit and generate trajectory
        pysplit.generate_bulktraj(basename, hysplit_working, output_dir, meteo_dir, years,
                      months, hours, altitudes, coordinates, run,
                      meteoyr_2digits=True, outputyr_2digits=False,
                      monthslice=monthslicer, meteo_bookends=([4,5], [1]),
                      get_reverse=False, get_clipped=False,
                      hysplit=hysplit_exec)


            



        




    
