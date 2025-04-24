import numpy as np

def sliding_window(signal, window_size=200, step=50):
    windows = []
    for i in range(0, len(signal) - window_size + 1, step):
        windows.append(signal[i:i + window_size])
    return np.array(windows)

if __name__ == "__main__":
    # 예시 전압 신호 (400포인트)
    example_signal = np.sin(np.linspace(0, 4 * np.pi, 400))
    windows = sliding_window(example_signal)
    print("Generated", len(windows), "windows of shape", windows.shape)
