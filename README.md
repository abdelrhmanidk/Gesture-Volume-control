# Hand Tracking and Volume Control

This project uses OpenCV and a hand tracking module to control the system volume based on hand gestures detected through a webcam.

## Features
- **Hand Tracking**: Detects hand landmarks using a custom module (`handtrackingmodule`).
- **Proximity Detection**: Calculates the hand's proximity to the camera to determine if the system should respond.
- **Volume Control**: Adjusts the system volume based on the distance between the thumb and index finger.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- Numpy (`numpy`)
- Custom hand tracking module (`handtrackingmodule`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/abdelrhmanidk/Gesture-Volume-control.git
   cd Gesture-Volume-control
