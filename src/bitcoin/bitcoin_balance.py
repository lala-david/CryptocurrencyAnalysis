import os
import requests
import json
import datetime

file_name = "./doc/address.txt"
file_path = os.path.join(file_name)

if os.path.exists(file_path):

  with open(file_path) as f:
    addresses = f.read().splitlines()

  balances = {}
  for address in addresses:
    url = f"https://blockchain.info/balance?active={address}"   
    try:
      response = requests.get(url)
      balances[address] = json.loads(response.text)
    except:
      pass

  now = datetime.datetime.now()
  timestamp = now.strftime("%Y%m%d_%H%M%S")  
  out_file = f"./json/balance/balances_{timestamp}.json"
  print("🐧 Good work")

  with open(out_file, "w") as f:
     json.dump(balances, f)
     
else:
  print("File ❌")