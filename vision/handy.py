import cv2
import mediapipe as mp
import time
import math
import numpy as np
import json


 
class handDetector():
    def __init__(self, mode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.hands = mp.solutions.hands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
       
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
 
    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        self.findPosition(img)
        # print(results.multi_hand_landmarks)
 
     #   if self.results.multi_hand_landmarks:
      #      for handLms in self.results.multi_hand_landmarks:
       #         if draw:
        #            self.mpDraw.draw_landmarks(img, handLms,
         #                                      self.mpHands.HAND_CONNECTIONS)
 
        
 
    def findPosition(self, img, handNo=0):
#       xList = []
#       yList = []
#       bbox = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
#                xList.append(cx)
#                yList.append(cy)
                # print(id, cx, cy)
                self.lmList.append([id, cx, cy])
                 
#            xmin, xmax = min(xList), max(xList)
#            ymin, ymax = min(yList), max(yList)
#            bbox = xmin, ymin, xmax, ymax
 
 
        return self.lmList,# bbox
 
    def fingersUp(self):
        
        fingers = []
        # Thumb
        #print(self.lmList)
        #print(self.tipIds)
        
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
 
        # Fingers
        for id in range(1, 5):
 
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
 
        # totalFingers = fingers.count(1)
 
        return fingers
 
    def findDistance(self, p1, p2, img):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
 
        
        length = math.hypot(x2 - x1, y2 - y1)
 
        return length, img, [x1, y1, x2, y2, cx, cy]

      

class buffers:
    def __init__(self) -> None:
        self.click=0
        self.stream=0
        self.labels=0
    def send_click(self,lineInfo):
        self.buffer=json.dumps({"EVENT":"CLICK", "x": lineInfo[4],"y": lineInfo[5]})
    
buffer = buffers()        

def hands(detector, frame):
    fingers=[0,0,0,0,0]
    img = detector.findHands(frame)
    lmList = detector.findPosition(img, handNo=1)
    
    if lmList != ([],):
        fingers = detector.fingersUp()

        # Click mouse if distance between Index and middle fingers is short
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)           
            if length < 40:
                #cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                buffer.send_click([lineInfo])
    #print("hands")

