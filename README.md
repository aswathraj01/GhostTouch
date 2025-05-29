# 👻 GhostTouch

**GhostTouch** is a futuristic desktop interaction tool that lets you control your computer using finger movements captured via your webcam — no physical contact needed.

## 🚀 Features

- 📷 Real-time hand and finger tracking using your webcam
- 🖱️ Finger-based cursor movement (air mouse)
- 👆 Custom gesture detection (e.g., pinch to click)
- ⚡ Smooth, responsive desktop control
- 💻 Cross-platform (Windows, macOS, Linux)

## 🧠 How It Works

GhostTouch uses [MediaPipe](https://google.github.io/mediapipe/) for high-precision hand tracking, and [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) to simulate system input (mouse movement and clicks).

## 📦 Installation

Make sure Python 3.8+ is installed, then:

```bash
git clone https://github.com/yourusername/GhostTouch.git
cd GhostTouch
pip install -r requirements.txt

```
## ▶️ Usage

Run the main script:    python ghosttouch.py


### 📁 Project Structure

GhostTouch/
├── ghosttouch.py           # Main app loop
├── gestures.py             # Gesture detection logic
├── controller.py           # System control interface
├── utils.py                # Smoothing, filters, helpers
├── assets/                 # (Optional) UI overlays or icons
└── README.md               # Project documentation


### ✨ Future Plans

    🤏 Pinch to click
    ✌️ Two-finger swipe for scrolling
    📐 Adjustable sensitivity and gesture zones
    🎥 Webcam feed overlay with gesture markers


### 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.