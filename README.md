# Digital Nishika N8000

## Why does this exist?

A few nights ago, I watched a youtube video titled:

        [Can I rebuild this 40 year old 3D camera into a digital one?](https://www.youtube.com/watch?v=_aofxbH0elo)

I thought this video would provide source code or maybe a parts list, but all that you could actually see of the camera being made was a picture of parts laid out on a table, a close-up shot of the battery, and a quick scroll-through of most of the code.

In dismay, I look to the comments, surely someone must be kind enough to have gone through this process and make an open-source project, right? Nope, I only find people asking for code and parts. Some even willing to pay money for it.

The truth of the matter, is that this camera is extremely simple to make in practice, but has a high ceiling for features you can add to it over time.

I found myself wanting to jump in on this project even with only the knowledge of what was included in the video.

Over time, I plan on making a more elegant solution, but in the meantime this is only a hub for the original code that was included in the video and a list of parts that **(Having done no extensive research)** should work for running it.

## Info

#### Parts

I have decided to use a Raspberry Pi Zero for this project because I had one laying around and it is all that is needed for such a low complexity application. The goal is to make a kiosk OS that will work like an actual camera with a simple UI. Eventually I will make it work for the Pi Zero 2 as well.

The Camera Array was chosen because of its low cost and diverse choice of cameras/lenses available. Buying each camera individually is a pain, but allows for easier replacability in case one stops working or is DOA. 

There are two choices for Arducams (OV2640 and OV5642). The goal is for both of these to work automatically with the final program. 

You can also buy better lenses for these Arducam models. Any M12 Lens should work (Don't take my word for it). This will hopefully make the camera suitable for more professional photography. 

A Screen for the camera has not been chosen at this time, but will be at some point in the future. 

#### Code

I am currently working on a simple FLTK CPP Kiosk program that I can run on the Raspberry pi that will take pictures and store them automatically. The goal is for this program to grow much larger in the future with custom settings and various shooting options. 

## Resources

[Arduino Panorama Photography with ArduCAM - Arducam](https://www.arducam.com/arduino-panorama-photography-arducam/)

[ArduCAM porting for Raspberry Pi - Arducam](https://www.arducam.com/arducam-porting-raspberry-pi/)

[Multi-Camera Adapter Board For Arduino - Arducam Wiki](https://docs.arducam.com/Arduino-SPI-camera/Legacy-SPI-camera/Multi-Camera-Adapter-Board-For-Arduino/)

[Arducam Shield Mini 5MP Plus - Arducam Wiki](https://docs.arducam.com/Arduino-SPI-camera/Legacy-SPI-camera/Hardware/Arducam-Shield-Mini-5MP-Plus/)

https://github.com/ArduCAM/Arduino/tree/master/ArduCAM/examples/RaspberryPi

[How to use a Raspberry Pi in kiosk mode - Raspberry Pi](https://www.raspberrypi.com/tutorials/how-to-use-a-raspberry-pi-in-kiosk-mode/)

Lenses

[Arducam M12 Lens Set, Arducam Lens for Raspberry Pi Camera (1/4&#039;) and Arduino, Telephoto, Macro, Wide Angle, Fisheye Lens Kit (10°- 200°) with M12 Lens Holder and Cleaning Cloth, Optical All-in-One](https://www.uctronics.com/lk001.html)

[Arducam Low Distortion M12 Lens Set for Rapsberry Pi Cameras and Arduino Cameras](https://www.uctronics.com/arducam-m12-lens-raspberry-pi-low-distortion.html)

Example Code

2MP - https://github.com/ArduCAM/Arduino/blob/master/ArduCAM/examples/RaspberryPi/arducam_ov2640_4cams_capture.cpp

[Backup Version](./Example Code/arducam_ov2640_4cams_capture.cpp)

5MP - https://github.com/ArduCAM/Arduino/blob/master/ArduCAM/examples/RaspberryPi/arducam_ov5642_4cams_capture.cpp

[Backup Version](./Example Code/arducam_ov5642_4cams_capture.cpp)

## Requirements

Minimize cost of parts

Allow high level of modularity for different levels of investment

Allow pictures to be stored individually, but also stiched together automatically in camera

## Stretch Goals

Make individual cameras rotate-able for portrait orientation wigglegrams
