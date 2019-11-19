#Images_Starting_Code_Edited
#Kyle Fricke and Cheryl Farmer, Engineer Your World (Edited by Samuel Rothstein)
#Takes a file as input by the user, colors it, and produces an original, grayscale, custom, and individually colored versions

#Import libraries
import cv2
import numpy
import os.path

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

#Create 5 windows, for the original, grayscale, each color, and custom
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Color 0 Parts of Image')
cv2.namedWindow('Color 1 Parts of Image')
cv2.namedWindow('Customized Image')

#Record image dimensions
img_height = og_img.shape[0]
img_width = og_img.shape[1]
img_channels = og_img.shape[2]

#Create 'papers' as arrays for each color
color0_paper = numpy.zeros((img_height,img_width,img_channels), numpy.uint8)
color1_paper = numpy.zeros((img_height,img_width,img_channels), numpy.uint8)
#Color each paper
color0_paper[0:img_height,0:img_width, 0:img_channels] = [0,0,255]
color1_paper[0:img_height,0:img_width, 0:img_channels] = [0,255,255]

#The grayscale breaks between colors
gs_break0 = 100

#Define ranges of grayscale where each color will be painted based on grayscale breaks
color0_min = [0,0,0]
color0_max = [gs_break0,gs_break0,gs_break0]
color1_min = [gs_break0+1,gs_break0+1,gs_break0+1]
color1_max = [255,255,255]

color0_min = numpy.array(color0_min, dtype = "uint8")
color0_max = numpy.array(color0_max, dtype = "uint8")
color1_min = numpy.array(color1_min, dtype = "uint8")
color1_max = numpy.array(color1_max, dtype = "uint8")

#Create mask for each color where it will not be painted, and return only the part that will be painted
color0_mask = cv2.inRange(gs_img, color0_min, color0_max)
color1_mask = cv2.inRange(gs_img, color1_min, color1_max)

color0_part = cv2.bitwise_or(color0_paper, color0_paper, mask = color0_mask)
color1_part = cv2.bitwise_or(color1_paper, color1_paper, mask = color1_mask)

#Add each colors part to create one custom image
custom_img = cv2.bitwise_or(color0_part, color1_part)

#Show each image (original, grayscale, each color, custom) in a seperate window
cv2.imshow('Original Image', og_img)
cv2.imshow('Grayscale Image',gs_img)
cv2.imshow('Color 0 Parts of Image',color0_part)
cv2.imshow('Color 1 Parts of Image',color1_part)
cv2.imshow('Customized Image',custom_img)

#Keep windows open. If esc is pressed, close all windows; if s is pressed, save the grayscale and custom images then close all windows
keypressed = cv2.waitKey(0)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',gs_img)
    cv2.imwrite('photo_RY_1.jpg',custom_img)
    cv2.destroyAllWindows()