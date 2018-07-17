import json
import requests
import configparser


CONFIG = configparser.ConfigParser()
CONFIG.read('crypto\provider.conf')


def getWalletsBalance(walletAddress) :

	url = CONFIG["Ethereum"]["Provider"].format(key = CONFIG["Ethereum"]["API_Key"], 
		address = walletAddress)
	
	response = requests.get(url)
	return response.json()
