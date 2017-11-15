import numpy as np
from math import cos, sin, radians

KERNELS = []


def translation(tx, ty):
	return np.array([
		[1, 0, tx],
		[0, 1, ty],
		[0, 0, 1]
	])


def shearing(cx, cy):
	return np.array([
		[1, cx, 0],
		[cy, 1, 0],
		[0, 0, 1]
	])


def scaling(xp, yp, sx, sy):
	return np.array([
		[sx, 0, ((-xp * sx) + xp)],
		[0, sy, ((-yp * sy) + yp)],
		[0, 0, 1]
	])


def rotation(xp, yp, angle):
	theta = radians(angle)
	return np.array([
		[cos(theta), -sin(theta), (-xp * cos(theta)) + (yp * sin(theta)) + xp],
		[sin(theta), cos(theta), (-xp * sin(theta)) - (yp * cos(theta)) + yp],
		[0, 0, 1]
	])


def reflection_x():
	return np.array([
		[1, 0, 0],
		[0, -1, 0],
		[0, 0, 1]
	])


def reflection_y():
	return np.array([
		[-1, 0, 0],
		[0, 1, 0],
		[0, 0, 1]
	])


def add_kernel(kernel):
	KERNELS.append(kernel)


def transformation_2d(vertices, kernels=KERNELS):
	"""
	Returns a copy of vertices with the 2D transformations that are in KERNELS
	"""
	# calculate the transpose matrix of vertices
	transpose = vertices.transpose()
	# insert a row of ones in the transpose matrix's end, then insert the result in 'matrices' list
	kernels.append(np.append(transpose, [np.ones(len(transpose[0]))], axis=0))
	# multiply matrices into 'kernels' list,
	# remove the last row (of ones) and calculate the transpose matrix of the result
	final_transformation_result = np.delete(np.linalg.multi_dot(kernels), 2, 0).transpose()
	KERNELS.clear()
	return final_transformation_result


def vertices_break(vertices):
	"""
	This function separates each point labels from vertices (x, y).
	In other words, given one or more A(x, y) points this function returns two lists like ["A"] and [[x, y]].
	The first contains only labels while the second one has the (x, y) points
	"""
	labels = [item[0] for item in vertices]
	points = np.array([item[1:] for item in vertices])
	return labels, points


def vertices_join(labels, points):
	"""
	This function opposite of break_list(). Instead of to separate labels from points, this function joins them back.
	"""
	points = [tuple(item) for item in points]
	return [((labels[index],) + value) for index, value in enumerate(points)]


def reference_point(vertices, index):
	"""
	This function returns the vertex (X, Y) from VERTICES through index value
	"""
	v = tuple(vertices_break(vertices)[-1][index-1])
	return (0, 0) if index == 0 else (v[0], v[1])
