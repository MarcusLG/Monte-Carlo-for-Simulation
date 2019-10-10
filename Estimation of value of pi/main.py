'''
Author: Marcus Guozong Lim
'''

import numpy as np
import math
import random

def check_within_circle(coord, radius):
	dist_to_origin = math.sqrt(coord[0] ** 2 + coord[1] ** 2)
	return dist_to_origin <= radius

# Declaration of parameters
NUM_ITER = 100000000

# Initialization of variables
total_points = 0
num_points_quad = 0

for i in range(NUM_ITER):
	coord = [random.random(), random.random()]
	total_points += 1
	if check_within_circle(coord, 1):
		num_points_quad += 1
	pi_estimate = (num_points_quad / total_points) * 4

	if i % 1000000 == 0:
		print("Iteration: " + str(i) + "\nPi: " + str(pi_estimate) )

print(pi_estimate)