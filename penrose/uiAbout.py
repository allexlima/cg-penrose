from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from penrose.gui.aboutwindow_ui import Ui_Dialog


class AboutWindow(QDialog, Ui_Dialog):
	def __init__(self):
		super(AboutWindow, self).__init__()
		self.setupUi(self)
		self.setWindowModality(Qt.ApplicationModal)
