import sys
from PyQt5.QtWidgets import QApplication
from .uiManager import MainWindow

if __name__ == "__main__":
    app = QApplication(["Penrose"])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
