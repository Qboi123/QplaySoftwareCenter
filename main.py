import sys
import typing
from PySide2.QtWidgets import QApplication, QWidget, QCheckBox, QWizard, QGraphicsScene


class Main(QWidget):
    def __init__(self):
        super().__init__())

        self.setWindowTitle("Qplay Software Center")
        self.checkbox = QCheckBox("Test", self)
        self.checkbox.clicked.connect(self.checkbox_clicked)
        self.showMinimized()

    def checkbox_clicked(self, state):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
