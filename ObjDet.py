#Importing Libraries
import numpy as np
import cv2
# Capturing video through webcam
webcam = cv2.VideoCapture(0)
while(1):
  _, imageFrame = webcam.read()
  hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
  red_lower = np.array([136, 87, 111], np.uint8)
  red_upper = np.array([180, 255, 255], np.uint8)
  red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

  kernel = np.ones((5, 5), "uint8")

  red_mask = cv2.dilate(red_mask, kernel)
  res_red = cv2.bitwise_and(imageFrame, imageFrame, mask = red_mask)

  contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
      x, y, w, h = cv2.boundingRect(contour)
      imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)
      cv2.putText(imageFrame, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

  cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
  if cv2.waitKey(10) & 0xFF == ord('q'):
      cap.release()
      cv2.destroyAllWindows()
      break