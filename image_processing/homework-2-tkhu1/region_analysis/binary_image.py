class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""

        hist = [0]*256
        
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                hist[image[row, col]] += 1
        
        '''for i in range(len(hist)):        
            print (hist[i])'''

        return hist

    def find_otsu_threshold(self, hist):
        """analyses a histogram it to find the otsu's threshold assuming that the input hstogram is bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value (otsu's threshold)"""

        #gets total number of pixels in image
        numPixels = sum(hist) 
        
        #gets the probabilities of each intensity level in histogram
        sum1 = 0
        for i in range(256): 
            sum1 += i * hist[i];
    
        #print("sum:", sum1)
        
        #var init
        threshold = 0.0
        sum2 = 0.0
        weightBackground = 0.0
        weightForeground = 0.0
        varianceMax = 0.0
        
        for i in range(256): 
            #calculates the weights of the background
            weightBackground += hist[i]
            #error checking
            if weightBackground == 0: 
                continue
            
            #calculates the weights of the foreground
            weightForeground = numPixels - weightBackground
            #error checking
            if weightForeground == 0:
                break
             
            sum2 += float(i * hist[i]) #temp sum
            
            #calculates the means of the background
            meanBackground = float(sum2 / weightBackground)
            #calculates the means of the foreground
            meanForeground = float((sum1 - sum2) / weightForeground)
            
            temp = float(meanBackground - meanForeground)
             
            '''calculates the between class variance, as it is much simpler than 
               using the within class variance'''
            variance = float(weightBackground * weightForeground * temp * temp)
            
            #checks for new maximum 
            if variance > varianceMax:
               varianceMax = variance;
               threshold = i;
        
        #print("th:", threshold)
               
        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()
        
        #gets the image's histogram
        binImager = BinaryImage()
        hist = binImager.compute_histogram(bin_img)
        #gets the image's otsu threshold
        threshold = binImager.find_otsu_threshold(hist)
        
        #loops every pixel and changes its intensity according to threshold
        for row in range(bin_img.shape[0]):
            for col in range(bin_img.shape[1]):
                if image[row, col] < threshold:
                    bin_img[row, col] = 255
                else:
                    bin_img[row, col] = 0

        return bin_img


