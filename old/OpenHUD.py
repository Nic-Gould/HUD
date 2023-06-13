import asyncio
from websockets.server import serve

import cv2
from ultralytics import YOLO
import vision.handy as handy
import json

video_path = "192.168.1.109:81/stream"  # default esp32cam output for testing

async def handler(websocket):
    while True:
        if clicker.buffer !=0:
            await websocket.send(clicker.buffer)
            clicker.buffer=0
       # msg = await websocket.recv()    
       # print(msg)
        await asyncio.sleep(5) 
        clicker.send_click([100,100,200,200,200,300])
        print('click')

class click:
    def __init__(self) -> None:
        self.buffer=0
    def send_click(self,lineInfo):
        self.buffer=json.dumps({"EVENT":"CLICK", "x": lineInfo[4],"y": lineInfo[5]})
    
clicker = click()

async def detect(video_path):
    # Load stuff
    model = YOLO('yolov8n-seg.pt')
    detector = handy.handDetector(maxHands=1)
    fourcc = cv2.VideoWriter_fourcc(*'h264')
    out = cv2.VideoWriter('output.mp4v', fourcc, 20.0, (640,480))
    print("yolo")
    
    # Open the video file
    
    cap = cv2.VideoCapture(video_path)

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run inference on the frame
            results = model(frame)
            annotated_frame = results[0].plot()
            fingers=[0,0,0,0,0]
            img = detector.findHands(annotated_frame)
            fingers = detector.fingersUp()
            
            # Click mouse if distance between Index and middle fingers is short
            if fingers[1] == 1 and fingers[2] == 1:
                length, img, lineInfo = detector.findDistance(8, 12, img)           
                if length < 40:
                    #cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    clicker.send_click([lineInfo])
            #cv2.imshow("YOLOv8 Inference", img)
            out.write(img)
        else:
            # Break the loop if the end of the video is reached
            break


  
    cap.release()
    cv2.destroyAllWindows()




async def main():

    asyncio.create_task(detect(video_path))
    async with serve(handler, 'localhost', 8989):
        await asyncio.Future()  # run forever
asyncio.run(main())



 #refs
 # Priyansh Shankhdhar 2023
 # ultralytics 2023
