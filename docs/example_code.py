import airtools.format_visualise_traj as pkg

traj = pkg.Traj('/home/jessicbm/trajectory-analysis/docs/example_traj_file.txt')

traj.plot_traj("test", "pressure", extent=[-180,180,-90,90])

traj.show()

traj.distance_travelled()

traj.boundary_position()

traj.rainfall_stats()