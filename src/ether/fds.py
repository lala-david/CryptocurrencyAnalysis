import pandas as pd

from sklearn.ensemble import RandomForestClassifier
import numpy as np 
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/transaction.csv')

print("-------------------------------------------------------------------")
print(df.columns)
print("-------------------------------------------------------------------")

# 상관계수 
corr_matrix = df.corr()

print(corr_matrix['FLAG'].sort_values(ascending=False))


str_cols = df.select_dtypes(include=[object]).columns

le = LabelEncoder()

for col in str_cols:
    df[col] = df[col].astype(str) 
    df[col] = le.fit_transform(df[col])

imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

X = df_imputed.drop(columns=['FLAG'])
y = df_imputed['FLAG']

model = RandomForestClassifier(random_state=0)
model.fit(X, y)

importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

for f in range(X.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30, X.columns[indices[f]], importances[indices[f]]))

print("-------------------------------------------------------------------")

# 히트맵 
plt.figure(figsize=(50, 50))
sns.heatmap(corr_matrix, vmax=1, square=True, annot=True)
plt.show()
print("-------------------------------------------------------------------")