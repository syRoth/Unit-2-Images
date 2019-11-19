#Images_Starting_Code_Edited
#Kyle Fricke and Cheryl Farmer, Engineer Your World (Edited by Samuel Rothstein)
#Takes a file as input by the user, colors it, and produces an original, grayscale, custom, and individually colored versions
#Use a slider bar to change grayscale break values
#COLORS ARE BGR

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

#Read file for saving color and grayscale settings
filename_valid = False
while filename_valid == False:
    preset_filename = raw_input("Enter a preset to open, including extension, and then press 'enter': ")
    #Check if file exists
    if os.path.isFile(preset_filename) == True:
        filename_valid = True
    #If file does not exist, make user try again
    else:
        print("Somthing was wrong with that filename. Please try again.")

#Open up a file using preset file given
presetFile = open(preset_filename,"r")
color_components = list(range(18))
gs_breaks = list(range(5))

#For each color component in the file, assign that value to the corresponding color variable
i = 0
while i < len(color_components):
    color_components[i] = int(presetFile.readline().rstrip("\n"))
    i += 1
    
#For each grayscale break in the file, assign that value to the corresponding grayscale break variable
i = 0
while i < len(gs_breaks):
    gs_breaks[i] = int(presetFile.readline().rstrip("\n"))
    i+=1
presetFile.close()

#Set each color component and grayscale breaks using corresponding data from preset file
color0_R = color_components[0]
color0_G = color_components[1]
color0_B = color_components[2]
color1_R = color_components[3]
color1_G = color_components[4]
color1_B = color_components[5]
color2_R = color_components[6]
color2_G = color_components[7]
color2_B = color_components[8]
color3_R = color_components[9]
color3_G = color_components[10]
color3_B = color_components[11]
color4_R = color_components[12]
color4_G = color_components[13]
color4_B = color_components[14]
color5_R = color_components[15]
color5_G = color_components[16]
color5_B = color_components[17]
gs_break0 = gs_breaks[0]
gs_break1 = gs_breaks[1]
gs_break2 = gs_breaks[2]
gs_break3 = gs_breaks[3]
gs_break4 = gs_breaks[4]

#Create windows, for the original, grayscale, each color, and custom
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
 
cv2.namedWindow('Grayscale Sliders')
cv2.resizeWindow('Grayscale Sliders',350,250)

cv2.namedWindow('Color 0 Components')
cv2.resizeWindow('Color 0 Components',350,150)
cv2.namedWindow('Color 1 Components')
cv2.resizeWindow('Color 1 Components',350,150)
cv2.namedWindow('Color 2 Components')
cv2.resizeWindow('Color 2 Components',350,150)
cv2.namedWindow('Color 3 Components')
cv2.resizeWindow('Color 3 Components',350,150)
cv2.namedWindow('Color 4 Components')
cv2.resizeWindow('Color 4 Components',350,150)
cv2.namedWindow('Color 5 Components')
cv2.resizeWindow('Color 5 Components',350,150)

cv2.namedWindow('Color 0 Part')
cv2.namedWindow('Color 1 Part')
cv2.namedWindow('Color 2 Part')
cv2.namedWindow('Color 3 Part')
cv2.namedWindow('Color 4 Part')
cv2.namedWindow('Color 5 Part')

cv2.namedWindow('Customized Image',cv2.WINDOW_NORMAL)

#Show original and grayscale image
cv2.imshow('Original Image', og_img)
cv2.imshow('Grayscale Image',gs_img)

#Record image dimensions
img_height = og_img.shape[0]
img_width = og_img.shape[1]
img_channels = og_img.shape[2]

#Create 'papers' as arrays for each color
color0_paper = numpy.zeros((img_height, img_width, img_channels), numpy.uint8)
color1_paper = numpy.zeros((img_height, img_width, img_channels), numpy.uint8)
color2_paper = numpy.zeros((img_height, img_width, img_channels), numpy.uint8)
color3_paper = numpy.zeros((img_height, img_width, img_channels), numpy.uint8)
color4_paper = numpy.zeros((img_height, img_width, img_channels), numpy.uint8)
color5_paper = numpy.zeros((img_height, img_width, img_channels), numpy.uint8)

#Create trackbars for grayscale breaks
cv2.createTrackbar('GS0_position','Grayscale Sliders', gs_break0, 255, lambda x:None)
cv2.createTrackbar('GS1_position','Grayscale Sliders', gs_break1, 255, lambda x:None)
cv2.createTrackbar('GS2_position','Grayscale Sliders', gs_break2, 255, lambda x:None)
cv2.createTrackbar('GS3_position','Grayscale Sliders', gs_break3, 255, lambda x:None)
cv2.createTrackbar('GS4_position','Grayscale Sliders', gs_break4, 255, lambda x:None)

