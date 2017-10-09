from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialogButtonBox
from .gui.mainwindow_ui import Ui_MainWindow
from .uiPlots import PlotCanvas
from .uiVertices import VerticesWindow
import string
import numpy as np


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.graphs = None
		self.vertices_dialog = VerticesWindow()
		self.vertices = []
		self.vert_transform = []
		self.actions()
		self.init_canvas()

	def init_canvas(self):
		self.graphs = [PlotCanvas(self) for i in range(2)]
		self.graphs[0].move(380 + 30, 37 + 100)
		self.graphs[1].move(380 + 325, 37 + 100)

	def set_polygon(self, points1=None, points2=None):
		self.graphs[0].plot("Initial polygon", points1)
		self.graphs[1].plot("Final polygon", points2)

	def actions(self):
		self.actionOpen_file.setEnabled(False)
		self.actionSave.setEnabled(False)
		self.actionClear.setEnabled(False)
		self.actionCompile.setEnabled(False)
		self.popVertice.setEnabled(False)
		self.actionExit.triggered.connect(self.close)
		self.pushVertice.clicked.connect(self.vertices_dialog.exec_)
		self.popVertice.clicked.connect(self.remove_vertive)
		self.vertices_dialog.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.insert_vertice)
		self.actionCompile.triggered.connect(self.render_polygon)
		self.actionClear.triggered.connect(self.clear_all)
		self.actionUpdate.triggered.connect(self.transforms_2d)

	def __create_table(self):
		contents = [()] if len(self.vertices) is 0 else self.vertices
		self.tableVertices.setModel(TableModel(self, contents, ["Label", "X", "Y"]))
		self.tableVertices.setColumnWidth(0, 158)

	def insert_vertice(self):
		self.vertices_dialog.vertice_x.setFocus()
		self.helpText.hide() if self.helpText.isHidden() is False else None
		x, y = float(self.vertices_dialog.vertice_x.value()), float(self.vertices_dialog.vertice_y.value())
		label = list(string.ascii_uppercase)[len(self.vertices)]
		self.vertices.append((label, x, y))
		self.__create_table()
		#
		self.vertices_dialog.vertice_x.setValue(0)
		self.vertices_dialog.vertice_y.setValue(0)
		self.popVertice.setEnabled(True) if len(self.vertices) > 0 else self.popVertice.setEnabled(False)
		if len(self.vertices) >= 3:
			self.actionClear.setEnabled(True)
			self.actionCompile.setEnabled(True)
		if len(self.vertices) > 8:
			self.alert("You can only enter up to 8 vertices", "Maximum amount of vertices")
			self.remove_vertive()

	def remove_vertive(self):
		self.vertices.pop()
		self.__create_table()
		if len(self.vertices) < 3:
			self.actionCompile.setEnabled(False)
			self.actionClear.setEnabled(False)
		if len(self.vertices) == 0:
			self.helpText.show()
			self.clear_all()

	def clear_all(self):
		self.vertices = []
		self.__create_table()
		self.helpText.show()
		self.popVertice.setEnabled(False)
		self.actionUpdate.setEnabled(False)
		self.set_polygon()

	def render_polygon(self):
		self.set_polygon(points1=self.vertices)
		self.actionCompile.setEnabled(False)
		self.actionUpdate.setEnabled(True)

	def transforms_2d(self):
		if not self.boxTranslation.isChecked() and not self.boxShearing.isChecked() and not self.boxScale.isChecked() \
					and not self.boxRotation.isChecked() and not self.boxReflection.isChecked():
			self.alert("You should select at least 1 transformation before", "No transformation selected", 3)
		else:
			matrices = []

			if self.boxTranslation.isChecked():
				matrices.append(np.array([
					[1, 0, self.translation_tx.value()],
					[0, 1, self.translation_ty.value()],
					[0, 0, 1]
				]))
			if self.boxShearing.isChecked():
				matrices.append(np.array([
					[1, self.shear_cx.value(), 0],
					[self.shear_cy.value(), 1, 0],
					[0, 0, 1]
				]))
			if self.boxScale.isChecked():
				matrices.append(np.array([
					[1, 0, 0],
					[0, 1, 0],
					[0, 0, 1]
				]))
			if self.boxRotation.isChecked():
				matrices.append(np.array([
					[1, 0, 0],
					[0, 1, 0],
					[0, 0, 1]
				]))
			if self.boxReflection.isChecked():
				matrices.append(np.array([
					[1, 0, 0],
					[0, 1, 0],
					[0, 0, 1]
				]))

			# calculate the transpose matrix of the vertices (after remove the labels in '__break_list')
			transpose = self.__break_list(self.vertices)[-1].transpose()

			# insert a row of ones in the transpose matrix's end, then insert the result in 'matrices' list
			matrices.append(np.append(transpose, [np.ones(len(transpose[0]))], axis=0))

			# multiply matrices into 'matrices' list,
			# remove the last row (of ones) and calculate the transpose matrix of the result
			multi_matrices = np.delete(np.linalg.multi_dot(matrices), 2, 0).transpose()
			# join the labels and vertices to generate a list of tuples like [(LABEL, X, Y),..]
			new_vertices = self.__join_list(self.__break_list(self.vertices)[0], multi_matrices)
			self.set_polygon(points1=self.vertices, points2=new_vertices)

	@staticmethod
	def __break_list(vertices):
		letters = [item[0] for item in vertices]
		points = np.array([item[1:] for item in vertices])
		return letters, points

	@staticmethod
	def __join_list(letters, points):
		points = [tuple(item) for item in points]
		return [((letters[index],) + value) for index, value in enumerate(points)]

	def alert(self, text, title="Alert", code=2):
		message = QMessageBox(self)
		message.setIcon(code)
		message.setText(text)
		message.setWindowTitle(title)
		message.setWindowModality(Qt.ApplicationModal)
		message.exec_()


class TableModel(QAbstractTableModel):
	def __init__(self, parent, my_list, header):
		QAbstractTableModel.__init__(self, parent)
		self.my_list = my_list
		self.header = header

	def rowCount(self, parent):
		return len(self.my_list)

	def columnCount(self, parent):
		return len(self.my_list[0])

	def data(self, index, role):
		if role == Qt.TextAlignmentRole:
			return Qt.AlignCenter
		return None if not index.isValid() or role != Qt.DisplayRole else self.my_list[index.row()][index.column()]

	def headerData(self, col, orientation, role):
		return self.header[col] if orientation == Qt.Horizontal and role == Qt.DisplayRole else None
