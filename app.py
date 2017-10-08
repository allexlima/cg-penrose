import sys
from gui import mainInterface
# from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

import random


class CgTriangle(QMainWindow, mainInterface.Ui_Cgtriangle):
	def __init__(self):
		super(CgTriangle, self).__init__()
		# uic.loadUi("gui/mainInterface.ui", self)
		self.setupUi(self)
		self.actions()
		self.init_canvas()

	def init_canvas(self):
		self.g1 = PlotCanvas(self)
		self.g1.move(380+30, 37+100)
		self.g2 = PlotCanvas(self)
		self.g2.move(380+325, 37+100)

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


class PlotCanvas(FigureCanvas):
	def __init__(self, parent=None, width=3, height=2, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		FigureCanvas.__init__(self, fig)
		self.setParent(parent)
		FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

	def plot(self, title, points):
		ax = self.figure.add_subplot(111)
		if points is None:
			points = np.array([[0, 0], [0, 0]])
			ax.cla()
		ax.set_aspect("equal")
		tr = plt.Polygon(points)
		ax.add_patch(tr)
		ax.relim()
		ax.autoscale_view()
		ax.set_title(title)
		self.draw()


def main():
	app = QApplication(sys.argv)
	main_window = CgTriangle()
	main_window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
