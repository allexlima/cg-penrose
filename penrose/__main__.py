import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from penrose.uiManager import MainWindow


def main():
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("Penrose")
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
