import pandas as pd
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense

#Reading test data
data = pd.read_csv('beam_data_eigen.csv')
data_train = data.sample(n=50)
predictor = data_train.drop(["k1","k2"],axis=1)
n_cols_predictor = predictor.shape[1]
# print(predictor)
target = data_train.drop(["y1(0.5)"],axis = 1)

model = Sequential()
model.add(Dense(25,activation='tanh',input_shape=(n_cols_predictor,)))
model.add(Dense(100,activation='softmax'))
model.add(Dense(200,activation='exponential'))
model.add(Dense(100,activation='softplus'))
model.add(Dense(50,activation='relu'))
model.add(Dense(2))
model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(predictor,target,epochs=5000)
data_test = data.loc[data.index.difference(data_train.index)]
test_predictor = data_test.drop(["k1","k2"],axis=1)
predictions = model.predict(test_predictor)
print("Testing prediction:")
print(predictions)
target = data_test.drop(["y1(0.5)"],axis = 1)
err=np.sum(np.abs(predictions-target.values),axis=0)
real=np.sum(target.values,axis=0)
print("Accuracy:")
print(100-(err*100/real))
test_predictor=pd.read_csv('testing.csv')

print("User input prediction:")
print(model.predict(test_predictor))