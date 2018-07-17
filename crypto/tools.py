import json
import requests
import configparser


CONFIG = configparser.ConfigParser()
CONFIG.read('crypto\provider.conf')


def checkInternetConnection() :
	try : 
		response = requests.get("https://google.com")
		return True
	except :
		return False


def checkProvider(currency) :

	url = CONFIG[currency]["Test_Provider"].format(key = CONFIG[currency]["API_Key"])
	response = requests.get(url).json()

	return bool(int(response["status"]))
	

def checkWallet(walletAddress) :

	url = CONFIG["Ethereum"]["Provider"].format(key = CONFIG["Ethereum"]["API_Key"], 
		address = walletAddress)
	
	response = requests.get(url).json()
	return response


def getWalletBalance(walletAddress) :

	url = CONFIG["Ethereum"]["Provider"].format(key = CONFIG["Ethereum"]["API_Key"], 
		address = walletAddress)
	
	response = requests.get(url).json()
	return response.json()
