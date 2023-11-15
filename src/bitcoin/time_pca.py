import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


with open('./json/timepattern/output_1699986850.json', 'r') as f:
    data = json.load(f)

times = [int(d['datetime'][5:7]) for d in data]  
outputs = [d['total_output'] for d in data]

X = np.array(list(zip(times, outputs)))
pca = PCA(n_components=2) 
X_pca = pca.fit_transform(X)


colors = ['blue', 'purple', 'skyblue']


fig, ax = plt.subplots()
for i, color in enumerate(colors):
    indices = np.where(np.array(times) == i + 1)
    ax.scatter(X_pca[indices, 0], X_pca[indices, 1], color=color, label=f"Month {i+1}")

ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_title('Time Pattern PCA')
ax.legend()


print("PC1 주성분 값:", pca.components_[0])
print("PC2 주성분 값:", pca.components_[1])


plt.savefig('./img/timepattern_pca.png')
