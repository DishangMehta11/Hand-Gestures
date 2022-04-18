import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)

sensitivity = 25

yellow_lower = np.array([22, 93, 0])
yellow_upper = np.array([45, 255, 255])
prev_y = 0

while True:
    success, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print(contours)
    for c in contours:
        # print(c)
        area = cv2.contourArea(c)
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            if y < prev_y - sensitivity:
                pyautogui.press('PgDn')

            if y > prev_y + sensitivity:
                pyautogui.press('PgUp')

            prev_y = y
    cv2.imshow('Image', img)
    # cv2.imshow("HSV", hsv)
    # cv2.imshow("Mask", mask)
    if cv2.waitKey(1) == ord('q'):
        break

# cap.release()
# cv2.destroyAllWindows()
