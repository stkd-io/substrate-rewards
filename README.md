# Substrate-rewards

## This should only be used to get a Guesstimate on the token rewarded for a wallet. 

This python script will connect to the subscan api (https://pro.subscan.io/login) and get the rewards for a wallet. 
**CAUTION** This is not era aware and will only loop through and grab the latest rewards from the api. The default is 
check 7 days back * number of era's a chain has in a 24 hour period. If you need to check back further you can update
the days variable to whatever you need. To use place your subscan apikey and wallet address into the .env file then:


```
pip3 install -r requirements.txt
python3 kusama_rewards.py
```


Tips:
- KSM: Fq4YmiAq76DntjMKKjMiL98MYszoApUa9idSErvyzfdGoqG
- DOT: 12pdN2XsNmG2yPAv5QCkq7YYUg1MM3prvGMgusH7S6FnDHAx
