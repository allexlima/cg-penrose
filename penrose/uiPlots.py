from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


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
