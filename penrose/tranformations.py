import numpy as np


def translation(tx, ty, vertices):
	# separa as letras (labels) dos pontos
	letters = [item[0] for item in vertices]
	points = np.array([item[1:] for item in vertices])
	# matriz de translação
	tmatrix = np.array([
		[1, 0, tx],
		[0, 1, ty],
		[0, 0, 1]
	])
	# adiciona uma linha de 1s no final da matriz transposta dos vértices
	aux = np.append(points.transpose(), [np.ones(3)], axis=0)
	# multiplica a matriz de translação com a 'aux' e remove a coluna de 1s, deixando só os pontos X, Y
	points = [tuple(item) for item in np.delete(np.dot(tmatrix, aux), 2, 0).transpose()]
	return [((letters[index], ) + value) for index, value in enumerate(points)]

test = [("A", 5, 4), ("B", 1, 4), ("C", 5, 0)]
print(translation(3, -7, test))
