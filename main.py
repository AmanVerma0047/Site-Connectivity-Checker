import requests
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class mywidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.inputURL = QtWidgets.QLineEdit()
        self.inputURL.placeholderText = "Type URL Here (https://....)"

        self.button = QtWidgets.QPushButton("Check Site Connectivity")
        self.resultLabel = QtWidgets.QLabel("") #empty label to show the message!

        layout  = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.inputURL)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.button)
        
        
        self.button.clicked.connect(self.checkUrl)


    def checkUrl(self):
        url = self.inputURL.text().strip()
        
        if not url:
            self.resultLabel.setText("⚠Incorrect URL!")
            return

        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.resultLabel.setText("✅Site is Online!")
            else:
                self.resultLabel.setText("❌Site is Offline!")
        except Exception as e:
            self.resultLabel.setText(f"ERROR:{e}")
        # print("Site is online!") if response.status_code == 200 else print("Site not found!")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = mywidget()
    window.setWindowTitle("Site Connectivity Checker!")
    window.resize(300,150)
    window.show()
    app.exec()
