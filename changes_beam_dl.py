import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense

#Reading test data
data = pd.read_csv('beam_data.csv')
data_train = data.sample(n=9990)
predictor = data_train.drop(["k1","k2"],axis=1)
n_cols_predictor = predictor.shape[1]
# print(predictor)
target = data_train.drop(["y1(0.2)","y2(0.7)","k2"],axis = 1)
maximum = max(target.values)
print(maximum)
target = target.values/maximum
model = Sequential()
model.add(Dense(100,activation='relu',input_shape=(n_cols_predictor,)))
model.add(Dense(100,activation='relu'))
model.add(Dense(1))
model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(predictor,target,epochs=200)
data_test = data.loc[data.index.difference(data_train.index)]
test_predictor = data_test.drop(["k1","k2"],axis=1)
print(test_predictor)
predictions = model.predict(test_predictor)*maximum
print(predictions)