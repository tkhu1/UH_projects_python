# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries
import numpy as np
import math

class DFT:

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        
        #gets dimensions
        numRows = matrix.shape[0]
        numCols = matrix.shape[1]
        M = numRows
        N = numCols

        #builds output matrix
        resultMatrix = np.zeros((numRows,numCols),dtype=complex)
        
        #forward fourier transform each pixel
        for u in range(numRows):
            for v in range(numCols):
                totalValue = 0 #resets pixel value for next calculation
                for i in range(numRows):
                    for j in range(numCols):
                        periodValue = (u * i / M) + (v * j / N) #calculates the period
                        expValue = -2j * np.pi * periodValue #calculates the exponent portion
                        pixelValue = matrix[i,j] * np.exp(expValue)
                        totalValue += pixelValue #sums calculated values
                
                resultMatrix[u,v] = totalValue
        
        return resultMatrix
                        

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        matrix: a 2d matrix (DFT) usually complex
        takes as input:
        returns a complex matrix representing the inverse fourier transform"""
        
        #gets dimensions
        numRows = matrix.shape[0]
        numCols = matrix.shape[1]
        M = numRows
        N = numCols

        #builds output matrix
        resultMatrix = np.zeros((numRows,numCols),dtype=complex)
        
        #forward fourier transform each pixel
        for i in range(numRows):
            for j in range(numCols):
                totalValue = 0 #resets pixel value for next calculation
                for u in range(numRows):
                    for v in range(numCols):
                        periodValue = (i * u / M) + (j * v / N) #calculates the period
                        expValue = 2j * np.pi * periodValue #calculates the exponent portion
                        pixelValue = matrix[u,v] * np.exp(expValue)
                        totalValue += pixelValue #sums calculated values
                        
                totalValue = totalValue / (M * N) #adjusts the summed value
                resultMatrix[i,j] = totalValue
        
        return resultMatrix


    def discrete_cosine_tranform(self, matrix):
        """Computes the discrete cosine transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing discrete cosine transform"""
        
        #gets dimensions
        numRows = matrix.shape[0]
        numCols = matrix.shape[1]
        M = numRows
        N = numCols

        #builds output matrix
        resultMatrix = np.zeros((numRows,numCols),dtype=complex)
        
        #forward fourier transform each pixel
        for u in range(numRows):
            for v in range(numCols):
                totalValue = 0 #resets pixel value for next calculation
                for i in range(numRows):
                    for j in range(numCols):
                        periodValue = (u * i / M) + (v * j / N) #calculates the period
                        expValue = -2j * np.pi * periodValue #calculates the exponent portion
                        pixelValue = matrix[i,j] * np.exp(expValue)
                        totalValue += pixelValue #sums calculated values
                
                resultMatrix[u,v] = totalValue
        
        return resultMatrix.real #only returns the real part of the complex numbers
        

    def magnitude(self, matrix):
        """Computes the magnitude of the DFT
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the dft"""
        
        #gets dimensions
        numRows = matrix.shape[0]
        numCols = matrix.shape[1]
        
        #builds output matrix
        resultMatrix = np.zeros((numRows,numCols),dtype=float)
        
        #gets the absolute value of the fft (magnitude) without using abs function
        for u in range(numRows):
            for v in range(numCols):
                resultMatrix[u,v] = math.sqrt(math.pow(np.real(matrix[u,v]), 2) + math.pow(np.imag(matrix[u,v]), 2))
        
        return resultMatrix

