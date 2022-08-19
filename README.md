# OpenHUD
OpenHUD is a project that aims to provide an AR overlay for everyday use. The HUD consists of widgets which are overlaying an FPV feed. Current feeds that are available are
##   .life
##  .drive
##   .fly

 ------------
# OpenHUDware
OpenHUDware is open source development hardware for OpenHUD application. 
##  .car
## .self
## .sky
--------------

## .intro

OpenHUD is based on the idea of fpv drone racing to overlay live video with critical information. Rather than using VR/AR for game-like interactions, OpenHUD approaches AR as an interface to enhance our experience of life. OpenHUD overlays a live camera stream with additional data about what is in view based on pretrained computer vision modules such as (Google vision API, Pre trained TF models, etc). This project investigated several widely available ML and CV APIs to provide overlay features. The tags that are returned are used to determine what funtions to undertake next. Such as:
* user generated search
* transition between classifier models
* additional sensor data, or sensor filtering and analysis. 

OpenHUD uses the classification tags to transition between classifier models. For example when the object recognition model returns "person" the following things happen. 
* the facial recognition model is launched
* stance is assessed
* facial analysis is undertaken to provide sentiment analysis 
* audio is enhanced using directional mic and filtering background.
* audio is also analysed
* if the person is known, all relevant information will be loaded. Linking to the users facebook account could provide most of these details. Along with phone contacts. The information is loaded into the info pane which is a default widget located in the right 'drawer' of the HUD (this can be changed in settings). 
* Events are also triggered for things like links, qr codes, plant ID, ect. and are relevant to the location. 

If the tag that was returned was "CD" different events may be loaded like spotify search using OCR or something similar. 

## OpenHUD.life
Here's a *mock-up* of the OpenHUD.life overlay with the results pane and app drawer open. In this example the facial recognition classifier has loaded information from the user's linked facebook account. There is also classifier data for sentiment analysis. Suggested actions are also presented to the user. 

![alt text](./images/OpenHUD.self "OpenHUD.self mockup")


**UserInteraction()**

The CV generated tags and bounding boxes are presented to the user  who can choose what further funtions or apps to launch. this can be done by making the mouse pointer gesture with your hand and clicking on the item as you see it in your goggles, or making the speach command gesture to give a verbal command. OpenHUD also uses ML to learn what you like and pre-cache information and data that's more relevant to the user. 

##	OpenHUD.drive
Addional envinmental awareness for road safety. There are plenty of existing vehicle HUDs that demostrate this idea. Sensor/360cam sensor data integrated into hud. If the car is self driving (this can be done pretty easily at a non-commercial level using ArduPilot(ROVER) as a test case), then additional functionality can be unlocked such as landmark info and context pane. The reference design for OpenHUD.drive is [OpenHUDware.car](https://github.com/Nic-Gould/Car).

![alt text](./images/OpenHUD.car "OpenHUD.car")

# OpenHUDware
## 	OpenHUDware.self
Like fpvcam/VR goggles but with front cam, environmental sensors. Display a customisable dashboard. Weather widget, hud apps. Additional environmental awareness such as facial recognition, mood detection, low light filters, zoom, directional mic? Track hand, gensture input, on hud items. Repo [here](https://github.com/Nic-Gould/Goggles)
       
## OpenHUDware.car

An opensource electric buggy with self-driving capabilities. Check out my [other repo](https://github.com/Nic-Gould/Car). Don't drive this thing on public roads. I'm looking at getting this approved under the Street Rod certification program once completed. Control system is, again, based on drones.

## OpenHUDware.sky
This was my first DIY drone. Built on the cheap using an untested flight controller I banged together out of a couple of dev boards and the ARDUPILOT code. Repo [here](https://github.com/Nic-Gould/Drone)
       
