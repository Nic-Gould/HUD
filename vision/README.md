# Program Architecture
The YOLO family of models will be used as the object detection backbone of the CV process. Additional models are run as required e.g. pose estimation is undertaken only once a person has been identified by YOLO, and YOLO passes as an input only the image data returned within the bounding box identfying a person.
For embedded applications such as running on microcontrollers, the model must be converted to a TFLite model or similar TinyML models designed to run on such architectures.
Initial experiments with Tensorflow.js showed high latency which would affect performance, and limit use to areas with network connectivity. It would be possible to pair the device to a phone (for goggles, car) and use the phone as a companion processor and network hub.

## MODELS
* yolo-v5-tflite/tflite_model https://tfhub.dev/neso613/lite-model/yolo-v5-tflite/tflite_model/1
TF Lite quantized version of the Yolo-v5 for object detection. 
YOLOv5 is a family of object detection architectures and models pretrained on the COCO dataset and significantly outperform its previous state-of-the-art yolo models.

* movenet/multipose/lightning https://www.tensorflow.org/hub/tutorials/movenet predicts human joint locations of people in the image frame. can run at >30FPS on most modern laptops and detects up to 6 people simultaneously while achieving good performance. 

* YOLO v5 https://github.com/ultralytics/yolov5
* PyTorch Video classifier
https://github.com/facebookresearch/pytorchvideo
* PyVision
https://pytorch.org/vision/stable/models.html#object-detection-instance-segmentation-and-person-keypoint-detection
* Object detection
https://www.tensorflow.org/lite/examples/object_detection/overview
* Pose estimation
https://www.tensorflow.org/lite/examples/pose_estimation/overview
* Segmentation (this is much cooler than bounding boxes...) The model will create a mask over the target objects with high accuracy.
https://www.tensorflow.org/lite/examples/segmentation/overview

### Action classification
Video classification and image classification models both use images as inputs to predict the probabilities of those images belonging to predefined classes. However, a video classification model also processes the spatio-temporal relationships between adjacent frames to recognize the actions in a video.
For example, a video action recognition model can be trained to identify human actions like running, clapping, and waving. 
https://www.tensorflow.org/lite/examples/video_classification/overview

### Audio
* TensorFlow Lite Python audio classification example with Raspberry Pi.
https://github.com/tensorflow/examples/tree/master/lite/examples/sound_classification/raspberry_pi

* Voice-controlled robot model
https://github.com/atomic14/voice-controlled-robot/tree/main/model


### Android
* Facial detection and Sentiment analysis 
https://developers.google.com/ml-kit/vision/face-detection
* Object detection and classification.
https://developers.google.com/ml-kit/vision/image-labeling
* Object Detection and tracking
https://developers.google.com/ml-kit/vision/object-detection

* TensorFlow Lite Gesture Classification Android Example
https://github.com/tensorflow/examples/tree/master/lite/examples/gesture_classification/android
* Pose Detection https://developers.google.com/ml-kit/vision/pose-detection
* Segmentation https://developers.google.com/ml-kit/vision/selfie-segmentation


### Online services 
* TensorFlow.js https://www.tensorflow.org/js/models (not recommended due to latency issues)
* Google Cloud Vision https://cloud.google.com/vision/docs/features-list


# JARVIS
* BERT Question and Answer
https://www.tensorflow.org/lite/examples/bert_qa/overview

* Recommendation
https://www.tensorflow.org/lite/examples/recommendation/overview

* Smart reply
https://www.tensorflow.org/lite/examples/smart_reply/overview

# Compiling for ESP32
* Compiling for ESP32
https://towardsdatascience.com/tensorflow-meet-the-esp32-3ac36d7f32c7

* ESP32-CAM Object detection with Tensorflow.js
https://www.survivingwithandroid.com/esp32-cam-object-detection-tensorflow-js/

* How to use ESP32-CAM with Tensorflow.js
https://www.survivingwithandroid.com/esp32-cam-tensorflow-js/

### ESP32-CAM Machine Learning/Vision Tutorials
```
https://eloquentarduino.github.io/2020/01/image-recognition-with-esp32-and-arduino/
https://www.survivingwithandroid.com/tinyml-esp32-cam-edge-image-classification-with-edge-impulse/
https://www.youtube.com/watch?v=kZdIO82059E
https://dev.to/tkeyo/tinyml-machine-learning-on-esp32-with-micropython-38a6
```