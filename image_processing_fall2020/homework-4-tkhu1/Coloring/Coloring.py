import numpy as np
import cv2
import math
import random

class Coloring:

    def intensitySlicer(self, maxValue, slices):
        intensityValue = float(maxValue)
        #returns a list of values as slice dividers
        return [i*intensityValue/slices for i in range(1,slices+1)]


    def intensity_slicing(self, image, n_slices):
        #Convert greyscale image to color image using color slicing technique.
        #takes as input:
        #image: the grayscale input image
        #n_slices: number of slices
  
        #Steps:
        # 1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        slicedDividers = Coloring.intensitySlicer(self, 255, n_slices+1)
        #print('dividers:', slicedDividers)
        
        # 2. Randomly assign a color to each interval
        colorsForEachInterval = []
        for i in range(n_slices+1):
            thisRGB = random.sample(range(0, 255), 3)
            colorsForEachInterval.append(thisRGB) 
            
        #print('colors:', colorsForEachInterval)
            
        # 3. Create and output color image
        x,y = image.shape
        
        coloredImage = np.zeros((x,y,3), np.uint8)
        
        # 4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to
        for i in range(x):
            for j in range(y):
                #assigns new RGB values according to the grayscale value
                for k in range(n_slices+1):
                    pixelValue = image[i,j]
                    firstDivider = slicedDividers[0]
                    '''keeps black intensity value as black (commented out)
                    if 0 <= pixelValue <= 10:
                        coloredImage[i,j,1] = 0    #red channel
                        coloredImage[i,j,1] = 0    #green channel
                        coloredImage[i,j,2] = 0    #blue channel'''
                    #first slice    
                    if pixelValue <= firstDivider:
                        #print("slice no.", k, "is coloring pixel:", i, j, "with value", pixelValue, "range is 0 to", firstDivider)
                        coloredImage[i,j,0] = colorsForEachInterval[0][0]    #red channel
                        coloredImage[i,j,1] = colorsForEachInterval[0][1]    #green channel
                        coloredImage[i,j,2] = colorsForEachInterval[0][2]    #blue channel
                        break
                    #other slices
                    elif slicedDividers[k] <= pixelValue <= slicedDividers[k+1]:
                        if k == 0:
                            coloredImage[i,j,0] = colorsForEachInterval[1][0]    #red channel
                            coloredImage[i,j,1] = colorsForEachInterval[1][1]    #green channel
                            coloredImage[i,j,2] = colorsForEachInterval[1][2]    #blue channel
                        else:
                            coloredImage[i,j,0] = colorsForEachInterval[k][0]    #red channel
                            coloredImage[i,j,1] = colorsForEachInterval[k][1]    #green channel
                            coloredImage[i,j,2] = colorsForEachInterval[k][2]    #blue channel
                        break
                        
        #returns colored image
        return coloredImage

    def color_transformation(self,image, n_slices, theta):
        #Convert greyscale image to color image using color transformation technique.
        #takes as input:
        #image:  grayscale input image
        #colors: color array containing RGB values
        
        #Steps:
        # 1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        slicedDividers = Coloring.intensitySlicer(self, 255, n_slices+1)
        #print('dividers:', slicedDividers)
        
        # 2. create red values for each slice using 255*sin(slice + theta[0])
        #    similarly create green and blue using 255*sin(slice + theta[1]), 255*sin(slice + theta[2])
        colorsForEachInterval = []
        
        if n_slices > 0:
            #handles first slice 
            center = slicedDividers[0] / 2
            thisR = int(255*math.sin(center + theta[0]))
            if thisR < 0:  #bound correcting
                thisR = 0;
            thisG = int(255*math.sin(center + theta[1]))
            if thisG < 0:
                thisG = 0;
            thisB = int(255*math.sin(center + theta[2]))
            if thisB < 0:
                thisB = 0;
            thisRGB = [thisR, thisG, thisB]
            colorsForEachInterval.append(thisRGB) 
            #print('center:', center, "between 0 and", slicedDividers[0])
        
        #handles other slices
        if n_slices > 1:
            for i in range(n_slices+1):
                if (i+1) == n_slices:
                    break
                else:
                    center = 0
                    center = slicedDividers[i] + ((slicedDividers[i+1] - slicedDividers[i]) / 2)
                    thisR = int(255*math.sin(center + theta[0]))
                    if thisR < 0:
                        thisR = 0;
                    thisG = int(255*math.sin(center + theta[1]))
                    if thisG < 0:
                        thisG = 0;
                    thisB = int(255*math.sin(center + theta[2]))
                    if thisB < 0:
                        thisB = 0;
                    thisRGB = [thisR, thisG, thisB]
                    colorsForEachInterval.append(thisRGB) 
                    #print('center:', center, "between", slicedDividers[i], "and", slicedDividers[i+1])
        
        print('colors:', colorsForEachInterval)
            
        # 3. Create and output color image
        x,y = image.shape
        
        coloredImage = np.zeros((x,y,3), np.uint8)
        
        # 4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to
        for i in range(x):
            for j in range(y):
                #assigns new RGB values according to the grayscale value
                for k in range(n_slices+1):
                    pixelValue = image[i,j]
                    firstDivider = slicedDividers[0]
                    '''keeps black intensity value as black (commented out)
                    if 0 <= pixelValue <= 10:
                        coloredImage[i,j,1] = 0    #red channel
                        coloredImage[i,j,1] = 0    #green channel
                        coloredImage[i,j,2] = 0    #blue channel'''
                    #first slice    
                    if pixelValue <= firstDivider:
                        #print("slice no.", k, "is coloring pixel:", i, j, "with value", pixelValue, "range is 0 to", firstDivider)
                        coloredImage[i,j,0] = colorsForEachInterval[0][0]    #red channel
                        coloredImage[i,j,1] = colorsForEachInterval[0][1]    #green channel
                        coloredImage[i,j,2] = colorsForEachInterval[0][2]    #blue channel
                        break
                    #other slices
                    elif slicedDividers[k] <= pixelValue <= slicedDividers[k+1]:
                        if k == 0:
                            coloredImage[i,j,0] = colorsForEachInterval[1][0]    #red channel
                            coloredImage[i,j,1] = colorsForEachInterval[1][1]    #green channel
                            coloredImage[i,j,2] = colorsForEachInterval[1][2]    #blue channel
                        else:
                            coloredImage[i,j,0] = colorsForEachInterval[k][0]    #red channel
                            coloredImage[i,j,1] = colorsForEachInterval[k][1]    #green channel
                            coloredImage[i,j,2] = colorsForEachInterval[k][2]    #blue channel
                        break
        
        #returns colored image
        return coloredImage



        

