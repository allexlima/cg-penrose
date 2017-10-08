from PyQt5.QtWidgets import QMainWindow
from .gui.mainwindow_ui import Ui_MainWindow
from .uiPlots import PlotCanvas


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.graphs = None
		self.actions()
		self.init_canvas()
		self.create_table()

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
		self.popVertice.setEnabled(False)
		self.actionExit.triggered.connect(self.close)
		self.pushVertice.clicked.connect(self.button_addvertice)

	def button_addvertice(self):
		self.helpText.hide()
		# self.helpText.show()

	def create_table(self):
		self.tableVertices.set_template()
