# Sliding Window & Stride Sweep Analysis

This document summarizes the results of a sweep test on different sliding window sizes and stride values, to evaluate their impact on model accuracy and inference latency. All tests were performed using a TensorFlow Lite model (approx. 82KB) on Raspberry Pi CM4.

## 🔬 Experiment Summary

| Window Size | Stride | Accuracy (%) | Inference Time (ms) |
|-------------|--------|---------------|----------------------|
| 150         | 25     | 94.3          | 88.2                 |
| 200         | 50     | 98.1          | 91.8                 |
| 250         | 100    | 97.6          | 95.3                 |

## 📌 Notes
- The best accuracy and real-time trade-off was observed at `window_size=200`, `stride=50`.
- Smaller windows tend to lose anomaly context, while larger windows increase latency.
- All results are logged in `stride_window_sweep.json`.

## 🔗 Reference
Part of the echo-sag project: [https://github.com/ykkims99/echo-sag](https://github.com/ykkims99/echo-sag)
