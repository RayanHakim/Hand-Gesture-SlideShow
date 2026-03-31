# 🖐️ AI-Powered Gesture Slideshow Controller

An advanced, touchless presentation tool built with **Python 3.12** and **MediaPipe Hands**. This project allows you to control PowerPoint or any slideshow application using natural hand gestures (lambaian tangan) without the need for physical clickers or colored markers.

## ✨ Key Features
- **AI-Based Tracking:** Uses MediaPipe's 21-point hand landmark model for high-precision tracking (no more color-dependency issues!).
- **Always-on-Top Monitor:** A compact floating camera window that stays visible even when PowerPoint is in Full Screen / Slide Show mode.
- **Smart Debouncing:** Implemented a cooldown system to prevent accidental multiple slide skips.
- **Natural Interface:** - **Right Zone:** Trigger "Next Slide" (Simulates Right Arrow Key).
  - **Left Zone:** Trigger "Back Slide" (Simulates Left Arrow Key).
  - **Center Zone:** Neutral area for explaining materials without triggering actions.
- **Dual-Exit Logic:** Close the program using the 'Q' key or the standard window 'X' button.

## 🛠️ Tech Stack
- **Python 3.12.10** (Optimized for MediaPipe compatibility).
- **OpenCV** - Image processing and GUI rendering.
- **MediaPipe** - Real-time Hand Landmark detection.
- **PyAutoGUI** - Cross-platform GUI automation for keyboard simulation.

## 🚀 Installation & Environment Setup

Since MediaPipe currently has limited support for Python 3.13, follow these steps to set up the **Python 3.12** environment on Windows:

1. **Install Python 3.12.10:** Download from [python.org](https://www.python.org/downloads/windows/).
2. **Setup Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
