import airtools.format_visualise_traj as visual
from airtools.functions import mean_rainfall, haversine
import pytest
import numpy as np
import pandas as pd
import numpy.testing as npt

# def test_format():
    #  traj = visual.Traj("~/trajectory-analysis/docs/example_traj_file.txt")
    #  df = traj.format()
    #  assert df.columns.tolist() == ['year','month','day','hour','time_step','lat', 'lon', 'alt', 
    #                                  'pressure','pot_temp', 'temp', 'precip', 'bl_height', 'rel_humid', 
    #                                  'spc_humid']
    #  assert df.lat.loc[0] == 42.820
    #  assert df.spc_humid.loc[0] == 11.4
    #  assert df.year.loc[0] == 12

def test_Traj():
    with pytest.raises(ValueError):
        visual.Traj("this_is_not_a_file_path")

    with pytest.raises(TypeError):
        visual.Traj(240)

# testing the rainfal function
@pytest.mark.parametrize(
        "test, expected",
        [
            ([1,2,3,4,5],3),
            ([0,0,1,0,0],0.2)
        ])

def test_mean_rainfall(test, expected):
    '''
    This test assesses whether the mean_rainfall () 
    accurately calculates the mean rainfall given an input.
    '''
    ## testing the rainfall mean function
    # test_input = [1, 2, 3, 4, 5]
    # test_result = 3

    #here you ask to see whether the arrays are equal,
    # comparing < daily_mean(test_intput) > to < test_result >
    npt.assert_equal(mean_rainfall(test), expected)

#testing the haversine formula
@pytest.mark.parametrize(
        "lat1, lat2, lon1, lon2, expected",
        [
            (52, 39, 4, 8, 1478.2), #netherlands to portugal
            (23, 21, 24, 86, 6347) #khutse game reserve to cancun
        ])
#currently set to round off to a specific set of decimals
def test_haversine(lat1, lat2, lon1, lon2, expected):
    '''
    This test assesses whether the haversine formula outputs a correct
    distance in kilometers.
    
    '''
    npt.assert_almost_equal(round(haversine(lat1, lat2, lon1, lon2), 1), round(expected, 1))

#could make the testdf into a pythong.mark.parametrize

def test_distance_travelled_func():
    '''
    This test assesses whether the distance travelled by an air parcel,
    independent of the amount of steps backwards there are in the analysis,
    is correctly calculated.
    '''
    # give input above
    # run the actual class function
    # check if the output is correct
    testdf = pd.DataFrame({
        "traj_id": [1,1,1],
        "lat":[52,55,57],
        "lon":[45,43,42]
    })

    #execute the class and its function

    pt =  visual.ProcessTraj()
    d = pt.distance_travelled(testdf)

    #manually compute to create comparison data
    dist1 = haversine(52,55,45,43)
    dist2 = haversine(55,57,43,42)

    expectedDist = dist1 + dist2

    npt.assert_equal(d, expectedDist)

def test_boundary_position():
    '''
    This test assesses whether the percentage of time spent by the air parcel
    above the boundary layer is correctly calculated.
    
    '''
    testdf = pd.DataFrame({
        "traj_id": [1,1,1,1],
        "alt":[450,550,650,750],
        "bl_height":[500,600,600,700]
    })

    pt = visual.ProcessTraj()
    bl = pt.boundary_position(testdf)

    # expected_flags = [0, 0, 1, 1]
    expected_pct = (2/4) * 100

    #first test to check that boundary results are correct
    # assert list(bl["bl"]) == expected_flags
    
    #then assert the percentage is the same
    npt.assert_equal(bl, expected_pct)
    
    