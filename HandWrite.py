import cv2
import numpy as np
import HandTrackerModule as htm
import pytesseract

cap = cv2.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 600)
detector = htm.handDetector()
xp, yp = 0, 0
imgCanvas = np.zeros((480, 640, 3), np.uint8)

while True:
     #Import image
     success, img = cap.read()
     img = cv2.flip(img, 1)

     #Find Hand Landmarks
     img = detector.findHands(img)
     lmList = detector.findPosition(img, draw=False) #finds position of points of fingers

     if len(lmList) != 0:   #when hand is detected
          # tip of index and middle fingers
          x1, y1 = lmList[8][1:] #id 8 is index finger [1:] as we want x and y value which is 1 and 2 in list
          x2, y2 = lmList[12][1:] #if 12 is middle finger

          #Check which fingers are up
          fingers = detector.fingersUp()
          if fingers[1] and fingers[2] and fingers[3] == False and fingers[4] == False:
               xp, yp = 0, 0
          if fingers[1] and fingers[2] == False and fingers[3] == False and fingers[4] == False:  #Drawing Mode - if only Index finger is up
               cv2.circle(img, (x1, y1), 15, (255,255,0), cv2.FILLED)
               #print("Drawing Mode")
               if xp == 0 and yp == 0:
                    xp, yp = x1, y1

               cv2.line(img, (xp, yp), (x1, y1), (255,255,0), 8)
               cv2.line(imgCanvas, (xp, yp), (x1, y1), (255, 255, 0), 8)
               xp, yp = x1, y1

          # Clear Canvas when 4 fingers are up
          if fingers[1] and fingers[2] and fingers[3] and fingers[4]:
             imgCanvas = np.zeros((480, 640, 3), np.uint8)

     imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
     _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
     _, imgInv2 = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
     imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
     if len(lmList)!=0:
          fingers = detector.fingersUp()
          if fingers[1] and fingers[2] and fingers[3] and fingers[4]==False: #detects when 3 fingers are up
               imgH, imgW = imgInv2.shape
               x1, y1, w1, h1 = 0, 0, imgH, imgW
               pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
               imgchar = pytesseract.image_to_string(imgInv2, lang='eng')
               imgboxes = pytesseract.image_to_boxes(imgInv2)
               for boxes in imgboxes.splitlines():
                    boxes = boxes.split(' ')
                    x, y, w, h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
                    cv2.rectangle(imgInv2, (x, imgH - y), (w, imgH - h), (0, 0, 255), 3)
                    # cv2.putText(imgInv2, imgchar, (x1 + int(w1 / 50), y1 + int(h1 / 50)), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                    #           (0, 0, 255),
                    #          2)
               if imgchar:
                  print(imgchar)

     cv2.imshow("Inv", imgInv)
     # img = cv2.bitwise_and(img, imgInv)
     # img = cv2.bitwise_or(img, imgCanvas)
     #_,img3 = cap.read(imgInv2)
     #img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
     #if pytesseract.image_to_string(img3):
     #    print(pytesseract.image_to_string(img3))
     cv2.imshow("Image", img)

     if cv2.waitKey(1) & 0xFF == ord('q'):  # waitkey(1) is frame rate 1 fpms, when pressed q program exits
          break
cap.release()
cv2.destroyAllWindows()
