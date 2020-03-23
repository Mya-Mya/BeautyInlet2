import tensorflow as tf
from tensorflow import Session
from tensorflow import keras
import os

print(tf.__version__)
MY_DIR=os.path.dirname(__file__)
print(MY_DIR)
TEST_DIR=os.path.join(MY_DIR,"..","test_data")
print(TEST_DIR)
MODEL_FNAME=os.path.join(MY_DIR,"..","modelA-01500.h5")
print(MODEL_FNAME)

model=keras.models.load_model(MODEL_FNAME)
model.summary()