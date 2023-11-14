import requests
import json
import time

address = "1N31P6vM4mJHUZx325qYj6ZFRK8eXHqqfo"

result = []
url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/full"

while True:
    response = requests.get(url)
    data = response.json()

    if 'txs' not in data or len(data['txs']) == 0:
        break   

    for tx in data['txs']:
        total_output_satoshi = sum([output['value'] for output in tx['outputs']])
        total_output_btc = total_output_satoshi / 100000000  
        result.append({
            'datetime': tx['confirmed'],
            'total_output': total_output_btc   
        })

    last_tx_hash = data['txs'][-1]['hash']
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/full?before={last_tx_hash}"
    # API 1 sec 
    time.sleep(1)  

timestamp = int(time.time())
with open(f'output_{timestamp}.json', 'w') as f:
    json.dump(result, f)
