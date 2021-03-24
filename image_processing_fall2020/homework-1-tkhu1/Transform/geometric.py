import math
import numpy as np
from .interpolation import interpolation

class Geometric:
    def __init__(self):
        pass

    def forward_rotate(self, image, theta):
        imgShape = image.shape
    
        ###the following code is inspired by Professor Mantini's dip_hw1_rotate.py
        #forward rotation matrix
        transformMatrix = np.array([[math.cos(theta), -math.sin(theta)],
                                    [math.sin(theta), math.cos(theta)]])
        
        #dictionary of the four input corners
        imgCorners = {"tl": np.array([0, 0]),
                   "tr": np.array([0, imgShape[1]]),
                   "bl": np.array([imgShape[0], 0]),
                   "br": np.array([imgShape[0], imgShape[1]])}
        
        #dictionary of the four transformed corners
        transformedCorners = dict()
        
        min_x, min_y = np.inf, np.inf
        max_x, max_y = np.NINF, np.NINF #negative infinity
            
        for k in imgCorners:
            transformedCorners[k] = np.sum(transformMatrix * imgCorners[k], axis=1)
    
            if transformedCorners[k][0] < min_x:
                min_x = transformedCorners[k][0]
    
            if transformedCorners[k][1] < min_y:
                min_y = transformedCorners[k][1]
        
            if transformedCorners[k][0] > max_x:
                max_x = transformedCorners[k][0]
                
            if transformedCorners[k][1] > max_y:
                max_y = transformedCorners[k][1]
        
        #finds rotated image size
        numRotRows = int(math.ceil(max_x - min_x))
        numRotCols = int(math.ceil(max_y - min_y))
        
        #creates new base image
        resultImage = np.zeros((numRotRows, numRotCols, 3), np.uint8) #creates result
        resultImageShape = resultImage.shape
        
        #transforms pixels from old image to new rotated image
        for row in range (imgShape[0]):
            for col in range (imgShape[1]):
                #calculates rotated pixel coord
                coords = np.array([row, col])
                rotatedCoords = np.sum(transformMatrix * coords, axis=1)
                
                #adjusts coord values for correct input into array
                finalRowCoord = int(round(rotatedCoords[0] - min_x))
                finalColCoord = int(round(rotatedCoords[1] - min_y))
                
                #copies pixel value from input image to result
                if (finalRowCoord >= 0 and finalRowCoord < resultImageShape[0] and finalColCoord >= 0 and finalColCoord < resultImageShape[1]):
                    resultImage[finalRowCoord, finalColCoord] = image[row, col]
                
        return resultImage

    def reverse_rotation(self, rotated_image, theta, origin, original_shape):
        ###the following code is inspired by Professor Mantini's dip_hw1_rotate.py
        #inverse rotation matrix
        transformMatrix2 = np.array([[math.cos(theta), math.sin(theta)],
                                    [-math.sin(theta), math.cos(theta)]]) 
        
        #creates new base image
        resultImage = np.zeros((original_shape[0], original_shape[1], 3), np.uint8) #creates result
        
        #transforms pixels from old image to new rotated image
        for row in range (rotated_image.shape[0]):
            for col in range (rotated_image.shape[1]):
                #gets pixel coord wrt origin
                WRT_Og_RowCoord = row - origin[0]
                WRT_Og_ColCoord = col - origin[1]
                
                #calculates rotated pixel coord
                rotatedCoords = np.array([WRT_Og_RowCoord, WRT_Og_ColCoord])
                finalCoords = np.sum(transformMatrix2 * rotatedCoords, axis=1)
                
                #adjusts coord values for correct input into array
                finalRowCoord = int(round(finalCoords[0]))
                finalColCoord = int(round(finalCoords[1]))
                
                #copies pixel value from input image to result
                if ((finalCoords[0] >= 0 and finalCoords[0] <= original_shape[0]-1) and 
                    (finalCoords[1] >= 0 and finalCoords[1] <= original_shape[1]-1)):
                    resultImage[finalRowCoord, finalColCoord] = rotated_image[row, col]
                
        return resultImage

    def rotate(self, image, theta, interpolation_type):
        ##############################START PART 1#################################
        
        imgShape = image.shape
    
        ###the following code is inspired by Professor Mantini's dip_hw1_rotate.py
        #forward rotation matrix
        transformMatrix = np.array([[math.cos(theta), -math.sin(theta)],
                                    [math.sin(theta), math.cos(theta)]])
        
        #dictionary of the four input corners
        imgCorners = {"tl": np.array([0, 0]),
                   "tr": np.array([0, imgShape[1]]),
                   "bl": np.array([imgShape[0], 0]),
                   "br": np.array([imgShape[0], imgShape[1]])}
        
        #dictionary of the four transformed corners
        transformedCorners = dict()
        
        min_x, min_y = np.inf, np.inf
        max_x, max_y = np.NINF, np.NINF #negative infinity
            
        for k in imgCorners:
            transformedCorners[k] = np.sum(transformMatrix * imgCorners[k], axis=1)
    
            if transformedCorners[k][0] < min_x:
                min_x = transformedCorners[k][0]
    
            if transformedCorners[k][1] < min_y:
                min_y = transformedCorners[k][1]
        
            if transformedCorners[k][0] > max_x:
                max_x = transformedCorners[k][0]
                
            if transformedCorners[k][1] > max_y:
                max_y = transformedCorners[k][1]
        
        #finds rotated image size
        numRotRows = int(math.ceil(max_x - min_x))
        numRotCols = int(math.ceil(max_y - min_y))
        
        #creates new base image
        resultImage = np.zeros((numRotRows, numRotCols, 3), np.uint8) #creates result
        
        ###############################END PART 1##################################
                
        ##############################START PART 2#################################
    
        origin = np.array([-min_x, -min_y])
        
        #inverse rotation matrix
        transformMatrix2 = np.array([[math.cos(theta), math.sin(theta)],
                                    [-math.sin(theta), math.cos(theta)]])
        
        #transforms pixels from old image to new rotated image
        for row2 in range (resultImage.shape[0]):
            for col2 in range (resultImage.shape[1]):
                #gets pixel coord wrt origin
                WRT_Og_RowCoord = row2 - origin[0]
                WRT_Og_ColCoord = col2 - origin[1]
                
                #calculates rotated pixel coord
                rotatedCoords2 = np.array([WRT_Og_RowCoord, WRT_Og_ColCoord])
                finalCoords2 = np.sum(transformMatrix2 * rotatedCoords2, axis=1)
                #######################END PART 2##################################
        
                ######################START PART 3#################################
                
                if interpolation_type == "nearest_neighbor":
                    #rounds nearest neighbors
                    finalCoordsNN = np.array([finalCoords2[0], finalCoords2[1]])
                    #adjusts coord values for correct input into array
                    finalRowCoord = int(round(finalCoordsNN[0]))
                    finalColCoord = int(round(finalCoordsNN[1]))
                    
                    #copies pixel value from input image to result
                    if ((finalCoordsNN[0] >= 0 and finalCoordsNN[0] <= imgShape[0]-1) and 
                       (finalCoordsNN[1] >= 0 and finalCoordsNN[1] <= imgShape[1]-1)):
                        resultImage[row2, col2] = image[finalRowCoord, finalColCoord]
                    
                elif interpolation_type == "bilinear":
                    #creates interpolation obj
                    interpolator = interpolation()
                    #checks bounds
                    if ((finalCoords2[0] >= 0 and finalCoords2[0] <= imgShape[0]-1) and 
                       (finalCoords2[1] >= 0 and finalCoords2[1] <= imgShape[1]-1)):
                        #gets four nearest neighbors
                        prev_x = int(math.floor(finalCoords2[0]))
                        next_x = prev_x + 1
                        prev_y = int(math.floor(finalCoords2[1]))
                        next_y = prev_y + 1
                    
                        #collates nearest neighbor data
                        q11 = (next_x, prev_y, image[next_x, prev_y])
                        q12 = (prev_x, prev_y, image[prev_x, prev_y])
                        q21 = (next_x, next_y, image[next_x, next_y])
                        q22 = (prev_x, next_y, image[prev_x, next_y])
                        p = (finalCoords2[0], finalCoords2[1])
                        
                        interpolatedValue = interpolator.bilinear_interpolation(q11, q12, q21, q22, p)
                        resultImage[row2, col2] = interpolatedValue
                        
                #######################END PART 3##################################
            
        return resultImage
