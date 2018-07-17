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
	
	if check["status"] == "0" :
		if check["result"] == "Error! Invalid address format" :
			showErrorWindow("Неверно введен адрес кошелька!")
		else :
			print (check.__str__())
			showErrorWindow("Ошибка!")
		return False
	
	info = eth.getWalletInfo(walletAddress)

	output = "Совершено {} транзакций\n".format(info["number"])
	if info["sum"] != 0 :
		output += "Сумма входящих транзакций - {}\n".format(str(info["sum"]))
		output += "Даты транзакций : \n"
		for date in info["dates"] :
			output += "{}\n".format(date)

	dialog.textBrowser.setText(output)





app = QtWidgets.QApplication([])
dialog = uic.loadUi("window.ui")

dialog.pushButton.clicked.connect(displayInfo)


dialog.show()
app.exec()

