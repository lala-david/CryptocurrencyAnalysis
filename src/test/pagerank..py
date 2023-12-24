import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


file_path = 'Eth_Txs.csv'
df = pd.read_csv(file_path)


address = "0xc179fbddc946694d11185d4e15dbba5fd0adac0a"


connected_txs = df[(df['From'] == address) | (df['To'] == address)]


G = nx.from_pandas_edgelist(connected_txs, 'From', 'To', create_using=nx.DiGraph())


plt.figure(figsize=(15, 15)) 
pos = nx.spring_layout(G, k=0.8)
nx.draw(G, pos, with_labels=True, node_color='yellow', node_size=1000, edge_color='blue', font_size=6, arrows=True)  


edge_labels = {(u, v): u[0:6]+'..'+v[0:6] for u, v in G.edges()} 
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=6)

plt.show()

G = nx.from_pandas_edgelist(df, 'From', 'To', create_using=nx.DiGraph())

pr = nx.pagerank(G, alpha=0.85)

top_addresses = sorted(pr.items(), key=lambda x: x[1], reverse=True)[:20]

for i, (address, pr_value) in enumerate(top_addresses):
    print(f"Rank {i+1}: Address {address}, PageRank value:  {'{:.10f}'.format(pr_value)}")


address = "0x00805ea227ac94796e92f619440c590f3f8e1615"


G = nx.from_pandas_edgelist(df, 'From', 'To', create_using=nx.DiGraph())

pr = nx.pagerank(G, alpha=0.85)

print(f"The PageRank of address {address} is {'{:.10f}'.format(pr_value)}")




address = "0xd6cb6744b7f2da784c5afd6b023d957188522198"


connected_txs = df[(df['From'] == address) | (df['To'] == address)]


G = nx.from_pandas_edgelist(connected_txs, 'From', 'To', create_using=nx.DiGraph())


plt.figure(figsize=(15, 15)) 
pos = nx.spring_layout(G, k=0.8)
nx.draw(G, pos, with_labels=True, node_color='yellow', node_size=1000, edge_color='blue', font_size=6, arrows=True)  


edge_labels = {(u, v): u[0:6]+'..'+v[0:6] for u, v in G.edges()} 
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=6)

plt.show()