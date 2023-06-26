import cv2 
import numpy as np

cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

 
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])


    mask = cv2.inRange(hsv, lower_black, upper_black)
    filtered = cv2.bitwise_and(frame, frame, mask=mask)


    filtered_gray = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(filtered_gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            angle = np.arctan2(y2 - y1, x2 - x1) * 180.0 / np.pi
            print("Angle: ", round(angle))
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()





