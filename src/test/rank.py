import csv
import pandas as pd


file_path = "Eth_Txs.csv"

tras= []

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)

 
    for row in csv_reader:
        tras.append(row)

tras_sum = len(tras)
print("전체 트랜잭션 개수:", tras_sum)

df = pd.read_csv('Eth_Txs.csv')
 
df[['Amount', 'Unit']] = df['Value'].str.split(' ', expand=True)
 
df['Amount'] = df['Amount'].str.replace(',', '').astype(float)

 
df.loc[df['Unit'] == 'Ether', 'Amount'] *= 1e18

sender = df.groupby('From')['Amount'].sum().sort_values(ascending=False).head(10)
print('Eth 가장 많이 보낸 10개 주소:')
print(sender)

active = df['From'].value_counts().head(10)
print('\n거래 내역 많은 트랜잭션 10개 주소:')
print(active)

receiver = df.groupby('To')['Amount'].sum().sort_values(ascending=False).head(10)
print('Eth 가장 많이 받은 10개 주소:')
print(receiver)


# 각 주소의 거래 내역 분석
for address in active.index:
    print(f"주소: {address}")
    
    # 해당 주소의 거래 내역 추출
    address_txs = df[df['From'] == address]
    
    # 총 거래 횟수
    total_txs = len(address_txs)
    print(f"총 거래 횟수: {total_txs}")
    
    print("\n")

