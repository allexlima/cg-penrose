import numpy as np


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


def bresenham():
	print("Bresenham")


if __name__ == "__main__":
	points = np.array([
		[1, 5],
		[5, 0]
	])
	print(basic_incremental(points))
