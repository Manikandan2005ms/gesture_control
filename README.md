# Gesture Control System

This project is a gesture recognition system that processes and recognizes gestures to perform specific actions. It consists of several components that work together to achieve this functionality.

# AI Hand Gesture Control System

This project uses computer vision and hand gesture recognition to control common computer tasks using a webcam. Built with Python, OpenCV, and MediaPipe, it supports gestures for copy, cut, paste, select, screenshots, and even launching apps.

## 🔧 Tech Stack
- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- Keyboard
- GitHub

## 🎯 Features
| Gesture             | Action             |
|---------------------|--------------------|
| ✊ All fingers closed | Take Screenshot    |
| ☝️ Index only        | Select / Click     |
| ✌️ Index + Middle    | Copy               |
| 🤞 Index + Mid + Ring| Cut                |
| 🤟 Thumb + Index + Pinky | Paste        |
| ✋ Swipe Up/Down     | Scroll PDF         |
| 👉 Swipe Right       | Launch Calculator  |
| 👈 Swipe Left        | Launch Notepad     |

## ▶️ Run This Project

pip install -r requirements.txt
python main.py

## Files Description

- **main.py**: This is the main entry point of the application. It initializes the system and orchestrates the gesture recognition process.

- **utils.py**: Contains utility functions that assist with gesture processing, such as data preprocessing and normalization.

- **gesture_map.py**: Defines the logic for mapping recognized gestures to specific actions. It includes classes or functions that handle the gesture recognition logic.

- **screenshots/**: A directory intended to store screenshots captured during the gesture recognition process for reference or debugging purposes.

- **logs/**: This directory contains log files. The `gesture_log.csv` file logs actions taken by the system, including timestamps and recognized gestures.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd gesture_control
   ```

3. Install the required dependencies (if any):
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

To run the gesture recognition system, execute the following command:
```
python main.py
```

Ensure that your camera is accessible and properly configured to capture gestures.


## License

If you'd like, I can:
- Write your full `README.md` and push it for you
- Generate sample screenshots for uploading
- Help with adding a license or GitHub topics/tags

Would you like help with any of these?
