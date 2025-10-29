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
        
#def test_Trajectory():
 #   inputs = pkg.Inputs(lat=90, lon=90, height= 25, start_datetime="2025-10-31 17:00:00", 
  #                      duration = 240, hysplit_working='str', hysplit_exec='str', 
   #                     meteo_dir= '/home/jessicbm/trajectory-analysis/scripts', 
    #                    output_dir='output_dir', basename='str')
 #   traj = pkg.Trajectory(inputs)
  #  assert traj.traj_loc == "output_dir/2025103117"

def test_Traj_output():
    with pytest.raises(ValueError):
        pkg.Traj_output("this_is_not_a_file_path")

def test_format_traj():
    traj_dum = pkg.Traj_output("/home/jessicbm/trajectory-analysis/.gitignore/example_traj_file.txt")
    traj = traj_dum.format_traj()
    assert traj.columns.tolist() == ['year','month','day','hour','time_step','lat', 'lon', 'alt', 
                                    'pressure','pot_temp', 'temp', 'precip', 'bl_height', 'rel_humid', 
                                    'spc_humid']
    assert traj.lat.loc[0] == 42.820
    assert traj.spc_humid.loc[0] == 11.4
    assert traj.year.loc[0] == 12