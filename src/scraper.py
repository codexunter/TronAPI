from tronpy import Tron
from tronpy.providers import HTTPProvider

def getPage(account: str):
	#client=Tron()
	client=Tron(HTTPProvider(api_key="YOUR API KEY")) #INSERT APY KEY HERE
	balance=client.get_account_balance(account)
	bandwidth=client.get_bandwidth(account)
	return {'balance': balance, 'bandwidth': bandwidth}
