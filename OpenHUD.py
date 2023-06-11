import asyncio
from websockets.server import serve

import cv2
from ultralytics import YOLO
import vision.handy as handy
import json

video_path = "http://statenisland.dnsalias.net/mjpg/video.mjpg"
#"192.168.1.109:81/stream"  # default esp32cam output for testing
    # img_resp=urllib.request.urlopen(url)
    # imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    # img=cv2.imdecode(imgnp,-1)
    


async def handler(websocket):
    print("server loaded")
    while True:
        if clicker.buffer !=0:
            await websocket.send(clicker.buffer)
            clicker.buffer=0
       # msg = await websocket.recv()    
       # print(msg)
        

class click:
    def __init__(self) -> None:
        self.buffer=0
    def send_click(self,lineInfo):
        self.buffer=json.dumps({"EVENT":"CLICK", "x": lineInfo[4],"y": lineInfo[5]})
    
clicker = click()

""" async def dummy_click():
    while True:
        await asyncio.sleep(5) 
        clicker.send_click([100,100,200,200,200,300])
        print('click')
 """
async def hands(detector, frame):
    fingers=[0,0,0,0,0]
    img = detector.findHands(frame)
    lmList, _ = detector.findPosition(img)
    
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingersUp()

        # Click mouse if distance between Index and middle fingers is short
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)           
            if length < 40:
                #cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                clicker.send_click([lineInfo])


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
            print("operation big success")
            # Run inference on the frame
            results = model(frame)
            hands(detector, frame)      
            #cv2.imshow("YOLOv8 Inference", img)
            annotated_frame = results[0].plot(boxes=False, labels=False, masks=True, probs = False)
            out.write(annotated_frame)
        else:
            # Break the loop if the end of the video is reached
            break
    cap.release()
    cv2.destroyAllWindows()

async def web():
    async with serve(handler, 'localhost', 8989):
        await asyncio.Future() 
  
async def main():
    asyncio.gather(detect(video_path))
asyncio.run(main())


 #refs
 # Priyansh Shankhdhar 2023
 # ultralytics 2023
