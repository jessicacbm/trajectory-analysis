import format_visualise_traj as pkg

traj = pkg.Traj("/home/jessicbm/trajectory-analysis/.gitignore/example_traj_file.txt")
plot = traj.plot_traj("traj plot", "precip", extent=[-80, -60, 35, 50])