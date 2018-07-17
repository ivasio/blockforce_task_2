from PyQt5 import QtWidgets, uic
from crypto import tools as eth


def displayInfo():
	walletAddress = dialog.lineEdit.text()
	info = eth.getWalletsBalance(walletAddress)
	dialog.textBrowser.setText(info["result"])


app = QtWidgets.QApplication([])
dialog = uic.loadUi("window.ui")

dialog.pushButton.clicked.connect(displayInfo)

dialog.show()
app.exec()