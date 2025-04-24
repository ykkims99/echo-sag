import tensorflow as tf
import numpy as np

def load_tflite_model(tflite_path="model.tflite"):
    interpreter = tf.lite.Interpreter(model_path=tflite_path)
    interpreter.allocate_tensors()
    return interpreter

def run_inference(interpreter, input_data):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    return interpreter.get_tensor(output_details[0]['index'])

if __name__ == "__main__":
    # 예시 입력 데이터 (200포인트)
    input_data = np.random.rand(1, 200, 1).astype(np.float32)
    interpreter = load_tflite_model()
    output = run_inference(interpreter, input_data)
    print("Inference Output:", output)
