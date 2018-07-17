import json
import requests
import configparser
from datetime import datetime


CONFIG = configparser.ConfigParser()
CONFIG.read('crypto\provider.conf')


def checkInternetConnection() :
	try : 
		response = requests.get("https://google.com")
		return True
	except :
		return False
	

def checkWallet(walletAddress) :

	url = CONFIG["Ethereum"]["Test_Provider"].format(key = CONFIG["Ethereum"]["API_Key"], 
		address = walletAddress)
	
	response = requests.get(url).json()
	return response


def getWalletInfo(walletAddress) :

	url = CONFIG["Ethereum"]["Provider"].format(key = CONFIG["Ethereum"]["API_Key"], 
		address = walletAddress)
	
	response = requests.get(url).json()

	sum = 0
	dates = []
	if len(response["result"]) != 0 :
		for transaction in response["result"] :
			if transaction["to"] == walletAddress :
				sum += int(transaction["value"])
			dates.append (datetime.fromtimestamp(int(transaction["timeStamp"])).strftime("%d.%m.%Y"))

	return {
		"number" : len(response["result"]),
		"sum" : sum,
		"dates" : dates
	}
