#Pysplit-test.py 
# Test script

# Prior to attempting trajectory generation with PySPLIT, the user should ensure
# that meteorology file names follow a format of '*mon*YY*#' or '*mon*YYYY*#' where:

# * '*' is a Bash-style wildcard
# * 'mon' is a three-letter lower-case abbreviation of the month
# * 'YY' or 'YYYY' is a two or four digit integer representation of the year 
# * '#' is the number of the file within the month

# For example, '*jan*07*2' will match files named 'gdas1.jan2007.w2' and
# 'edas.jan2007_2'.

# Import the package
import os
import pysplit

#Working directory
working_dir = "/home/bvissel/airflow/hysplit5.4/working/"
#location where it will be stored
storage_dir = "/home/bvissel/airflow-trajectories/trajectories/colgate/"
#data dir
meteo_dir = "/home/bvissel/airflow/data/"

#specify where hysplit is located
hysplit_executable = "/home/bvissel/airflow/hysplit5.4/exec/hyts_std"
# in order for this to work also need to enter in terminal: 
# ls -l /home/bvissel/airflow/hysplit5.4/exec/hyts_std
# chmod +x /home/bvissel/airflow/hysplit5.4/exec/hyts_std

os.makedirs(storage_dir, exist_ok=True)

#create a setup file
setup_cfg_path = os.path.join(working_dir, "SETUP.CFG")

#define which params you want
setup_content = """&SETUP
tm_tpot = 1,     ! Potential temperature
tm_tamb = 1,     ! Ambient temperature
tm_rain = 1,     ! Precipitation
tm_mixd = 1,     ! Mixing depth
tm_sphu = 1,     ! Specific humidity
tm_pres = 1,     ! Pressure
tm_relh = 1,     ! Relative humidity
/
"""

#create (overwrite) setup file
with open(setup_cfg_path, "w") as f:
    f.write(setup_content)

#confirm creation setup file
print(f"SETUP.CFG written to {setup_cfg_path}")

#basename
basename = 'colgate'


# Specify the arguments

years = [2012, 2020, 2025]
months = [8]
hours = [11, 17, 23]
altitudes = [500, 1000, 1500]
location = (42.82, -75.54)
#with a runtime of -120, it has to contain the july week before
runtime = -72


#run function

pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 2), get_reverse=True,
                          get_clipped=True, hysplit=hysplit_executable)