#Create trackbars for color components
#Color 0
cv2.createTrackbar('color0_R','Color 0 Components', color0_R, 255, lambda x:None)
cv2.createTrackbar('color0_G','Color 0 Components', color0_G, 255, lambda x:None)
cv2.createTrackbar('color0_B','Color 0 Components', color0_B, 255, lambda x:None)
#Color 1
cv2.createTrackbar('color1_R','Color 1 Components', color1_R, 255, lambda x:None)
cv2.createTrackbar('color1_G','Color 1 Components', color1_G, 255, lambda x:None)
cv2.createTrackbar('color1_B','Color 1 Components', color1_B, 255, lambda x:None)
#Color 2
cv2.createTrackbar('color2_R','Color 2 Components', color2_R, 255, lambda x:None)
cv2.createTrackbar('color2_G','Color 2 Components', color2_G, 255, lambda x:None)
cv2.createTrackbar('color2_B','Color 2 Components', color2_B, 255, lambda x:None)
#Color 3
cv2.createTrackbar('color3_R','Color 3 Components', color3_R, 255, lambda x:None)
cv2.createTrackbar('color3_G','Color 3 Components', color3_G, 255, lambda x:None)
cv2.createTrackbar('color3_B','Color 3 Components', color3_B, 255, lambda x:None)
#Color 4
cv2.createTrackbar('color4_R','Color 4 Components', color4_R, 255, lambda x:None)
cv2.createTrackbar('color4_G','Color 4 Components', color4_G, 255, lambda x:None)
cv2.createTrackbar('color4_B','Color 4 Components', color4_B, 255, lambda x:None)
#Color 5
cv2.createTrackbar('color5_R','Color 5 Components', color5_R, 255, lambda x:None)
cv2.createTrackbar('color5_G','Color 5 Components', color5_G, 255, lambda x:None)
cv2.createTrackbar('color5_B','Color 5 Components', color5_B, 255, lambda x:None)



