import requests 
import json
import os
from dotenv import load_dotenv

#Api Key for subscan
load_dotenv()
subscanApiKey = os.getenv('subscanApiKey')

walletAddress = os.getenv('walletAddress')

#Set to network api
#https://support.subscan.io/#service-status
url = "https://polkadot.api.subscan.io/api/scan/account/reward_slash"

#Number of days to look back
days = 7

#Number or era's in 24 hours
erasInDay = 1

#How many decimals on the chain
#https://guide.kusama.network/docs/learn-DOT/
tokenDecimals = 10

totalProfit = 0


if __name__ == "__main__":

    for x in range(days*erasInDay):
        data = {
            "row": 1,
            "page": x,
            "address": walletAddress 
        }

        r = requests.post(url, data=json.dumps(data),headers={'Content-Type': 'application/json', 'X-API-Key' : subscanApiKey} )

        list = r.json()['data']['list']

        buffer = 12 - len(list[0]['amount'])
        num = list[0]['amount']

        totalProfit = int(num) + totalProfit
    
    print(totalProfit / (10 ** (tokenDecimals)))

