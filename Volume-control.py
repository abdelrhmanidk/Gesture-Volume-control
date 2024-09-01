import cv2
import time
import numpy as np
import handtrackingmodule as htm
import math
import os

# Set up camera parameters
wcam, hcam = 320, 240
cap = cv2.VideoCapture(1)
cap.set(3, wcam)
cap.set(4, hcam)

# Initialize hand detector and time variables
detector = htm.handDetection()
Ptime = 0

# Function to set the system volume
def set_volume(volume_level):
    os.system(f"osascript -e 'set volume output volume {volume_level}'")

# Main loop for video capture and hand tracking
while True:
    success, img = cap.read()
    if not success:
        break

    img = detector.findHand(img)
    lmList = detector.findPostion(img, draw=False)

    if lmList:
        # Get coordinates of thumb tip, index finger tip, and wrist
        x1, y1 = lmList[4][1], lmList[4][2]  # Thumb tip
        x2, y2 = lmList[8][1], lmList[8][2]  # Index finger tip
        x0, y0 = lmList[0][1], lmList[0][2]  # Wrist

        # Calculate the approximate hand size (distance between wrist and index finger tip)
        hand_size = math.hypot(x2 - x0, y2 - y0)
        print(f'Hand size: {hand_size}')

        # Proceed with volume control only if the hand is close to the camera
        if hand_size > 250:  # Threshold for proximity
            # Calculate distance between thumb and index finger
            length = math.hypot(x2 - x1, y2 - y1)
            print(f'Finger distance: {length}')

            # Draw landmarks and line between thumb and index finger
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

            # Set system volume based on the length
            if length < 50:
                set_volume(0)  # Mute the volume
            else:
                volume_level = min(max(int((length / 300) * 100), 0), 100)
                set_volume(volume_level)

    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - Ptime)
    Ptime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Image", img)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()