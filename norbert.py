import Image
import RPi.GPIO as gpio
import time

def takePicture():
    cameraImage = Image.open('boxwithball.jpg').convert('P', palette=Image.ADAPTIVE, colors=20).convert('RGB')
    cameraImage.save('test.png')
    imageColours = cameraImage.getcolors(256)
    for colour in imageColours:
        if colour[1][0] > 140 and colour[1][1] < 120 and colour[1][2] < 120:
            print 'Ball in picture'

def forward(seconds):
    startTime = time.time()
    while time.time() < startTime + seconds:
        gpio.output(16, False)
        gpio.output(18, True)
        gpio.output(24, True)
        gpio.output(22, False)
        time.sleep(0.01)

def backwards(seconds):
    gpio.output(16, True)
    gpio.output(18, False)
    gpio.output(24, False)
    gpio.output(22, True)
    time.sleep(seconds)

def stop():
    gpio.output(16, False)
    gpio.output(18, False)
    gpio.output(24, False)
    gpio.output(22, False)
    time.sleep(seconds)

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(24, gpio.OUT)

gpio.output(7, True)
gpio.output(11, True)
gpio.output(13, True)
gpio.output(15, True)

forward(7)
stop()

print 'End Line Norbert Robot'