#Initialize while loop and loop control variable
keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):
    #Update the grayscale breaks between colors
    gs_break0 = cv2.getTrackbarPos('GS0_position','Grayscale Sliders')
    gs_break1 = cv2.getTrackbarPos('GS1_position','Grayscale Sliders')
    gs_break2 = cv2.getTrackbarPos('GS2_position','Grayscale Sliders')
    gs_break3 = cv2.getTrackbarPos('GS3_position','Grayscale Sliders')
    gs_break4 = cv2.getTrackbarPos('GS4_position','Grayscale Sliders')
    
    #Update the components of each color
    #Color 0
    color0_R = cv2.getTrackbarPos('color0_R','Color 0 Components')
    color0_G = cv2.getTrackbarPos('color0_G','Color 0 Components')
    color0_B = cv2.getTrackbarPos('color0_B','Color 0 Components')
    #Color 1
    color1_R = cv2.getTrackbarPos('color1_R','Color 1 Components')
    color1_G = cv2.getTrackbarPos('color1_G','Color 1 Components')
    color1_B = cv2.getTrackbarPos('color1_B','Color 1 Components')
    #Color 2
    color2_R = cv2.getTrackbarPos('color2_R','Color 2 Components')
    color2_G = cv2.getTrackbarPos('color2_G','Color 2 Components')
    color2_B = cv2.getTrackbarPos('color2_B','Color 2 Components')
    #Color 3
    color3_R = cv2.getTrackbarPos('color3_R','Color 3 Components')
    color3_G = cv2.getTrackbarPos('color3_G','Color 3 Components')
    color3_B = cv2.getTrackbarPos('color3_B','Color 3 Components')
    #Color 4
    color4_R = cv2.getTrackbarPos('color4_R','Color 4 Components')
    color4_G = cv2.getTrackbarPos('color4_G','Color 4 Components')
    color4_B = cv2.getTrackbarPos('color4_B','Color 4 Components')
    #Color 5
    color5_R = cv2.getTrackbarPos('color5_R','Color 5 Components')
    color5_G = cv2.getTrackbarPos('color5_G','Color 5 Components')
    color5_B = cv2.getTrackbarPos('color5_B','Color 5 Components')
    
    #Recolor each paper
    color0_paper[0:img_height, 0:img_width, 0:img_channels] = [color0_B,color0_G,color0_R]
    color1_paper[0:img_height, 0:img_width, 0:img_channels] = [color1_B,color1_G,color1_R]
    color2_paper[0:img_height, 0:img_width, 0:img_channels] = [color2_B,color2_G,color2_R]
    color3_paper[0:img_height, 0:img_width, 0:img_channels] = [color3_B,color3_G,color3_R]
    color4_paper[0:img_height, 0:img_width, 0:img_channels] = [color4_B,color4_G,color4_R]
    color5_paper[0:img_height, 0:img_width, 0:img_channels] = [color5_B,color5_G,color5_R]
    
    #Define ranges of grayscale where each color will be painted based on grayscale breaks
    color0_min = [0,0,0]
    color0_max = [gs_break0,gs_break0,gs_break0]
    
    color1_min = [gs_break0+1,gs_break0+1,gs_break0+1]
    color1_max = [gs_break1,gs_break1,gs_break1]

    color2_min = [gs_break1+1,gs_break1+1,gs_break1+1]
    color2_max = [gs_break2,gs_break2,gs_break2]
    
    color3_min = [gs_break2+1,gs_break2+1,gs_break2+1]
    color3_max = [gs_break3,gs_break3,gs_break3]
    
    color4_min = [gs_break3+1,gs_break3+1,gs_break3+1]
    color4_max = [gs_break4,gs_break4,gs_break4]
    
    color5_min = [gs_break4+1,gs_break4+1,gs_break4+1]
    color5_max = [255,255,255]
    
    #Numpy array for min and max of colors
    color0_min = numpy.array(color0_min, dtype = "uint8")
    color0_max = numpy.array(color0_max, dtype = "uint8")
    color1_min = numpy.array(color1_min, dtype = "uint8")
    color1_max = numpy.array(color1_max, dtype = "uint8")
    color2_min = numpy.array(color2_min, dtype = "uint8")
    color2_max = numpy.array(color2_max, dtype = "uint8")
    color3_min = numpy.array(color3_min, dtype = "uint8")
    color3_max = numpy.array(color3_max, dtype = "uint8")
    color4_min = numpy.array(color4_min, dtype = "uint8")
    color4_max = numpy.array(color4_max, dtype = "uint8")
    color5_min = numpy.array(color5_min, dtype = "uint8")
    color5_max = numpy.array(color5_max, dtype = "uint8")
    
    #Create mask for each color where it will not be painted, and return only the part that will be painted
    color0_mask = cv2.inRange(gs_img, color0_min, color0_max)
    color1_mask = cv2.inRange(gs_img, color1_min, color1_max)
    color2_mask = cv2.inRange(gs_img, color2_min, color2_max)
    color3_mask = cv2.inRange(gs_img, color3_min, color3_max)
    color4_mask = cv2.inRange(gs_img, color4_min, color4_max)
    color5_mask = cv2.inRange(gs_img, color5_min, color5_max)
    
    color0_part = cv2.bitwise_or(color0_paper, color0_paper, mask = color0_mask)
    color1_part = cv2.bitwise_or(color1_paper, color1_paper, mask = color1_mask)
    color2_part = cv2.bitwise_or(color2_paper, color2_paper, mask = color2_mask)
    color3_part = cv2.bitwise_or(color3_paper, color3_paper, mask = color3_mask)
    color4_part = cv2.bitwise_or(color4_paper, color4_paper, mask = color4_mask)
    color5_part = cv2.bitwise_or(color5_paper, color5_paper, mask = color5_mask)
    
    #Add each colors part to create one custom image
    custom_img = cv2.bitwise_or(cv2.bitwise_or(cv2.bitwise_or(cv2.bitwise_or(cv2.bitwise_or(color0_part, color1_part), color2_part), color3_part), color4_part), color5_part)
    
    #Show each color and custom image in a seperate window
    
    cv2.imshow('Color 0 Part',color0_part)
    cv2.imshow('Color 1 Part',color1_part)
    cv2.imshow('Color 2 Part',color2_part)
    cv2.imshow('Color 3 Part',color3_part)
    cv2.imshow('Color 4 Part',color4_part)
    cv2.imshow('Color 5 Part',color5_part)
    
    cv2.imshow('Customized Image',custom_img)

    #Keep windows open. If esc is pressed, close all windows; if s is pressed, save the grayscale and custom images then close all windows
    keypressed = cv2.waitKey(1)
    
#If esc is pressed, destroy all windows without saving
if keypressed == 27:
    cv2.destroyAllWindows()
#If s is pressed, save grayscale and custom images
elif keypressed == ord('s'): 
    #Destroy all windows and save grayscale image
    cv2.destroyAllWindows()
    cv2.imwrite('photo_GS_1.jpg',gs_img)
    
    #Save preset under a custom filename
    preset_filename = raw_input("Enter a name to save your preset under, including the extension, and then press 'enter': ")
    presetFile = open(preset_filename,"w")
    color_components = [color0_R,color0_G,color0_B, color1_R,color1_G,color1_B, color2_R,color2_G,color2_B, color3_R,color3_G,color3_B, color4_R,color4_G,color4_B, color5_R,color5_G,color5_B]
    gs_breaks = [gs_break0,gs_break1,gs_break2,gs_break3,gs_break4]
    
    #Write each color component and grayscale break into the preset file
    for j in color_components:
        presetFile.write(str(j)+"\n")
    for j in gs_breaks:
        presetFile.write(str(j)+"\n")
    presetFile.close()
    
    #Save under a custom filename
    custom_filename = raw_input("Enter a name to save your custom image under, including the extension, and then press 'enter': ")
    cv2.imwrite(custom_filename,custom_img)