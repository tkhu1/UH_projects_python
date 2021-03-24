import numpy as np

class Rle:
    def __init__(self):
        pass

    def encode_image(self,binary_image):
        #stores the run length encoding output
        encoding = []
        #stores the number of occurrences
        count = 1
    
        for row in range(binary_image.shape[0]):
            #encoding.append("row:"+str(row))
            #gets the first pixel value of every row
            firstPixel = binary_image[row, 0]
            #encodes 1 if black, 0 if white
            if firstPixel == 0:
                encoding.append(1)
            else:
                encoding.append(0)
            for col in range(binary_image.shape[1]-1):
                #if blob touches right image border in row
                if binary_image[row, col+1] == binary_image[row, col]:
                    #keeps incrementing until it finds a different value
                    count += 1
                    #appends final blob at the end of the column if necessary
                    if ((col+1) == binary_image.shape[1]-1) and (binary_image[row, col+1] == binary_image[row, col]):
                        #adds to encoding
                        encoding.append(count)
                        #resets counter and updates previous element position
                        count = 1
                else:
                    #adds to encoding
                    encoding.append(count)
                    #resets counter and updates previous element position
                    count = 1
                    #if blob does not touch rightmost pixel in image border in row
                    if ((col+1) == binary_image.shape[1]-1) and (binary_image[row, col+1] != binary_image[row, col]):
                        count = 1
                        #adds to encoding
                        encoding.append(count)
                        #resets counter and updates previous element position
                        count = 1
    
        return encoding

    def decode_image(self, rle_code, height , width):
        #creates base image
        decoded_image = np.zeros((height,width), np.uint8)
        
        #moves through rle code
        iterator = 0
        
        for row in range(height):
            #resets column counter
            col = 0
            #gets first pixel value
            pixelValue = rle_code[iterator]
            if pixelValue == 0:
                writeValue = 255
            else:
                writeValue = 0
            #used while loop here to change the col integer in loop
            while col < width:
                iterator += 1
                numOfOccurrences = 0
                #gets number of occurrences of value
                numOfOccurrences = rle_code[iterator]
                #only changes pixels that are white
                for i in range(numOfOccurrences):
                    decoded_image[row, col] = writeValue
                    col += 1
                    #error checking for bound
                    if col == width:
                        break
                    
                #swaps color for next write
                if writeValue == 0:
                    writeValue = 255
                else:
                    writeValue = 0
            
            #gets next pixel value
            iterator += 1
                
        return decoded_image





        




