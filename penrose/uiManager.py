from PyQt5.QtWidgets import QMainWindow
from .gui.mainwindow_ui import Ui_MainWindow
from .uiPlots import PlotCanvas


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.actions()
		self.init_canvas()

	def init_canvas(self):
		self.g1 = PlotCanvas(self)
		self.g1.move(380 + 30, 37 + 100)
		self.g2 = PlotCanvas(self)
		self.g2.move(380 + 325, 37 + 100)

	def set_polygon(self, points1, points2):
		self.g1.plot("Initial polygon", points1)
		self.g2.plot("Final polygon", points2)

	def actions(self):
		self.actionOpen_file.setEnabled(False)
		self.actionSave.setEnabled(False)
		self.actionExit.triggered.connect(self.close)
		self.pushVertice.clicked.connect(self.button_addvertice)

	def button_addvertice(self):
		self.helpText.hide()
		# self.helpText.show()