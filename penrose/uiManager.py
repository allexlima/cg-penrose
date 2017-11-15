from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialogButtonBox
from penrose.gui.mainwindow_ui import Ui_MainWindow
from penrose.uiPlots import PlotCanvas
from penrose.uiVertices import VerticesWindow
from penrose.uiAbout import AboutWindow
import string
import webbrowser
import penrose.funcsPolygon as fPolygon
import penrose.funcsLine as fLine
from functools import partial


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.vertices = []
		self.graphs = None
		self.vertices_dialog = VerticesWindow()
		self.about_dialog = AboutWindow()
		self.actions()
		self.init_canvas()

	def init_canvas(self):
		self.graphs = [PlotCanvas(self) for _ in range(2)]
		self.graphs[0].move(355 + 30, 100)
		self.graphs[1].move(355 + 333, 100)

	def actions(self):
		self.actionOpen_file.setEnabled(False)
		self.actionSave.setEnabled(False)
		self.actionClear.setEnabled(False)
		self.actionCompile.setEnabled(False)
		self.popVertice.setEnabled(False)
		self.menuRasterize_with.setEnabled(False)
		#
		self.actionCompile.triggered.connect(self.render_polygon)
		self.actionUpdate.triggered.connect(self.transforms_2d)
		self.actionClear.triggered.connect(self.clear_all)
		self.actionGithub_repository.triggered.connect(self.github)
		self.actionAbout_this_software.triggered.connect(self.about_dialog.exec_)
		self.actionExit.triggered.connect(self.close)
		#
		self.actionSimpleLineAlgorithm.triggered.connect(partial(self.rasterize_lines, 0))
		self.actionBasicIncrementalAlgorithm.triggered.connect(partial(self.rasterize_lines, 1))
		self.actionBresenhamAlgorithm.triggered.connect(partial(self.rasterize_lines, 2))
		#
		self.actionExLine01.triggered.connect(partial(self.examples, 0))
		self.actionExLine02.triggered.connect(partial(self.examples, 1))
		self.actionExLine03.triggered.connect(partial(self.examples, 2))
		self.actionExTriangle.triggered.connect(partial(self.examples, 3))
		self.actionExSquare.triggered.connect(partial(self.examples, 4))
		self.actionExPentagon.triggered.connect(partial(self.examples, 5))
		self.actionExHexagon.triggered.connect(partial(self.examples, 6))
		#
		self.pushVertice.clicked.connect(self.vertices_dialog.exec_)
		self.popVertice.clicked.connect(self.remove_vertex)
		self.vertices_dialog.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.insert_vertex)
		self.about_dialog.commandLinkButton.clicked.connect(self.github)
		#
		self.boxScale.toggled.connect(self.scale_point.setEnabled, True)
		self.boxRotation.toggled.connect(self.rotation_vertices.setEnabled, True)
		self.boxRotation.toggled.connect(self.rotation_direction.setEnabled, True)

	def update_table(self):
		contents = [()] if len(self.vertices) is 0 else self.vertices
		self.tableVertices.setModel(TableModel(self, contents, ["Label", "X", "Y"]))
		self.tableVertices.setColumnWidth(0, 158)

	def insert_vertex(self, x=None, y=None):
		self.vertices_dialog.vertice_x.setFocus()
		if not x and not y:
			x, y = float(self.vertices_dialog.vertice_x.value()), float(self.vertices_dialog.vertice_y.value())
		label = list(string.ascii_uppercase)[len(self.vertices)]
		self.vertices.append((label, x, y))

		if not self.helpText.isHidden():
			self.helpText.hide()
		self.vertices_dialog.vertice_x.setValue(0)
		self.vertices_dialog.vertice_y.setValue(0)
		self.popVertice.setEnabled(True if len(self.vertices) > 0 else False)
		self.update_table()

		if len(self.vertices) == 2:
			self.menuRasterize_with.setEnabled(True)
		if len(self.vertices) >= 3:
			self.menuRasterize_with.setEnabled(False)
			self.actionClear.setEnabled(True)
			self.actionCompile.setEnabled(True)
		if len(self.vertices) > 8:
			self.alert("You can only enter up to 8 vertices", "Maximum amount of vertices")
			self.remove_vertex()

	def remove_vertex(self):
		self.vertices.pop()
		self.update_table()

		if len(self.vertices) < 3:
			self.actionCompile.setEnabled(False)
			self.actionClear.setEnabled(False)
		if len(self.vertices) == 0:
			self.helpText.show()
			self.clear_all()

	def examples(self, index):
		self.clear_all()
		vertices = [
			[(1, 5), (5, 0)],  # line 01
			[(2, 6), (6, 1)],  # line 02
			[(1, 0), (5, 2)],  # line 03
			[(5, 4), (1, 4), (5, 0)],  # triangle
			[(-4, 6), (-1, 6), (-1, 3), (-4, 3)],  # square
			[],
			[]
		]
		for point in vertices[index]:
			self.insert_vertex(*point)

	def clear_all(self):
		self.vertices = []
		self.update_table()
		self.helpText.show()
		self.graphs[0].plot("Initial polygon", None)
		self.graphs[1].plot("Final polygon", None)
		self.actionClear.setEnabled(False)
		self.actionCompile.setEnabled(False)
		self.popVertice.setEnabled(False)
		self.menuRasterize_with.setEnabled(False)
		self.boxTranslation.setChecked(False)
		self.boxShearing.setChecked(False)
		self.boxScale.setChecked(False)
		self.boxRotation.setChecked(False)
		self.boxReflection.setChecked(False)
		self.reflection_x.setChecked(False)
		self.reflection_y.setChecked(False)
		self.translation_tx.setValue(0)
		self.translation_ty.setValue(0)
		self.shear_cx.setValue(0)
		self.shear_cy.setValue(0)
		self.scale_sx.setValue(0)
		self.scale_sy.setValue(0)
		self.rotation_angle.setValue(0)
		self.rotation_angle.setValue(0)

	def render_polygon(self):
		self.graphs[0].plot("Initial Polygon", self.vertices)
		self.actionCompile.setEnabled(False)
		self.actionUpdate.setEnabled(True)
		self.init_comboboxs()

	def rasterize_lines(self, algorithm):
		self.graphs[0].matrix("Initial Points", self.vertices)
		if algorithm == 0:
			fLine.simple_line()
		elif algorithm == 1:
			fLine.basic_incremental()
		else:
			fLine.bresenham()
		self.menuRasterize_with.setEnabled(False)

	def init_comboboxs(self):
		self.scale_point.clear()
		self.rotation_vertices.clear()
		self.rotation_direction.clear()
		self.scale_point.addItems(["Origin"] + fPolygon.vertices_break(self.vertices)[0])
		self.rotation_vertices.addItems(["Origin"] + fPolygon.vertices_break(self.vertices)[0])
		self.rotation_direction.addItem("counter-clockwise")

	def transforms_2d(self):
		if not self.boxTranslation.isChecked() and not self.boxShearing.isChecked() and not self.boxScale.isChecked() \
					and not self.boxRotation.isChecked() and not self.boxReflection.isChecked():
			self.alert("You should select at least 1 transformation before", "No transformation selected", 3)
		else:
			
			if self.boxTranslation.isChecked():
				fPolygon.add_kernel(fPolygon.translation(self.translation_tx.value(), self.translation_ty.value()))
				
			if self.boxShearing.isChecked():
				fPolygon.add_kernel(fPolygon.shearing(self.shear_cx.value(), self.shear_cy.value()))
				
			if self.boxScale.isChecked():
				xp, yp = fPolygon.reference_point(self.vertices, self.scale_point.currentIndex())
				fPolygon.add_kernel(fPolygon.scaling(xp, yp, self.scale_sx.value(), self.scale_sy.value()))
				
			if self.boxRotation.isChecked():
				xp, yp = fPolygon.reference_point(self.vertices, self.rotation_vertices.currentIndex())
				fPolygon.add_kernel(fPolygon.rotation(xp, yp, self.rotation_angle.value()))
				
			if self.boxReflection.isChecked():
				if self.reflection_x.isChecked():
					fPolygon.add_kernel(fPolygon.reflection_x())
				if self.reflection_y.isChecked():
					fPolygon.add_kernel(fPolygon.reflection_y)
					
			new_vertices = fPolygon.transformation_2d(fPolygon.vertices_break(self.vertices)[-1])
			new_vertices = fPolygon.vertices_join(fPolygon.vertices_break(self.vertices)[0], new_vertices)
			self.graphs[1].plot("Final Polygon", new_vertices)

	def alert(self, text, title="Alert", code=2):
		message = QMessageBox(self)
		message.setIcon(code)
		message.setText(text)
		message.setWindowTitle(title)
		message.setWindowModality(Qt.ApplicationModal)
		message.exec_()

	@staticmethod
	def github():
		webbrowser.open("https://github.com/allexlima/cg-penrose")


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
