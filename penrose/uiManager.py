from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialogButtonBox
from penrose.gui.mainwindow_ui import Ui_MainWindow
from penrose.uiPlots import PlotCanvas
from penrose.uiVertices import VerticesWindow
from penrose.uiAbout import AboutWindow
import string
import webbrowser
import penrose.funcsPolygon as fPolygon


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.graphs = None
		self.vertices_dialog = VerticesWindow()
		self.about_dialog = AboutWindow()
		self.actions()
		self.init_canvas()

	def init_canvas(self):
		self.graphs = [PlotCanvas(self) for i in range(2)]
		self.graphs[0].move(355 + 30, 100)
		self.graphs[1].move(355 + 333, 100)

	def actions(self):
		self.actionOpen_file.setEnabled(False)
		self.actionSave.setEnabled(False)
		self.actionClear.setEnabled(False)
		self.actionCompile.setEnabled(False)
		self.popVertice.setEnabled(False)
		#
		self.actionCompile.triggered.connect(self.render_polygon)
		self.actionUpdate.triggered.connect(self.transforms_2d)
		self.actionClear.triggered.connect(self.clear_all)
		self.actionGithub_repository.triggered.connect(self.github)
		self.actionAbout_this_software.triggered.connect(self.about_dialog.exec_)
		self.actionExit.triggered.connect(self.close)
		#
		self.pushVertice.clicked.connect(self.vertices_dialog.exec_)
		self.popVertice.clicked.connect(self.remove_vertex)
		self.vertices_dialog.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.insert_vertice)
		self.about_dialog.commandLinkButton.clicked.connect(self.github)
		#
		self.boxScale.toggled.connect(self.scale_point.setEnabled, True)
		self.boxRotation.toggled.connect(self.rotation_vertices.setEnabled, True)
		self.boxRotation.toggled.connect(self.rotation_direction.setEnabled, True)

	def __create_table(self):
		contents = [()] if len(fPolygon.VERTICES) is 0 else fPolygon.VERTICES
		self.tableVertices.setModel(TableModel(self, contents, ["Label", "X", "Y"]))
		self.tableVertices.setColumnWidth(0, 158)

	def insert_vertice(self):
		self.vertices_dialog.vertice_x.setFocus()
		self.helpText.hide() if self.helpText.isHidden() is False else None
		x, y = float(self.vertices_dialog.vertice_x.value()), float(self.vertices_dialog.vertice_y.value())
		label = list(string.ascii_uppercase)[len(fPolygon.VERTICES)]
		fPolygon.VERTICES.append((label, x, y))
		self.__create_table()
		#
		self.vertices_dialog.vertice_x.setValue(0)
		self.vertices_dialog.vertice_y.setValue(0)
		self.popVertice.setEnabled(True) if len(fPolygon.VERTICES) > 0 else self.popVertice.setEnabled(False)
		if len(fPolygon.VERTICES) >= 3:
			self.actionClear.setEnabled(True)
			self.actionCompile.setEnabled(True)
		if len(fPolygon.VERTICES) > 8:
			self.alert("You can only enter up to 8 vertices", "Maximum amount of vertices")
			self.remove_vertex()

	def remove_vertex(self):
		fPolygon.VERTICES.pop()
		self.__create_table()
		if len(fPolygon.VERTICES) < 3:
			self.actionCompile.setEnabled(False)
			self.actionClear.setEnabled(False)
		if len(fPolygon.VERTICES) == 0:
			self.helpText.show()
			self.clear_all()

	def clear_all(self):
		fPolygon.VERTICES = []
		self.__create_table()
		self.helpText.show()
		self.graphs[0].plot("Initial polygon", None)
		self.graphs[1].plot("Final polygon", None)
		self.popVertice.setEnabled(False)
		self.actionUpdate.setEnabled(False)
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
		self.graphs[0].plot("Initial polygon", fPolygon.VERTICES)
		self.actionCompile.setEnabled(False)
		self.actionUpdate.setEnabled(True)
		self.init_comboboxs()

	def init_comboboxs(self):
		self.scale_point.clear()
		self.rotation_vertices.clear()
		self.rotation_direction.clear()
		self.scale_point.addItems(["Origin"] + fPolygon.vertices_break()[0])
		self.rotation_vertices.addItems(["Origin"] + fPolygon.vertices_break()[0])
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
				xp, yp = fPolygon.reference_point(self.scale_point.currentIndex())
				fPolygon.add_kernel(fPolygon.scaling(xp, yp, self.scale_sx.value(), self.scale_sy.value()))
				
			if self.boxRotation.isChecked():
				xp, yp = fPolygon.reference_point(self.rotation_vertices.currentIndex())
				fPolygon.add_kernel(fPolygon.rotation(xp, yp, self.rotation_angle.value()))
				
			if self.boxReflection.isChecked():
				if self.reflection_x.isChecked():
					fPolygon.add_kernel(fPolygon.reflection_x())
				if self.reflection_y.isChecked():
					fPolygon.add_kernel(fPolygon.reflection_y)
					
			new_vertices = fPolygon.transformation_2d(fPolygon.vertices_break()[-1])
			new_vertices = fPolygon.vertices_join(fPolygon.vertices_break()[0], new_vertices)
			self.graphs[1].plot("Final polygon", new_vertices)

	@staticmethod
	def github():
		webbrowser.open("https://github.com/allexlima/cg-penrose")

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
