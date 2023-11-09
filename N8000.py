




# import GPIO
# import os
# Nothing before line 9 is shown
from gpiozero import Button
from signal import pause
import PySimpleGUI as sg
from threading import Thread


GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

button = Button(27)

GPIO.output(17, True)
sleep(1)
GPIO.output(17, False)

layout = [ [sg.Text("QuadCam is on!")]]

window = sg.Window('Quad Cam', layout)

def main():
    t = time.localtime(time.time())
    currentTime = time.strftime("%m-%d-%Y-%H:%M:%S", t)
    # TODO: Change to relative paths? Make option to not store original images if you just want the gif.
    folderPath = "/home/kentheckel/Desktop/Kentcamera/images/%s" % currentTime
    photoName = "capture_Main"
    GPIO.output(17, True)
    capture(photoName, currentTime, folderPath)
    GPIO.output(17, False)
    crop(photoName, folderPath)
    #cropAdjust(folderPath)
    #makeGif(folderPath)

def capture(photoName, currentTime, folderPath):

    newpath = folderPath
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    cmd = "libcamera-jpeg -o %s/%s.jpg -n --autofocus -f --quality 100" % (folderPath, photoName)
    os.system(cmd)

def crop(photoName, folderPath):
    originalImage = Image.open("%s/%s.jpg" % (folderPath, photoName))
    width, height = originalImage.size
#    adjustDistance = 300

    # TODO: Make this modular so that image width and height is determined when the program is run.
    # This probably currently depends on the cameras you use.
    imageWidth = 2328
    imageHeight = 1748

    # TODO: Clean this up with a loop
    left = 0
    top = 0
    right = width / 2
    bottom = height / 2

    crop1 = originalImage.crop((left, top, right, bottom))
    #crop1Final = crop1.crop((0, 14, imageWidth - 315, imageHeight))
    crop1.save("%s/crop1.jpg" % folderPath)

    left = width / 2
    top = 0
    right = width
    bottom = height / 2

    crop2 = originalImage.crop((left, top, right, bottom))
    #crop2Final = crop2.crop((315, 0, imageWidth, imageHeight - 14))
    crop2.save("%s/crop2.jpg" % folderPath)

    left = 0
    top = height / 2
    right = width / 2
    bottom = height

    crop3 = originalImage.crop((left, top, right, bottom))
    #crop3Final = crop3.crop((adjustDistance * 2, 0, width / 2 - adjustDistance, height)) # Note: This is cut off in the video, unsure if there is anything past 'height'
    crop3.save("%s/crop3.jpg" % folderPath)

    left = width / 2
    top = height / 2
    right = width
    bottom = height

    crop4 = originalImage.crop((left, top, right, bottom))
    #crop4Final = crop4.crop((adjustDistance * 3, 0, width / 2, height / 2))
    crop4.save("%s/crop4.jpg" % folderPath)

def makeGif(folderPath):
    images = []
    images.append(imageio.imread("%s/crop1.jpg" % folderPath))
    images.append(imageio.imread("%s/crop2.jpg" % folderPath))
    images.append(imageio.imread("%s/crop3.jpg" % folderPath))
    images.append(imageio.imread("%s/crop4.jpg" % folderPath))

    imageio.mimsave("%s/final.gif" % folderPath, images, fps=4)

def say_hello():
    if __name__ == '__main__':
        print("Running!")
        Thread(target = main).start()
        Thread(target = blink).start()
    #print("Running!")
    #main()
    GPIO.output(17, True)
    sleep(1)
    GPIO.output(17, False)

def blink():
    sleep(4)
    GPIO.output(17, True)
    sleep(0.5)
    GPIO.output(17, False)
    sleep(0.5)
    GPIO.output(17, True)
    sleep(0.5)
    GPIO.output(17, False)
    sleep(0.5)
    GPIO.output(17, True)
    sleep(0.5)
    GPIO.output(17, False)




# def mouseClick(x, y, button, pressed):
#    print(x, y)
#    mouseListener.stop()

# mouseListener = mouse.Listener(on_click=mouseClick)

# def cropAdjust(folderPath):
#     mouseListener.start()
#     image1 = Image.open("%s/crop1.jpg" % folderPath)
#     image1.show()

button.when_pressed = say_hello
# main()

event, values = window.read()

# There is a comment at the bottom of the page which is a copy-paste of usage of running a command. It doesn't seem necessary
# See 10:12 in the video for the comment at the bottom of the page