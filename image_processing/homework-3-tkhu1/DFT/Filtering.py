# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv
import numpy as np
import math

class Filtering:

    def __init__(self, image, filter_name, cutoff, order = 0):
        """initializes the variables frequency filtering on an input image
        takes as input:
        image: the input image
        filter_name: the name of the mask to use
        cutoff: the cutoff frequency of the filter
        order: the order of the filter (only for butterworth
        returns"""
        self.image = image
        if filter_name == 'ideal_l':
            self.filter = self.get_ideal_low_pass_filter
        elif filter_name == 'ideal_h':
            self.filter = self.get_ideal_high_pass_filter
        elif filter_name == 'butterworth_l':
            self.filter = self.get_butterworth_low_pass_filter
        elif filter_name == 'butterworth_h':
            self.filter = self.get_butterworth_high_pass_filter
        elif filter_name == 'gaussian_l':
            self.filter = self.get_gaussian_low_pass_filter
        elif filter_name == 'gaussian_h':
            self.filter = self.get_gaussian_high_pass_filter

        self.cutoff = cutoff
        self.order = order


    def get_ideal_low_pass_filter(self, shape, cutoff, order = 0):
        """Computes a Ideal low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the ideal filter
        returns a ideal low pass mask"""
        
        #filter was tested with cutoff = 30, order = 0
        
        #gets dimensions
        numRows = shape[0]
        numCols = shape[1]
        
        #builds output mask
        maskILPF = np.zeros((numRows, numCols), np.uint8)
        
        d0 = cutoff
        
        for u in range(numRows):
            for v in range(numCols):
                #calculates the distance between the frequency domain point and the center of the frequency rectangle
                distance = math.sqrt((u-(numRows/2)) ** 2 + (v-(numCols/2)) ** 2)
                if distance <= d0:
                    maskILPF[u,v] = 1
                else:
                    maskILPF[u,v] = 0

        return maskILPF


    def get_ideal_high_pass_filter(self, shape, cutoff, order = 0):
        """Computes a Ideal high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the ideal filter
        returns a ideal high pass mask"""
        
        #Hint: May be one can use the low pass filter function to get a high pass mask
        
        #filter was tested with cutoff = 30, order = 0
        
        maskIHPF = 1.0 - self.get_ideal_low_pass_filter(shape, cutoff)
        
        return maskIHPF


    def get_butterworth_low_pass_filter(self, shape, cutoff, order):
        """Computes a butterworth low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the butterworth filter
        order: the order of the butterworth filter
        returns a butterworth low pass mask"""
        
        #filter was tested with cutoff = 30, order = 2
        
        #gets dimensions
        numRows = shape[0]
        numCols = shape[1]
        
        n = order
        d0 = cutoff
        
        #generates arrays of linearly distributed values
        x = np.linspace(-0.5, 0.5, numCols) * numCols
        y = np.linspace(-0.5, 0.5, numRows) * numRows
        
        #calculates the distance between the frequency domain point and the center of the frequency rectangle
        distance = np.sqrt((x ** 2)[np.newaxis] + (y ** 2)[:, np.newaxis])
        
        maskBLPF = 1 / (1.0 + (distance / d0) ** (2*n))
        
        return maskBLPF
        
    
    def get_butterworth_high_pass_filter(self, shape, cutoff, order):
        """Computes a butterworth high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the butterworth filter
        order: the order of the butterworth filter
        returns a butterworth high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask
        
        #filter was tested with cutoff = 30, order = 2
        
        maskBHPF = 1.0 - self.get_butterworth_low_pass_filter(shape, cutoff, order)
        
        return maskBHPF
        

    def get_gaussian_low_pass_filter(self, shape, cutoff, order = 0):
        """Computes a gaussian low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the gaussian filter (sigma)
        returns a gaussian low pass mask"""
        
        #filter was tested with cutoff = 30, order = 0
        
        #gets dimensions
        numRows = shape[0]
        numCols = shape[1]
        
        d0 = cutoff
        
        #generates arrays of linearly distributed values
        x = np.linspace(-0.5, 0.5, numCols) * numCols
        y = np.linspace(-0.5, 0.5, numRows) * numRows
        
        #calculates the distance between the frequency domain point and the center of the frequency rectangle
        distance = np.sqrt((x ** 2)[np.newaxis] + (y ** 2)[:, np.newaxis])
        
        maskGLPF = np.exp(-(distance ** 2) / (2 * (d0 ** 2)))
        
        return maskGLPF


    def get_gaussian_high_pass_filter(self, shape, cutoff, order = 0):
        """Computes a gaussian high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the gaussian filter (sigma)
        returns a gaussian high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask
        
        #filter was tested with cutoff = 30, order = 0
        
        maskGHPF = 1.0 - self.get_gaussian_low_pass_filter(shape, cutoff)
        
        return maskGHPF


    def post_process_image(self, image):
        """Post process the image to create a full contrast stretch of the image
        takes as input:
        image: the image obtained from the inverse fourier transform
        return an image with full contrast stretch
        -----------------------------------------------------
        1. Full contrast stretch (fsimage)
        2. take negative (255 - fsimage) (Only if needed)
        """
        
        imagePost = np.round(image).astype(np.uint8)
        
        #1. Full contrast stretch
        A = np.min(imagePost)
        B = np.max(imagePost)
        K = 255.0/(B-A)
        
        imagePost = np.round((imagePost - A) * K + 0.5)
        
        return imagePost
    
    
    def filtering(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of DFT, magnitude of filtered DFT        
        ----------------------------------------------------------
        You are allowed to used inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape, cutoff, order)
        4. filter the image frequency based on the mask (Convolution theorem)
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do a full contrast stretch on the magnitude and depending on the algorithm you may also need to
        take negative of the image to be able to view it (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of DFT, magnitude of filtered DFT: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8 
        """
        
        #1. Compute the fft of the image
        imageFFT = np.fft.fft2(self.image)
        #2. shift the fft to center the low frequencies
        imageFFTShifted = np.fft.fftshift(imageFFT)
        #3. get the mask; can be called by self.filter(shape, cutoff, order)
        mask = self.filter(self.image.shape, self.cutoff, self.order)
        #4. filter the image frequency based on the mask (Convolution theorem)
        imageFiltered = imageFFTShifted * mask
        #5. compute the inverse shift
        imageInverseShift = np.fft.ifftshift(imageFiltered)
        #6. compute the inverse fourier transform
        imageIFFT_Filtered = np.fft.ifft2(imageInverseShift)
        #7. compute the magnitude
        magnitudeDFT = np.absolute(imageFFTShifted)      
        #8. You will need to do a full contrast stretch on the magnitude and depending on the algorithm you may also need to
        #   take negative of the image to be able to view it (use post_process_image to write this code)
        imageFilteredFinal = np.uint8(self.post_process_image(np.absolute(imageIFFT_Filtered)))
        #log compression
        magnitudeDFT_Compressed = (np.uint8(np.log(magnitudeDFT))) * 10
        #calculates magnitude of filtered DFT
        magnitudeDFT_Compressed_Filtered = (np.uint8(np.log((1 + np.absolute(imageFiltered))))) * 10

        return [imageFilteredFinal, magnitudeDFT_Compressed, magnitudeDFT_Compressed_Filtered]
        