import cv2
from ultralytics import YOLO
import vision.handy as handy

buffer = handy.buffer


video_path = "http://statenisland.dnsalias.net/mjpg/video.mjpg"

def labels(results)->list:
    detections = results[0].boxes.cls.data.numpy()
    names= results[0].names
    labels=[]
    for detection in detections:
        labels.append(names[detection])
    return labels
# Loop through the video frames

def yolo(model, frame):
    results = model(frame)
    # Visualize the results on the frame
    annotated_frame = results[0].plot(boxes=False, labels=False, masks=True, probs = False)
    buffer.stream=annotated_frame
    buffer.labels = labels(results)
    #print(labs)
    # Display the annotated frame
    cv2.imshow("YOLOv8 Inference", annotated_frame)
       
def detect():
    model = YOLO('yolov8n-seg.pt')
    detector =  handy.handDetector(maxHands=1)
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            yolo(model,frame)
            handy.hands(detector,frame)
    # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break      

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()
