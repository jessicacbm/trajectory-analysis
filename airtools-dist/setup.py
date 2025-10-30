from setuptools import setup, find_packages

setup(name='airtools',
      version='0.1',
      description='A package to analyse air parcel trajectories',
      author='Jessica Matthew, Phoebe Sloper, Bente Vissel',
      packages=['airtools'],
      install_requires = ["numpy>=1.19,<2.0",
                          "matplotlib>=3.1,<4.0",
                          "basemap>=1.2.2",
                          "geopandas>=0.8,<1.0",
                          "cartopy>=0.18,<0.23",
                          "pysplit>=0.3.3,<1.0"],
      python_requires=">=3.7, <3.8",
      license='GPLv3')