import pytest
from datetime import datetime
from unittest.mock import MagicMock
import scripts.run_pysplit as pkg

def test_Inputs():
    with pytest.raises(ValueError):
        pkg.Inputs(lat=90, lon=90, height= 25, start_datetime="31-10-2025 17:00:00", duration = 240, hysplit_working='str', hysplit_exec='str',
                   meteo_dir= '"/home/jessicbm/trajectory-analysis/scripts"', output_dir='str', basename='str')
        
    with pytest.raises(ValueError):
        pkg.Inputs(lat=90, lon=90, height= 25, start_datetime="2025-10-31 17:00:00", duration = 240, hysplit_working='str', hysplit_exec='str',
                   meteo_dir= 'directory_does_not_exist', output_dir='str', basename='str')
        
    with pytest.raises(ValueError):
        pkg.Inputs(lat=90, lon=90, height= 25, start_datetime="2025-10-31 17:00:00", duration = 240, hysplit_working='str', hysplit_exec='str',
                   meteo_dir= '/home/jessicbm/trajectory-analysis/.gitignore/empty_dir', output_dir='str', basename='str')
        

def test_format_traj():
    print('hello world')