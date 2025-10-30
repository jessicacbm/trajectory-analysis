import pytest
import numpy as np
import pandas as pd
import numpy.testing as npt
from airtools.functions import mean_rainfall, haversine
from airtools.calcu import TrajectoryCalculations

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
    testTraj = TrajectoryCalculations('TryOut', datafile=testdf)

    testDistTravelled = testTraj.distance_travelled()

    #manually compute to create comparison data
    dist1 = haversine(52,55,45,43)
    dist2 = haversine(55,57,43,42)

    expectedDist = dist1 + dist2

    npt.assert_equal(testDistTravelled, expectedDist)

def test_boundary_position():
    '''
    This test assesses whether the percentage of time spent by the air parcel
    above the boundary layer is correctly calculated.
    
    '''
    testdf = pd.DataFrame({
        "traj_id": [1,1,1,1],
        "alt":[450,550,650,750],
        "mixdepth":[500,600,600,700]
    })


    testTraj2 = TrajectoryCalculations("TryOut2", datafile=testdf)
    testTraj2.filepath = "dummy.csv"  # prevent CSV write crash

    TestBoundPos = testTraj2.boundary_position()

    expected_flags = [0, 0, 1, 1]
    expected_pct = (2/4) * 100

    #first test to check that boundary results are correct
    assert list(testTraj2.datafile["bounlaypos"]) == expected_flags
    
    #then assert the percentage is the same
    npt.assert_equal(TestBoundPos, expected_pct)
    







