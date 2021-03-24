import cv2
import numpy as np

class CellCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        '''using 3 pixel window as defined from lecture'''

        regions = dict()
        
        #region number counter
        k = 1
        #region color array
        regionArr = np.zeros(image.shape)
        
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                #ensures correct bounds for pixel on top left corner
                if i == 0 and j == 0:
                    #if the current pixel is white
                    if image[i, j] == 255:
                        regionArr[i, j] = k
                        k += 1
                
                #ensures correct bounds for pixels on top side of image minus top left corner
                elif i == 0 and j > 0: 
                    #case 1: if only the current pixel is white
                    if image[i, j] == 255 and image[i, j-1] != 255:
                        regionArr[i, j] = k
                        k += 1
                    #case 2: if the current and left pixels are white
                    if image[i, j] == 255 and image[i, j-1] == 255:
                        regionArr[i, j] = regionArr[i, j-1]
                                            
                #ensures correct bounds for pixels on left side of image minus top left corner
                elif i > 0 and j == 0:
                    #case 1: if only the current pixel is white
                    if image[i, j] == 255 and image[i-1, j] != 255:
                        regionArr[i, j] = k
                        k += 1
                    #case 2: if only the current and top pixels are white
                    if image[i, j] == 255 and image[i-1, j] == 255:
                        regionArr[i, j] = regionArr[i-1, j]
                                                    
                #all other pixels    
                else: 
                    #case 1: if only the current pixel is white
                    if image[i, j] == 255 and image[i, j-1] != 255 and image[i-1, j] != 255:
                        regionArr[i, j] = k
                        k += 1
                    #case 2: if only the current and top pixels are white
                    if image[i, j] == 255 and image[i, j-1] != 255 and image[i-1, j] == 255:
                        regionArr[i, j] = regionArr[i-1, j]
                    #case 3: if only the current and left pixels are white
                    if image[i, j] == 255 and image[i, j-1] == 255 and image[i-1, j] != 255:
                        regionArr[i, j] = regionArr[i, j-1]
                    #case 4: if all three pixels are white
                    if image[i, j] == 255 and image[i, j-1] == 255 and image[i-1, j] == 255:
                        regionArr[i, j] = regionArr[i-1, j]
                        #copies region number k to connected pixels
                        if regionArr[i, j-1] != regionArr[i-1, j]:
                            regionArr[i, j-1] = regionArr[i-1, j]
                            
        #print(regionArr)
        
        #populates regions dict
        for row in range(regionArr.shape[0]):
            for col in range(regionArr.shape[1]):
                regionNum = int(regionArr[row, col])
                if regionNum:
                    pixel = [(row, col)]
                    if regionNum in regions:
                        regions[regionNum] = regions[regionNum] + pixel 
                    else: 
                        regions[regionNum] = pixel
    
        return regions

    def compute_statistics(self, region):
        cellFilter = 15
        
        #dict of image stats
        imgStats = dict()
        
        newRegionNum = 1
        
        for regionNum in region:
            area = len(region[regionNum])
            
            #ignores blobs with areas less than 15
            if area > cellFilter:
                #join the area tuples together
                ranges = list(zip(*region[regionNum]))
    
                cent_row = int(sum(ranges[1]) / area)
                cent_col = int(sum(ranges[0]) / area)
                
                #builds a structure to be put into imgStats dict 
                stat = { 'area': area, 'centroid': (cent_row, cent_col) }
                
                #puts a stat into the imgStats dict
                imgStats[newRegionNum] = stat
                
                #prints stats to console
                print("Region:", newRegionNum, "\tArea:", area, "\tCentroid:", stat['centroid'])
                newRegionNum += 1
                
                
        #print ("\nnumber of regions:", len(imgStats))
        
        return imgStats

    def mark_image_regions(self, image, stats):
        #makes a copy of the input image
        resultImage = image.copy()
        
        #font of output text
        outFont = cv2.FONT_HERSHEY_SIMPLEX
        #color of output text
        outColor = (0, 0, 255)
    
        #iterates through each region's 
        for i in stats.values():
            #gets region number
            outRegion = str(int((list(stats.keys())[list(stats.values()).index(i)])))
            #builds text string
            outText = '*' + outRegion + "," + str(i['area'])
            #gets centroid coords
            row, col = i['centroid']
            #adjusts placement of text to appear centered
            row -= 3
            col += 3
            
            #overlays text on input image
            cv2.putText(resultImage, outText, (row, col), outFont, 0.4, outColor)

        return resultImage


