import Image

#Opens the camera image. Compresses it to only include 20 colours.
cameraImage = Image.open('boxwithball.jpg').convert('P', palette=Image.ADAPTIVE, colors=20).convert('RGB')
#Saves the image (only needed for testing)
cameraImage.save('test.png')
#Saves the RGB values of the colours in the image to a list
imageColours = cameraImage.getcolors(256)

#Iterates through the list of colours in the image
for colour in imageColours:
    #If the colour is red (The call is in the image)
    if colour[1][0] > 140 and colour[1][1] < 120 and colour[1][2] < 120:
        #Prints a message
        print 'Ball in picture'

print 'End Line Geoffrey Robot'