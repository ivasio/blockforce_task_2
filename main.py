from PyQt5 import QtWidgets, uic
from crypto import tools as eth
import time

def showErrorWindow (message):
	error_dialog = QtWidgets.QMessageBox()
	error_dialog.setText(message)
	error_dialog.setWindowTitle("Error")
	error_dialog.exec_() 


def displayInfo():
	
	if eth.checkInternetConnection() == False : 
		showErrorWindow ("Интернет-подключение отсутствует!")
		return False

	walletAddress = dialog.lineEdit.text()
	check = eth.checkWallet(walletAddress)
	
	if check.status == "0" :
		if check.result == "Error! Invalid address format" :
			showErrorWindow ("Неверно введен адрес кошелька!")
		else :
			showErrorWindow ("Ошибка!")
		return False
	
	info = eth.getWalletBalance(walletAddress)
	dialog.textBrowser.setText(info["result"])





app = QtWidgets.QApplication([])
dialog = uic.loadUi("window.ui")

dialog.pushButton.clicked.connect(displayInfo)


dialog.show()
print ("shit")
app.exec()

