import numpy as np

class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        #extracts value from array
        tempArr1 = np.array([pt1[2]])
        fpt1 = tempArr1[0]
        tempArr2 = np.array([pt2[2]])
        fpt2 = tempArr2[0]
        
        #calculates R value
        linearValue = ((((pt2[1]-unknown[1])/(pt2[1]-pt1[1]))*fpt1)+(((unknown[1]-pt1[1])/(pt2[1]-pt1[1]))*fpt2))
        
        return linearValue

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        #gets R values from linear interpolation function
        r1Value = self.linear_interpolation(pt1, pt3, unknown)
        r2Value = self.linear_interpolation(pt2, pt4, unknown)
        
        #calculates P value
        bilinearValue = (((pt2[0]-unknown[0])/(pt2[0]-pt1[0]))*r1Value)+(((unknown[0]-pt1[0])/(pt2[0]-pt1[0]))*r2Value)
    
        return bilinearValue

