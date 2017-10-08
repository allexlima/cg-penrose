from PyQt5.QtWidgets import QDialog
from .gui.verticewindow_ui import Ui_Dialog


class VerticesWindow(QDialog, Ui_Dialog):
	def __init__(self):
		super(VerticesWindow, self).__init__()
		self.setupUi(self)
