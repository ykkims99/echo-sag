import tensorflow as tf
import numpy as np

def evaluate_model(model_path, test_data, test_labels):
    model = tf.keras.models.load_model(model_path)
    loss, acc = model.evaluate(test_data, test_labels)
    print(f"Test Accuracy: {acc * 100:.2f}%")

if __name__ == "__main__":
    # 가상의 테스트 데이터 불러오기
    X_test = np.random.rand(100, 200, 1).astype(np.float32)
    y_test = np.random.randint(0, 2, 100)
    evaluate_model("model.h5", X_test, y_test)
