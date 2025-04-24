import tensorflow as tf

def convert_model(h5_path="model.h5", tflite_path="model.tflite"):
    model = tf.keras.models.load_model(h5_path)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    with open(tflite_path, "wb") as f:
        f.write(tflite_model)

if __name__ == "__main__":
    convert_model()
