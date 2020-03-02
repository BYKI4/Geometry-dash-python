from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QLabel
from PyQt5.QtGui import QPixmap
import sys
import os
from game import Ui_Form


class Intro(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Geometry Dash (alpha)")
        self.pushButton.clicked.connect(self.game)
        self.pushButton_2.clicked.connect(self.info)
        self.pic = QPixmap(os.path.join('data', 'geometry-dash-icon.png'))
        self.label = QLabel(self)
        self.label.move(225, 100)
        self.label.resize(200, 200)
        self.label.setPixmap(self.pic)

    def game(self):
        import classes_and_functions as code
        self.game_gd = code.Game()
        self.hide()
        self.game_gd.main()
        del self.game_gd, code
        self.show()

    def info(self):
        ok = QMessageBox.information(self, "Управление", "Управление двумя кнопками: пробелом или левой кнопкой мыши")
        if ok:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    intr = Intro()
    intr.show()
    sys.exit(app.exec())
