import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)

green_lower = np.array([22, 93, 0])
green_upper = np.array([45, 255, 255])
prev_y = 0

while True:
    success, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, green_lower, green_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if y < prev_y:
                pyautogui.press('PgDn')

            prev_y = y
    cv2.imshow('Image', img)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
