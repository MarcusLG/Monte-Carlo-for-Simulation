# ESTIMATION OF THE VALUE OF PI
Quadrant of a circle can be used to estimate the value of pi using Monte-Carlo method.
This implementation uses a quadrant of circle with radius of 1 at origin (0, 0)

Area = pi * (r ** 2):
By estimating area of quadrant with A = 1 * (Num of points/ Total points),
the value of pi can be estimated with:
pi 	= Area / (r ** 2),
	= Area

Target value: pi = 3.1415926535

# How to use
The programme is entiredly contained within main.py, running main.py will start the iterations, default number of iterations: 100,000,000