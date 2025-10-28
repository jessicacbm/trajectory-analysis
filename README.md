# trajectory-analysis

In order to run the airflow trajectory generator, it is necessary to install HYSPLIT and the PySplit package.

First, create a virtual environment which runs on Python3.6 or 3.7, because Pysplit depends on that environment.

# Installing Hysplit

Highsplit can be downloaded using the following link: https://ready.arl.noaa.gov/HYSPLIT.php 

Place the HYSPLIT folder in the same directory as the folder you are working in/the virtual environment. 

# Pysplit

Pysplit can be installed in the virtual environment using 
```
pip install pysplit
```

# Installing the modules
The requirements file describes the specific versions needed to run pysplit. Run the following command to install the right ones.
```
pip install -r requirements.txt
```

# Data
The data has been obtained from https://www.ready.noaa.gov/data/archives/gdas1/

To install the data, filezilla can be used. Download the Filezilla (https://filezilla-project.org/) FileZilla client version.

Once installed, use as the host 'ftp.arl.noaa.gov'. Click QuickConnect. Select the directory in which you would like to store the files by inserting the path in the box 'Local site'. 

Navigate to the folder /archives/gdas1/. Here you can find the files in the set-up of gdas1.monthYEAR.week. Download the files by selecting the file and right-clicking to 'Download'.

The files that were installed for this project are:

* August 2012 weeks 1-4 (gdas1.aug12.wk1-wk4)
* August 2020 weeks 1-2 (gdas1.aug20.wk1-2)
* August 2025 weeks 1-4 (gdas1.aug25.wk1-4)

