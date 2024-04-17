from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
import sys

class MyCalculator(QMainWindow):
    def __init__(self):
        super(MyCalculator, self).__init__()
        self.setGeometry(200, 200, 400, 600)
        self.setWindowTitle("Prosty Kalkulator")
        self.setFixedSize(400, 600)

        self.initUI()

    def initUI(self):
        self.setLabel()
        self.setButtons()   

    def setButtons(self):
        size = 80
        button_prop = [
            ["+", 0, 0, size, size, "append", "#ff7f0e"],
            ["7", 100, 0, size, size, "append", "#808080"],
            ["8", 200, 0, size, size, "append", "#808080"],
            ["9", 300, 0, size, size, "append", "#808080"],
            ["-", 0, 100, size, size, "append", "#ff7f0e"],
            ["4", 100, 100, size, size, "append", "#808080"],
            ["5", 200, 100, size, size, "append", "#808080"],
            ["6", 300, 100, size, size, "append", "#808080"],
            ["*", 0, 200, size, size, "append", "#ff7f0e"],
            ["1", 100, 200, size, size, "append", "#808080"],
            ["2", 200, 200, size, size, "append", "#808080"],
            ["3", 300, 200, size, size, "append", "#808080"],
            ["/", 0, 300, size, size, "append", "#ff7f0e"],
            ["0", 100, 300, size, size, "append", "#808080"],
            [".", 200, 300, size, size, "append", "#808080"],
            ["=", 300, 300, size, size, "evaluate", "#808080"],
            ["C", 0, 400, size, size, "clear", "#ff7f0e"],
        ]
 
        self.button = []
        for i in range(len(button_prop)):
            self.button.append(QtWidgets.QPushButton(self))
            self.button[i].setText(button_prop[i][0])
            self.button[i].setGeometry(button_prop[i][1]+10, button_prop[i][2]+110, button_prop[i][3], button_prop[i][4])
            self.button[i].setFont(QFont('Arial', 28))
            self.button[i].setStyleSheet("color: white; background-color: {}; border: 1px solid #ccc; border-radius: 10px;".format(button_prop[i][6]))
            if button_prop[i][5] == "append":
                self.button[i].clicked.connect(self.append)
            if button_prop[i][5] == "evaluate":
                self.button[i].clicked.connect(self.evaluate)
            if button_prop[i][5] == "clear":
                self.button[i].clicked.connect(self.clear)

    def setLabel(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(10, 10, 380, 80)
        self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label.setFont(QFont('Arial', 36))
        self.label.setStyleSheet("color: white; background-color: #444; border: 1px solid #ccc; border-radius: 10px;")

    def append(self):
        if self.label.text() == "Error":
            self.clear() 
        sender = self.sender()
        current_text = self.label.text()
        new_text = current_text + sender.text()
        self.label.setText(new_text)

    def evaluate(self):
        expression = self.label.text()
        try:     
            result = eval(expression)
            self.label.setText(str(result))
        except:
            self.label.setText("Error")
    
    def clear(self):
        self.label.setText("")


def window():
    app = QApplication(sys.argv)
    win = MyCalculator()
    win.setStyleSheet("background-color: #333;")
    win.show()
    sys.exit(app.exec_())

window()
