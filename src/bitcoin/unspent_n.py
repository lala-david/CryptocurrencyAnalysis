import json
import requests
from datetime import datetime

# 주소 입력
address = input("Enter the bitcoin address: ")

timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

# utxo 조회
try:
    resp_utxo = requests.get('https://blockchain.info/unspent?active={}'.format(address)) 
    resp_utxo.raise_for_status()   
    utxo_set = resp_utxo.json()["unspent_outputs"]

    # utxo 정보
    utxo_info = [{'TX_ID': utxo['tx_hash_big_endian'], 'TX_Number': utxo['tx_output_n'], 'Amount': utxo['value']} for utxo in utxo_set]
    with open(f'./json/unspent_n/unspent_{timestamp}.json', 'w') as f:
        json.dump(utxo_info, f)
except requests.exceptions.RequestException as e:
    print(f"UTXO 조회 실패: {e}")

# 잔액 조회
try:
    resp_balance = requests.get('https://blockchain.info/balance?active={}'.format(address))
    resp_balance.raise_for_status()  

    # 잔액 정보
    with open(f'./json/unspent_n/balance_{timestamp}.json', 'w') as f:
        json.dump(resp_balance.json(), f)
        json.dump(resp_balance.json(), f)
except requests.exceptions.RequestException as e:
    print(f"잔액 조회 실패: {e}")
