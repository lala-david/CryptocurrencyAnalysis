import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping

data = pd.read_csv('data/transaction.csv')

for col in data.columns:
    if data[col].dtype == 'object':
        data[col] = data[col].astype('category').cat.codes

data = data.fillna(data.mean())
# data shuffle 
for _ in range(1000):
    data = data.sample(frac=1).reset_index(drop=True)

# Target
X = data.drop(columns=['FLAG', 'Address'])
y = data['FLAG']

# minmax 
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# 오버샘플링
smote = SMOTE(random_state=42)
X, y = smote.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# reshape
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

# model 
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(X_train.shape[1], 1), name='lstm_layer'))  
model.add(Dense(1, activation='sigmoid', name='output_layer'))  


model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# EarlyStopping 
es = EarlyStopping(monitor='val_accuracy', mode='max', verbose=1, patience=50, baseline=0.96)

# 모델 학습
model.fit(X_train, y_train, epochs=60, batch_size=32, verbose=1, validation_split=0.2, callbacks=[es])
loss, accuracy = model.evaluate(X_test, y_test, verbose=2)

print(f'Loss: {loss}, Accuracy: {accuracy}')

model.save('model/lstm3_onchain.h5') 