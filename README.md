# echo-sag: Real-Time Anomaly Detection in Power Waveforms

`echo-sag`는 논문 기반 전력 품질 이상 탐지 시스템의 전체 구현을 포함하는 오픈소스 프로젝트입니다.  
본 프로젝트는 실제 110–240V AC 전압 기반의 1,000건 이상의 실측 또는 시뮬레이션 전압 데이터를 활용하며,  
경량화된 1D-CNN + RNN 기반 모델을 통해 Raspberry Pi CM4, ESP32, Jetson Nano 등에서 실시간 추론을 가능하게 합니다.

## 프로젝트 구성

echo-sag/
├── data/                      # 정상/이상 시계열 전압 샘플 (20kHz 슬라이딩 윈도우)
├── model/                    # Conv1D 기반 모델 정의
├── scripts/                  # 전처리, 추론, 변환 스크립트
├── compare/                  # 기존 FFT/LSTM 모델과의 성능 비교
├── LICENSE                   # MIT 라이선스
├── README.md                 # 프로젝트 요약 및 실행 안내
├── test_log.txt              # 실제 성능 측정 로그
├── metrics_result.json       # 논문 수치 기반 메타 정보
└── verify_accuracy.py        # 모델 성능 검증 스크립트

## 주요 성능 요약

- 정확도: 98.1%
- 추론 시간: 91.8ms (Raspberry Pi CM4 기준)
- 데이터 구성: 1,000건 이상 (110~240V AC), 슬라이딩 윈도우 200pt

## 실행 방법

```bash
# 모델 학습 후 TFLite 변환
python scripts/convert_to_tflite.py

# 슬라이딩 윈도우 생성 예시
python scripts/preprocessing.py

# 추론 테스트 (TFLite)
python scripts/inference.py

# 정확도 검증
python verify_accuracy.py
```

## 민감도 분석 결과

Sliding window 크기 및 stride 변화에 따른 정확도 및 추론 시간 분석:

- compare/stride_window_sweep.md
- compare/stride_window_sweep.json

## 지원 하드웨어

- Raspberry Pi CM4
- ESP32 (ESP-DL 기반)
- Jetson Nano
- BeagleBone
- Coral Edge TPU

## 라이선스

본 프로젝트는 MIT 라이선스를 따릅니다. 자유롭게 사용 가능하며, 재배포 및 수정 시 원저작자 표시만 유지해 주세요.

---

문의 및 협업 제안: ykkims99@gmail.com

