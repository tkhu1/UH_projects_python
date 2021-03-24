import numpy as np
import cv2


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """
        
        # add your code here
        
        leftImage = image_left
        rightImage = image_right
        divider = column
        
        numRows = len(leftImage)    #finds number of rows in input image
        numCols = len(leftImage[0]) #finds number of columns in input image
        
        resultImage = np.zeros((numRows, numCols), np.uint8) #creates output image
        
        #maps left and right input halves to output image
        resultImage[0:numRows, 0:divider] = leftImage[0:numRows, 0:divider]
        resultImage[0:numRows, divider:numCols] = rightImage[0:numRows, divider:numCols]
    
        # Please do not change the structure
        return resultImage 

    def intensity_scaling(self, output_image, column, alpha, beta):
        """
        Scale your image intensity.

        output_image: the input image
        column: image column at which left section ends
        alpha: left half scaling constant
        beta: right half scaling constant

        return: output_image
        """

        # add your code here
        
        divider = column
        numRows = len(output_image)    #finds number of rows in input image
        numCols = len(output_image[0]) #finds number of columns in input image
    
        #changes values of left and right input halves in output image
        output_image[0:numRows, 0:divider] = output_image[0:numRows, 0:divider]*alpha
        output_image[0:numRows, divider:numCols] = output_image[0:numRows, divider:numCols]*beta

        # Please do not change the structure
        return output_image

    def centralize_pixel(self, output_image, column):
        """
        Centralize your pixels (do not use np.mean)

        output_image: the input image
        column: image column at which left section ends

        return: output_image
        """

        # add your code here
        
        divider = column
        numRows = len(output_image)    #finds number of rows in input image
        numCols = len(output_image[0]) #finds number of columns in input image
        
        leftAvg = 0  #init average values
        rightAvg = 0
        
        #calculates average intensity of left half
        for row in range (numRows):
            for col in range (divider):
                pixelValueLeft = output_image[row, col]
                leftAvg += pixelValueLeft
                
        leftAvg = leftAvg / (numRows*divider)
        
        #calculates average intensity of right half        
        for row in range (numRows):
            for col in range (divider, numCols):
                pixelValueRight = output_image[row, col]
                rightAvg += pixelValueRight
    
        rightAvg = rightAvg / (numRows*(numCols-divider))
        
        #calculates offsets
        leftOffset = 128 - leftAvg
        rightOffset = 128 - rightAvg
        
        #print(leftOffset)
        #print(rightOffset)
    
        #adds offset to left image half        
        for row in range (numRows):
            for col in range (divider):
                pixelValueLeft = output_image[row, col]
                leftAdjusted = leftOffset + pixelValueLeft
                if leftAdjusted > 255:
                    leftAdjusted = 255
                if leftAdjusted < 0:
                    leftAdjusted = 0
                output_image[row, col] = np.uint8(leftAdjusted)
                
        #adds offset to right image half       
        for row in range (numRows):
            for col in range (divider, numCols):
                pixelValueRight = output_image[row, col]
                rightAdjusted = rightOffset + pixelValueRight
                if rightAdjusted > 255:
                    rightAdjusted = 255
                if rightAdjusted < 0:
                    rightAdjusted = 0
                output_image[row, col] = np.uint8(rightAdjusted)

        return output_image
