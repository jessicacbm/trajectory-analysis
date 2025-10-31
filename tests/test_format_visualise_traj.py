import airtools.format_visualise_traj as visual
import pytest
import numpy as np

def test_Traj():
    with pytest.raises(ValueError):
        visual.Traj("this_is_not_a_file_path")

    with pytest.raises(TypeError):
        visual.Traj(240)

def test_format():
    traj = visual.Traj("/home/jessicbm/trajectory-analysis/.gitignore/example_traj_file.txt")
    df = traj.format()
    assert df.columns.tolist() == ['year','month','day','hour','time_step','lat', 'lon', 'alt', 
                                    'pressure','pot_temp', 'temp', 'precip', 'bl_height', 'rel_humid', 
                                    'spc_humid']
    assert df.lat.loc[0] == 42.820
    assert df.spc_humid.loc[0] == 11.4
    assert df.year.loc[0] == 12
    