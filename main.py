from PyQt5 import QtWidgets, uic
from crypto import tools as eth
import openpyxl



if __name__ == '__main__':
	

	def showMessageWindow (message):
		error_dialog = QtWidgets.QMessageBox()
		error_dialog.setText(message)
		error_dialog.setWindowTitle("Error")
		error_dialog.exec_() 



	# Отображение информации о кошельке в текстовом окне
	def displayInfo():
		
		if eth.checkInternetConnection() == False : 
			showMessageWindow ("Интернет-подключение отсутствует!")
			return False

		walletAddress = window.lineEdit.text()

		if len(walletAddress) < 3 or walletAddress[0:2] != "0x" :
			showMessageWindow("Неверно введен адрес кошелька!")
			return False

		check = eth.checkWallet(walletAddress)
		
		if check["status"] == "0" :
			if check["result"] == "Error! Invalid address format" :
				showMessageWindow("Неверно введен адрес кошелька!")
			else :
				showMessageWindow("Ошибка!")
			return False
		
		global walletInfo # Запись в глобальную переменную 
		walletInfo = eth.getWalletInfo(walletAddress)

		output = "Совершено {} транзакций\n".format(walletInfo["number"])
		if walletInfo["number"] != 0 :
			output += "Сумма входящих транзакций - {}\n".format(str(walletInfo["sum"]))
			output += "Даты транзакций : \n"
			for date in walletInfo["dates"] :
				output += "{}\n".format(date)

		window.textBrowser.setText(output)


	# Запись в Excel
	def saveExcel() :

		if walletInfo is None :
			showMessageWindow("Нет данных для сохранения! Сначала получите \
				данные с помощью кнопки 'Просмотреть информацию'")
			return False

		filePath = QtWidgets.QFileDialog.getSaveFileName()[0]

		book = openpyxl.Workbook()
		sheet = book.active
		sheet["A1"] = "Совершено транзакций"
		sheet["B1"] = walletInfo["number"]

		if walletInfo["number"] != 0 :
			sheet["A2"] = "Сумма входящих транзакций"
			sheet["B2"] = walletInfo["sum"]
			sheet["A3"] = "Даты транзакций"
			counter = 4
			for date in walletInfo["dates"] :
				sheet["A" + str(counter)] = date
				counter += 1

		book.save(filePath)
		showMessageWindow("Данные сохранены!")



	walletInfo = None

	app = QtWidgets.QApplication([])
	window = uic.loadUi("window.ui")

	# Обработчики кнопок
	window.pushButton.clicked.connect(displayInfo)
	window.saveButton.clicked.connect(saveExcel)

	# Запуск основного цикла приложения
	window.show()
	app.exec()

