import numpy as np
from bresenham import bresenham as bh_algorithm


def simple_line(vertices):
	(xa, ya, xb, yb) = tuple(np.abs(vertices).reshape(1, 4)[0])
	m = (yb - ya) / (xb - xa)
	b = ya - m*xa
	n_points = [(xa, ya)]
	while xa < xb:
		xa += 1
		y = m*xa + b
		n_points.append((xa, y))
	return np.array(n_points)


def basic_incremental(vertices):
	(xa, ya, xb, yb) = tuple(np.abs(vertices).reshape(1, 4)[0])
	m = (yb - ya) / (xb - xa)
	n_points = [(xa, ya)]
	while xa < xb:
		xa += 1
		ya += m
		n_points.append((xa, ya))
	return np.array(n_points)


def bresenham(vertices):
	return np.array(list(bh_algorithm(*tuple(np.uint8(np.abs(vertices)).reshape(1, 4)[0]))))

