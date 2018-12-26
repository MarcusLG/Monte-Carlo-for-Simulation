import numpy as np
import math
import random
import time
import sys

def estimator(radius, radial_density, mc_points):
	simu_density = radial_density * radius
	origin_point =  np.array([simu_density + 1, simu_density + 1, simu_density + 1])
	# Full-simulation of spherical volume
	mc_volume = 0
	fs_volume = 0
	fs_start = time.time()
	fs_unit_count = 0
	fs_total_unit = pow((2 * simu_density) + 1, 3)
	for i in range(0, (2 * simu_density) + 1):
		for j in range(0, (2 * simu_density) + 1):
			for k in range(0, (2 * simu_density) + 1):
				fs_unit_count += 1
				x_diff = i - origin_point[0]
				y_diff = j - origin_point[1]
				z_diff = k - origin_point[2]
				mc_rad = math.sqrt(pow(x_diff,2) + pow(y_diff,2) + pow(z_diff,2))
				mc_rad = mc_rad * radius / simu_density
				mc_rad = int(math.floor(mc_rad))
				if mc_rad < radius:
					fs_volume += 1
				if (fs_unit_count % 10000) == 0:
					print("Progress: " + str(fs_unit_count * 100 / fs_total_unit) + "%.")

	fs_stop = time.time()
    # Normalize fs volume
	fs_volume = fs_volume * pow(radius,3) / pow(simu_density,3)
	print("Full-simulation estimator gives: " + str(fs_volume) + ".\n")
	pi = 3.1415926535
	true_volume = (4/3) * pi * (pow(radius,3))
	print("The true value is: " + str(true_volume) + ".")
	percentage_diff_fs = abs(fs_volume-true_volume) * 100 / true_volume
	print("The percentage difference is: " + str(percentage_diff_fs) + "%.\n")
	print("Time elapsed: " + str(fs_stop - fs_start) + "secs.\n")
	#Monte-carlo estimator
	estimator_point = []
	mc_count = 0
	mc_start = time.time()
	for i in range(0, mc_points):
		estimator_point.append([random.randint(0,((simu_density * 2) + 1 )) for _ in range(3)])
	for element in estimator_point:
		x_diff = element[0] - origin_point[0]
		y_diff = element[1] - origin_point[1]
		z_diff = element[2] - origin_point[2]
		mc_rad = math.sqrt(pow(x_diff,2) + pow(y_diff,2) + pow(z_diff,2))
		mc_rad = mc_rad * radius / simu_density
		mc_rad = int(math.floor(mc_rad))
		if mc_rad < radius:
			mc_count += 1
	mc_volume = mc_count / mc_points #non-normalized volume
	mc_volume = mc_volume * pow(2*radius, 3)
	mc_stop = time.time()
	print("The Monte-carlo volume is: " + str(mc_volume) + ".")
	percentage_diff_mc = abs(mc_volume - true_volume) * 100 / true_volume
	print("The percentage difference is: " + str(percentage_diff_mc) + "%.\n")
	print("Time elapsed: " + str(mc_stop - mc_start) + "sec(s).\n")

	#Analysis
	print("Difference between Monte-carlo method and Full-simulation in percentage error: \n" + str(percentage_diff_mc - percentage_diff_fs) + "." )
	print("Difference in time elapsed (Monte-carlo over Full-simulation): \n" + str((mc_stop - mc_start) - (fs_stop - fs_start)) + "sec(s).")


radius = int(input("Radius of sphere (Integer): "))
radial_density = int(input("Simulation density(Integer, simulation point / unit of space): "))
mc_points = int(input("Number of points of estimations: "))
estimator(radius, radial_density, mc_points)