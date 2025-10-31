import pytest
from airtools import run_pysplit as runps

def test_Inputs(tmp_path,):
    with pytest.raises(ValueError):
        """ # is the format correct, namely: YYYY-MM-DD HH:MM:SS? """
        runps.Inputs(lat=90, lon=90, height= 25, start_datetime="31-10-2025 17:00:00", duration = 240, hysplit_working='str', hysplit_exec='str',
                   meteo_dir= str(tmp_path / "meteo"), output_dir='str', basename='str')
        
    with pytest.raises(ValueError):
        """# fail if the dir doesn't exist """
        runps.Inputs(lat=90, lon=90, height= 25, start_datetime="2025-10-31 17:00:00", duration = 240, hysplit_working='str', hysplit_exec='str',
                   meteo_dir= 'directory_does_not_exist', output_dir='str', basename='str')
        
    with pytest.raises(ValueError):
        """# fail if the meteodir is empty"""
        runps.Inputs(lat=90, lon=90, height= 25, start_datetime="2025-10-31 17:00:00", duration = 240, hysplit_working='str', hysplit_exec='str',
                   meteo_dir= str(tmp_path / "empty_dir"), output_dir='str', basename='str')
        
    with pytest.raises(TypeError):
        """#is start date time a string?"""
        runps.Inputs(lat=90, lon=90, height= 25, start_datetime=20240531, duration = 240, hysplit_working='str', hysplit_exec='str',
                   meteo_dir= str(tmp_path / "meteo"), output_dir='str', basename='str')