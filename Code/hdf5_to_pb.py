import tensorflow as tf
from keras.models import load_model

keras_model_path = "../DnCNN/snr_15_model.hdf5"
saved_model_path = "../DnCNN/snr_15_model.pb"

model = load_model(keras_model_path, compile=False)
tf.saved_model.save(model, saved_model_path)