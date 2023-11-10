# Digital Nishika N8000

## Why does this exist?

A few nights ago, I watched a youtube video titled:

        [Can I rebuild this 40 year old 3D camera into a digital one?](https://www.youtube.com/watch?v=_aofxbH0elo)

I thought this video would provide source code or maybe a parts list, but all that you could actually see of the camera being made was a picture of parts laid out on a table, a close-up shot of the battery, and a quick scroll-through of most of the code.

In dismay, I look to the comments, surely someone must be kind enough to have gone through this process and make an open-source project, right? Nope, I only find people asking for code and parts. Some even willing to pay money for it.

The truth of the matter, is that this camera is extremely simple to make in practice, but has a high ceiling for features you can add to it over time.

I found myself wanting to jump in on this project even with only the knowledge of what was included in the video.

Overtime, I plan on making a more elegant solution, but in the meantime this is only a hub for the original code that was included in the video and a list of parts that **(Having done no extensive research)** should work for running it.

## Current Concerns

#### Parts

The current parts list gives a few options for each part. This is because I have not done any more research into which parts are needed and which aren't further than what is shown in the video.

To my knowledge, these parts should work. However, I am not responsible if you buy parts from this list and they don't end up working together.

###### Arduino

The current selection of Raspberry Pis may be much more overpowered than is required for this project. I need to spend time looking into using something like a Pi Zero or maybe even a cheap microcontroller is all you'd need. 

###### Camera Hats

There are many options for Camera Hats, choosing one other than the one chosen in the video (unclear) may cause certain things in the code to run correctly. These are simple things to fix, but if you don't know how to code then it may be a challenge.

###### Cameras

The video says they use 16Mp cameras, but I could not find a Camarray Hat that included these cameras. 

I saw another example of one of these cameras using USB cameras. This most likely won't work the same way or how we'd want it, but it's worth looking more into other options to see what works best for the best cost.

#### Code

There are a few quick things I could fix about the code to get it all up and running, but I can't spend time or money on it until I start working in 2024.

I want to get this project to the point where you can create and use it like a genuine camera. That is going to take a lot more time as I would have to start from scratch, but is definitely an achievable goal.



## Resources

[Multi-Camera CamArray - Arducam Wiki](https://docs.arducam.com/Raspberry-Pi-Camera/Multi-Camera-CamArray/Multi-Camera-CamArray/)

[Quick Start Guide for Arducam CamArray HAT Kit - Arducam Wiki](https://docs.arducam.com/Raspberry-Pi-Camera/Multi-Camera-CamArray/quick-start/)

[Quick Start Guide for Multi-Camera Adapter Board - Arducam Wiki](https://docs.arducam.com/Raspberry-Pi-Camera/Multi-Camera-CamArray/Quick-Start-Guide-for-Multi-Adapter-Board/)







[Arduino Panorama Photography with ArduCAM - Arducam](https://www.arducam.com/arduino-panorama-photography-arducam/)

[ArduCAM porting for Raspberry Pi - Arducam](https://www.arducam.com/arducam-porting-raspberry-pi/)

https://github.com/ArduCAM/Arduino/blob/master/ArduCAM/examples/mini/ArduCAM_Mini_4CAM_Capture2SD/ArduCAM_Mini_4CAM_Capture2SD.ino



[Arducam Mini Multi-Camera Adapter Board for Arduino](https://www.uctronics.com/arducam-mini-multi-camera-adapter-board-for-arduino-raspberry-pi.html)

[Multi-Camera Adapter Board For Arduino - Arducam Wiki](https://docs.arducam.com/Arduino-SPI-camera/Legacy-SPI-camera/Multi-Camera-Adapter-Board-For-Arduino/)

[Arducam Shield Mini 5MP Plus - Arducam Wiki](https://docs.arducam.com/Arduino-SPI-camera/Legacy-SPI-camera/Hardware/Arducam-Shield-Mini-5MP-Plus/)







## Requirements

Minimize cost

Allow pictures to be stored individually, but also stiched together automatically in camera



## Stretch Goals

Make individual cameras rotate-able for portrait orientation wigglegrams?
