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
		ax.cla()
		if points is not None:
			vertices = []
			for item in points:
				ax.annotate("{}({}, {})".format(*item), (item[1], item[2])).set_fontsize(8)
				vertices.append([item[1], item[2]])
			tr = plt.Polygon(np.array(vertices))
			ax.add_patch(tr)
			ax.relim()
			ax.margins(x=0.30, y=0.30)
			ax.autoscale_view()
			ax.set_title(title).set_fontsize(9)
		self.draw()
