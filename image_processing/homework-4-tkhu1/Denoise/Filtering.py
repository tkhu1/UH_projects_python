import numpy as np
import math
import cv2


class Filtering:

    def __init__(self, image, filter_name, filter_size, var = None):
        """initializes the variables of spatial filtering on an input image
        takes as input:
        image: the noisy input image
        filter_name: the name of the filter to use
        filter_size: integer value of the size of the fitler
        global_var: noise variance to be used in the Local noise reduction filter
        S_max: Maximum allowed size of the window that is used in adaptive median filter
        """

        self.image = image
        self.filterName = filter_name

        if filter_name == 'arithmetic_mean':
            self.filter = self.get_arithmetic_mean
        elif filter_name == 'geometric_mean':
            self.filter = self.get_geometric_mean
        if filter_name == 'local_noise':
            self.filter = self.get_local_noise
        elif filter_name == 'median':
            self.filter = self.get_median
        elif filter_name == 'adaptive_median':
            self.filter = self.get_adaptive_median

        self.filter_size = filter_size
        self.global_var = var
        self.S_max = 15
        

    def get_arithmetic_mean(self, roi):
        """Computes the arithmetic mean of the input roi
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the arithmetic mean value of the roi"""
        
        #iterates through roi and returns the arithmetic mean of its elements 
        return math.fsum(i for i in roi) / len(roi)
    

    def get_geometric_mean(self, roi):
        """Computes the geometric mean for the input roi
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the geometric mean value of the roi"""
        
        #init vars
        product = 1
        n = len(roi)
      
        #iterates through roi and returns the geometric mean of its elements 
        for i in range(n): 
            product = product * roi[i] 
       
        result = (float)(math.pow(product, (1 / n))) 
        return (float)(result) 
    

    def get_local_noise(self, roi, pixel):
        """Computes the local noise reduction value
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the local noise reduction value of the roi"""
        
        noiseVar = self.global_var
        n = len(roi)
        
        #gets g(x, y) aka the noisy pixel value
        noisyPixel = (float)(pixel)
        
        localMean = (float)(math.fsum(i for i in roi) / n)
        localVar = (float)((math.fsum(i**2 for i in roi) / n) - localMean**2)
        
        result = (float)(noisyPixel - (noiseVar/localVar)*(noisyPixel-localMean))
        
        #returns the local noise reduction value. Unfortunately, my local noise function cannot handle bipolar noise
        return (float)(result) 
    

    def get_median(self, roi):
        """Computes the median for the input roi
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the median value of the roi"""

        #returns the median of roi
        return np.median(roi)

    
    def StageB(self, window, Zmin, Zmed, Zmax):
        """Stage B for the adaptive median filter
        takes as input:
        window: matrix passed from get_adaptive_median 
        returns the median value of the roi"""
        
        #gets window dimensions
        x,y = window.shape
        
        Zxy = window[x//2, y//2]
        B1 = Zxy - Zmin
        B2 = Zxy - Zmax
    
        if B1 > 0 and B2 < 0 :
            return Zxy
        else:
            return Zmed
        

    def get_adaptive_median(self, img, x, y, size, sMax):
        """Changed the input parameters to make window reshaping easier.
        This function represents Stage A for the adaptive median filter
        takes as input:
        image: image matrix
        x: current x pixel
        y: current y pixel
        size: filter window size
        sMax: maximum allowed size of Sxy
        returns the filtered intensity value of the pixel"""
        
        #reshapes window for every pixel
        baseWindow = size//2
        filterWindow = img[x-baseWindow:x+baseWindow+1, y-baseWindow:y+baseWindow+1]
        
        #gets window intensity values
        Zmin = np.min(filterWindow)
        Zmed = np.median(filterWindow)
        Zmax = np.max(filterWindow)
        
        #Stage A
        A1 = Zmed - Zmin
        A2 = Zmed - Zmax
    
        if A1 > 0 and A2 < 0:
            return Filtering.StageB(self, filterWindow, Zmin, Zmed, Zmax)
        else:
            size += 2 
            if size <= sMax:
                return Filtering.get_adaptive_median(self, img, x, y, size, sMax)
            else:
                return Zmed
            

    def filtering(self):
        """performs filtering on an image containing gaussian or salt & pepper noise
        returns the denoised image
        ----------------------------------------------------------
        Note: Here when we perform filtering we are not doing convolution.
        For every pixel in the image, we select a neighborhood of values defined by the kernal and apply a mathematical
        operation for all the elements with in the kernel. For example, mean, median and etc.

        Steps:
        1. add the necesssary zero padding to the noisy image, that way we have sufficient values to perform the operati
        ons on the pixels at the image corners. The number of rows and columns of zero padding is defined by the kernel size
        2. Iterate through the image and every pixel (i,j) gather the neighbors defined by the kernel into a list (or any data structure)
        3. Pass these values to one of the filters that will compute the necessary mathematical operations (mean, median, etc.)
        4. Save the results at (i,j) in the ouput image.
        5. return the output image

        Note: You can create extra functions as needed. For example if you feel that it is easier to create a new function for
        the adaptive median filter as it has two stages, you are welcome to do that.
        For the adaptive median filter assume that S_max (maximum allowed size of the window) is 15
        """
        
        noisyImage = self.image
        
        #1. add the necesssary zero padding to the noisy image
        if self.filterName == 'adaptive_median':
            padValue = self.S_max//2
            paddedImage = np.zeros((noisyImage.shape[0] + 2*padValue, noisyImage.shape[1] + 2*padValue))
            paddedImage[padValue:-padValue,padValue:-padValue] = noisyImage
        else:
            padValue = self.filter_size//2
            paddedImage = np.zeros((noisyImage.shape[0] + 2*padValue, noisyImage.shape[1] + 2*padValue))
            paddedImage[padValue:-padValue,padValue:-padValue] = noisyImage
        
        #2. Iterate through the image and every pixel (i,j) gather the neighbors defined by the kernel into a list (or any data structure)
        #3. Pass these values to one of the filters that will compute the necessary mathematical operations (mean, median, etc.)
        #4. Save the results at (i,j) in the ouput image.
        #5. return the output image
            
        outputImage = np.zeros(paddedImage.shape)
         
        if self.filterName == 'adaptive_median':    
            for i in range(padValue, noisyImage.shape[0]+padValue+1):
                for j in range(padValue, noisyImage.shape[1]+padValue+1):
                    denoisedValue = Filtering.get_adaptive_median(self, paddedImage, i, j, self.filter_size, self.S_max)
                    outputImage[i,j] = denoisedValue
                    
        elif self.filterName == 'local_noise':    
            for i in range(padValue, noisyImage.shape[0]+padValue+1):
                for j in range(padValue, noisyImage.shape[1]+padValue+1):
                    windowFilter = paddedImage[i-padValue:i+padValue+1, j-padValue:j+padValue+1] #gets window
                    roiFilter = windowFilter.flatten() #flattens 2d image array to 1d array
                    denoisedValue = Filtering.get_local_noise(self, roiFilter, paddedImage[i,j])
                    outputImage[i,j] = denoisedValue

            
        elif self.filterName == 'arithmetic_mean':
            for i in range(padValue, noisyImage.shape[0]+padValue+1):
                for j in range(padValue, noisyImage.shape[1]+padValue+1):
                    windowFilter = paddedImage[i-padValue:i+padValue+1, j-padValue:j+padValue+1]
                    roiFilter = windowFilter.flatten()
                    denoisedValue = Filtering.get_arithmetic_mean(self, roiFilter)
                    outputImage[i,j] = denoisedValue

        elif self.filterName == 'geometric_mean':
            for i in range(padValue, noisyImage.shape[0]+padValue+1):
                for j in range(padValue, noisyImage.shape[1]+padValue+1):
                    windowFilter = paddedImage[i-padValue:i+padValue+1, j-padValue:j+padValue+1]
                    roiFilter = windowFilter.flatten()
                    denoisedValue = Filtering.get_geometric_mean(self, roiFilter)
                    outputImage[i,j] = denoisedValue
        
        elif self.filterName == 'median':
            for i in range(padValue, noisyImage.shape[0]+padValue+1):
                for j in range(padValue, noisyImage.shape[1]+padValue+1):
                    windowFilter = paddedImage[i-padValue:i+padValue+1, j-padValue:j+padValue+1]
                    roiFilter = windowFilter.flatten()
                    denoisedValue = Filtering.get_median(self, roiFilter)
                    outputImage[i,j] = denoisedValue
                
        return outputImage[padValue:-padValue, padValue:-padValue] #crops image to remove padding

