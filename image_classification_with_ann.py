# -*- coding: utf-8 -*-
"""image_Classification_with_ANN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HOdNKkT_wxs1gA_xhvqmLLGMWb4MeMZo
"""

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.datasets import fashion_mnist
from keras.models import Sequential 
from keras.layers import Dense,Dropout, BatchNormalization
from keras.utils.np_utils import to_categorical
from keras import optimizers
from keras.layers import Activation

(x_train,y_train),(x_test,y_test)=fashion_mnist.load_data()

plt.figure(figsize=[5,5])
plt.imshow(x_train[5], cmap="gray")
plt.show()
print("Label : ", y_train[5])

plt.figure(figsize=(10,1))
for i in range(10):
  plt.subplot(1,10,i+1)
  plt.imshow(x_train[i])
plt.show()

print("Label of above images : %s " %(y_train[0:10]))

#x_train.shape 
x_test.shape

# reshaping x data (n,28,28) = > (n , 784)
x_train=x_train.reshape((x_train.shape[0],-1))
x_test=x_test.reshape((x_test.shape[0],-1))

# converting y data into categorical (one - hot encoding)
y_train=to_categorical(y_train)
y_test=to_categorical(y_test)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

model=Sequential()
model.add(Dense(50, input_shape=(784, )))
model.add(Activation("sigmoid"))
model.add(Dense(50))
model.add(Activation("sigmoid"))
model.add(Dense(50))
model.add(Activation("relu"))
model.add(Dense(50))
model.add(Activation("sigmoid"))
model.add(Dense(10))
model.add(Activation("softmax"))

sgd=optimizers.sgd(learning_rate=0.01)
model.compile(optimizer=sgd,loss="categorical_crossentropy", metrics=['accuracy'])

history=model.fit(x_train,y_train,batch_size=256,epochs=30,verbose=1)
results=model.evaluate(x_test,y_test)

print("Test accuracy: ", results[1])

def mlp_model():
  model=Sequential()
  model.add(Dense(50 , input_shape=(784,), kernel_initializer="he_normal"))
  model.add(Activation('sigmoid'))
  model.add(Dense(50,kernel_initializer="he_normal"))
  model.add(Activation('sigmoid'))
  model.add(Dense(50,kernel_initializer="he_normal"))
  model.add(Activation('relu'))
  model.add(Dense(50, kernel_initializer='he_normal'))
  model.add(Activation('sigmoid'))
  model.add(Dense(10, kernel_initializer='he_normal'))
  model.add(Activation('softmax'))

  sgd=optimizers.sgd(learning_rate=0.01)
  model.compile(optimizer=sgd,loss='categorical_crossentropy', metrics=['accuracy'])

  return model

model=mlp_model()
history=model.fit(x_train,y_train,batch_size=200,epochs=50,verbose=1)
result2=model.evaluate(x_test,y_test)


print("Test accuracy: ", result2[1])


def MLP_Model():
  model=Sequential()
  model.add(Dense(50, input_shape=(784,)))
  model.add(Activation('relu'))
  model.add(Dense(50))
  model.add(Activation('relu'))
  model.add(Dense(50))
  model.add(Activation('sigmoid'))
  model.add(Dense(50))
  model.add(Activation('relu'))
  model.add(Dense(10))
  model.add(Activation('softmax'))

  optimizerX=optimizers.SGD(learning_rate=0.001)
  model.compile(optimizer=optimizerX,loss='categorical_crossentropy',metrics=['accuracy'])

  return model

model2=MLP_Model()
history=model2.fit(x_train,y_train,batch_size=256,epochs=10,verbose=1)
result3=model2.evaluate(x_test,y_test)
print("Test accuracy: ", result3[1])
"""Batch Normalization"""
#
def MLP_model():
  model=Sequential()
  model.add(Dense(50, input_shape=(784,)))
  model.add(BatchNormalization())
  model.add(Activation('relu'))
  model.add(Dense(50))
  model.add(BatchNormalization())
  model.add(Activation('relu'))
  model.add(Dense(50))
  model.add(BatchNormalization())
  model.add(Activation('relu'))
  model.add(Dense(50))
  model.add(BatchNormalization())
  model.add(Activation('relu'))
  model.add(Dense(10))
  model.add(Activation('softmax'))

  SGDOP=optimizers.SGD(learning_rate=0.01)
  model.compile(optimizer=SGDOP,loss='categorical_crossentropy',metrics=['accuracy'])

  return model

model3=MLP_model()
history=model3.fit(x_train,y_train,batch_size=256,epochs=20,verbose=1)

print(model3.evaluate(x_test, y_test))

"""Dropout"""

def MLP_MODEL():
  model=Sequential()
  model.add(Dense(128, input_shape=(784,),kernel_initializer='he_normal'))
  model.add(BatchNormalization())
  model.add(Activation('relu'))
  model.add(Dropout(0.2))
  model.add(Dense(128, kernel_initializer='he_normal'))
  model.add(BatchNormalization())
  model.add(Activation('relu'))
  model.add(Dropout(0.2))
  model.add(Dense(128, kernel_initializer='he_normal'))
  model.add(BatchNormalization())
  model.add(Activation('relu'))
  model.add(Dropout(0.2))
  model.add(Dense(50, kernel_initializer='he_normal'))
  model.add(BatchNormalization())
  model.add(Activation('relu'))
  model.add(Dropout(0.2))
  model.add(Dense(10, kernel_initializer='he_normal'))
  model.add(Activation('softmax'))



  sgdopti=optimizers.SGD(learning_rate=0.01)
  model.compile(optimizer=sgdopti,loss='categorical_crossentropy', metrics=['accuracy'])

  return model

model4=MLP_MODEL()
history=model4.fit(x_train,y_train,batch_size=200,epochs=20,verbose=1)
print(model4.evaluate(x_test,y_test))
