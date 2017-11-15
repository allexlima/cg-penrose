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
	return np.array(n_points, dtype=np.uint8)


def basic_incremental():
	print("Basic Incremental")


def bresenham():
	print("Bresenham")


if __name__ == "__main__":
	points = np.array([
		[2, 6],
		[6, 1]
	])
	print(simple_line(points))
