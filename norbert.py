import Image
import RPi.GPIO as gpio
import time
import random
import subprocess

def takePicture():
    devNull = open('/dev/null', 'w')#used to output the fswebcam stdout and stderr
    cameraCommand = subprocess.Popen(["fswebcam", "-r", "356x292", "-d", "/dev/video0", "image.jpg", "--skip", "10"], stdout=devNull, stderr=devNull)
    cameraCommand.communicate()
    cameraImage = Image.open('image.jpg').convert('P', palette=Image.ADAPTIVE, colors=20).convert('RGB')
    cameraImage.save('test.png')
    imageColours = cameraImage.getcolors(256)
    for colour in imageColours:
        if colour[1][0] > 140 and colour[1][1] < 120 and colour[1][2] < 120:
            print 'Ball in picture'
        else:
            print 'Ball not in the picture'

def forward(seconds, freq):
    startTime = time.time()
    while time.time() < startTime + seconds:
        p2.start(freq)
        p4.start(freq)
    p2.start(0)
    p4.start(0)

def backwards(seconds, freq):
    startTime = time.time()
    while time.time() < startTime + seconds:
        p.start(freq * 2.5)
        p3.start(freq * 2.5)
    p.start(0)
    p3.start(0)

def right(seconds, freq):
    startTime = time.time()
    while time.time() < startTime + seconds:
        p2.start(freq)
    p2.start(0)

def left(seconds, freq):
    startTime = time.time()
    while time.time() < startTime + seconds:
        p4.start(freq)
    p4.start(0)

def wander():
    randommove = random.randint(1,2)
    randomtrun = float(random.randint(1,6)) / 6
    forward(2, 40)
    if randommove == 1:
        left(randomtrun, 40)
    else:
        right(randomtrun, 40)
    print "TAKE PICTURE"


def stop():
    gpio.output(16, False)
    gpio.output(18, False)
    gpio.output(24, False)
    gpio.output(22, False)
    time.sleep(2)

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

p = gpio.PWM(16, 100)
p2 =  gpio.PWM(18, 100)
p3 = gpio.PWM(22, 100)
p4 = gpio.PWM(24, 100)

takePicture()
# try:
#     while True:
#         wander()
# except KeyboardInterrupt:
#     GPIO.cleanup()          # clean up GPIO on CTRL+C exit


print 'End Line Norbert Robot'
