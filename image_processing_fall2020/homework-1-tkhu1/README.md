# Digital Image Processing 
Assignment #1

Due: Thu 10/01/20 11:59 PM

1. (10 pts.) Forward Rotation: Write code to perform forward rotation on an image.
    - Starter code available in directory Tranform/
    - Transform/geometric.py: Edit the function forward_rotate to implement this part.
    
2. (10 pts.) Reverse Rotation: Write code to perform reverse rotation on the input image.
    - Starter code available in directory Tranform/
    - Transform/geometric.py: Edit the function reverse_rotation to implement this part.
    
2. (20 pts.) Rotation with interpolation: Write code to rotate an the input image, using nearest neighbor and bilinear interpolation.
    - Starter code available in directory Tranform/
    - Transform/geometric.py: Edit the function rotate to implement this part.
    - Transform/interpolation.py: Write code for linear and bilinear interpolation in there respective function definitions, you are welcome to write new functions and call them from these functions


  - The assignment can be run using dip_hw1_rotate.py (there is no need to edit this file)
  - Usage: ./dip_hw1_rotate.py -i image-name -t theta -m method                   
       - image-name: name of the image
       - theta: angle in radians to rotate the image (eg. 0.5)
       - method: "nearest_neightbor" or "bilinear" 
  - Please make sure your code runs when you run the above command from prompt/Terminal
  - Any output images or files must be saved to "output/" folder

----------------------
One images is provided for testing: cameraman.jpg
  
Notes: 

1. Files not to be changed: requirements.txt and Jenkinsfile 

2. the code has to run using one of the following commands

 - Usage: `./dip_hw1_rotate.py -i image-name -t theta -m method`
 
   Example: `./dip_hw1_rotate.py -i cameraman.jpg -t 0.5 -m nearest_neighbor`

 - Usage: `python dip_hw1_rotate.py -i image-name -t theta -m method`
 
   Example: `python dip_hw1_rotate.py -i cameraman.jpg -t 0.5 -m bilinear`
  
3. Any output file or image should be written to output/ folder

4. The code has to run on jenkins CI/CD


Part| Name | Pts
--------------|-------------|----------
1|Forward rotation |- 10 Pts
2|Reverse rotation |- 10 Pts
3|Rotation interpolation |- 20 Pts
-|**Total**     | - **40 Pts**

-----------------------

<sub><sup>
License: Property of Quantitative Imaging Laboratory (QIL), Department of Computer Science, University of Houston. This software is property of the QIL, and should not be distributed, reproduced, or shared online, without the permission of the author This software is intended to be used by students of the digital image processing course offered at University of Houston. The contents are not to be reproduced and shared with anyone with out the permission of the author. The contents are not to be posted on any online public hosting websites without the permission of the author. The software is cloned and is available to the students for the duration of the course. At the end of the semester, the Github organization is reset and hence all the existing repositories are reset/deleted, to accommodate the next batch of students.
</sub></sup>

