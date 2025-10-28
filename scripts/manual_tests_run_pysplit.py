import run_pysplit as funcs
from datetime import datetime

traj_inputs = funcs.Inputs(90, 90, 25, "2006-04-30 15:00:00", -168,
             "/home/jessicbm/hysplit/hysplit.v5.4.2_UbuntuOS20.04.6LTS_public/working",
             "/home/jessicbm/hysplit/hysplit.v5.4.2_UbuntuOS20.04.6LTS_public/exec/hyts_std",
             "/home/jessicbm/weather_data",
             "/home/jessicbm/hysplit_outputs", "test_run")

traj = funcs.Trajectory(traj_inputs)
traj.generate_traj()