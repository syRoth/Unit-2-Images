import cv2
import numpy
import os.path

#Create color class
class Color:
    def __init__(self,r,g,b,name,Max,Min):
        self.r = r
        self.g = g
        self.b = b
        self.name = name
        self.max = Max
        self.min = Min
    paper = []
    mask = 0
    part = 0
    gs_break = 0

#Initialize colors
color0 = Color(255,0,0,'0',125,0)
color1 = Color(0,255,0,'1',255,126)
color2 = Color(0,0,255,'2',255,126)

#Add all created colors to color list
colors = [color0,color1,color2]

#Get file from user and check if it exists
print "Save your original image in the same folder as this program."
#Originally assume the file does not exist
filename_valid = False
while filename_valid == False:
    filename = raw_input("Enter the name of your file, including the "\
                                "extension, and then press 'enter': ")
    #If the file does exist, change its existence to true
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
    #If the file does not exist, tell user to input a new file
        print("Something was wrong with that filename. Please try again.")

#Create the original image, grayscale simple, and grayscale
og_img = cv2.imread(filename,1)
gs_img_simple = cv2.imread(filename, 0)
gs_img = cv2.cvtColor(gs_img_simple, cv2.COLOR_GRAY2BGR)

#Create original image, grayscale image, grayscale slider, and custom image windows
cv2.namedWindow('Original Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original Image',300,300)
cv2.namedWindow('Grayscale Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Grayscale Image',300,300)
cv2.namedWindow('Grayscale Sliders')
cv2.resizeWindow('Grayscale Sliders',350,250)
cv2.namedWindow('Customized Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Customized Image',600,600)

#For each color, create a component trackbar window
for color in colors:
    cv2.namedWindow('Color ' + color.name + ' Components')
    cv2.resizeWindow('Color ' + color.name + ' Components',350,150)
    
#Show the original and grayscale images, only done once so this is not in the loop
cv2.imshow('Original Image', og_img)
cv2.imshow('Grayscale Image',gs_img)

#Get the image dimensions
img_height = og_img.shape[0]
img_width = og_img.shape[1]
img_channels = og_img.shape[2]

for color in colors:
    #Create paper with same dimensions as image
    color.paper = numpy.zeros((img_height, img_width, img_channels), numpy.uint8)

    #Create trackbar for each component of the color (red, green, blue)
    cv2.createTrackbar('Color' + color.name + '_R','Color ' + color.name + ' Components', color.r, 255, lambda x:None)
    cv2.createTrackbar('Color' + color.name + '_G','Color ' + color.name + ' Components', color.g, 255, lambda x:None)
    cv2.createTrackbar('Color' + color.name + '_B','Color ' + color.name + ' Components', color.b, 255, lambda x:None)

i = 0
gs_breaks = list(range(len(colors)-1))
while i < len(gs_breaks):
    cv2.createTrackbar('GS'+str(i)+'_position','Grayscale Sliders', 0, 255, lambda x:None)
    i+=1

keypressed = 1
#Run until user presses 'esc' or 's'
while (keypressed != 27 and keypressed != ord('s')):
    custom_img = 0
    
    #Update grayscale break positions
    i = 0
    while i < len(gs_breaks):
        gs_breaks[i] = cv2.getTrackbarPos('GS'+str(i)+'_position','Grayscale Sliders')
    
    for color in colors:
        #Update the color components by taking the positions of the trackbars
        color.r = cv2.getTrackbarPos('Color' + color.name + '_R','Color '+ color.name + ' Components')
        color.g = cv2.getTrackbarPos('Color' + color.name + '_G','Color '+ color.name + ' Components')
        color.b = cv2.getTrackbarPos('Color' + color.name + '_B','Color '+ color.name + ' Components')
        
        #Color the paper
        color.paper[0:img_height, 0:img_width, 0:img_channels] = [color.b,color.g,color.r]

        if color.name == '0':
            color.min = [0,0,0]
        else:
            color.min = [gs_breaks[int(color.name)-1]+1,gs_breaks[int(color.name)-1]+1,gs_breaks[int(color.name)-1]+1]
        
        if int(color.name) == (len(colors)-1):
            color.max = [255,255,255]
        else:
            color.max = [gs_breaks[int(color.name)],gs_breaks[int(color.name)],gs_breaks[int(color.name)]]
        
        #Update the maximum and minimum grayscale values for which the paper will color
        color.min = numpy.array(color.min, dtype = "uint8")
        color.max = numpy.array(color.max, dtype = "uint8")

        color.mask = cv2.inRange(gs_img, color.min, color.max)
        color.part = cv2.bitwise_or(color.paper, color.paper, mask = color.mask)
        
        #Add the colored part to the image
        custom_img = cv2.bitwise_or(custom_img,color.part)
    
    #Show the updated custom image
    cv2.imshow('Customized Image', custom_img)
    
    #Wait for the user to press a key
    keypressed = cv2.waitKey(1)
    
#If the user pressed 'esc'    
if keypressed == 27:
    cv2.destroyAllWindows()