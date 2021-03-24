# -*- coding: utf-8 -*-
"""
Tyler Hu 
COSC 1306

1. Program outputs the number of right triangles with integer length sides for a given integer perimeter. By repeating this calculation, 
   the program determines the perimeter that provides the maximum number of different integer-sided right triangles with the same 
   perimeter.
   EXAMPLE: For a right triangle with integer sides (a,b,c), the perimeter of the triangle is the sum of the sides: p=a+b+c. Given a 
   specific perimeter, for example a perimeter of 12, there is only one possible triangle with integer sides – the classic 
   (3, 4, 5) triangle. For a perimeter of 120, there are three possible triangles: (20, 48, 52), (24, 45, 51), and (30, 40, 50). 
   This is the maximum number of triangles for any perimeter value below 200.
2. Program determines the perimeter, less than 2018, with the most possible integer-sided right triangles and outputs this perimeter.
3. Program keeps track of the possible triangles and output the triangles associated with the maximal perimeter in sorted order.
4. Program calculates and outputs run-time til completion.
"""

import time

# calculates the sides for any right triangle per perimeter
def get_right_tri_sides(perimeter):
    # init list to store triangle side values
    result = [] 
    # right triangles cannot have odd perimeter
    if perimeter % 2 != 0: 
        return
    else: 
        # loops for each 'b' side value starting at 1
        for b in range(1, perimeter // 2): 
            # rewrites 'a' side pythagoras equation to get rid of c
            a = perimeter / 2 * ((perimeter - 2 * b) / (perimeter - b)) 
            if a.is_integer(): 
                # converts 'a' side into integer for tuple
                a = int(a)
                # creates sorted tuple of side a, b, c 
                sides = tuple(sorted((a, b, perimeter-a-b)))
                # checks to avoid duplicates 
                if sides not in result: 
                    result.append(sides)
        return result

# calculates the number of right triangles per perimeter
def get_right_tri_counter(perimeter):
    # init list to store triangle side values
    result = [] 
    # right triangles cannot have odd perimeter
    if perimeter % 2 != 0: 
        return 0
    else: 
        # init value for number of right triangles
        counter = 0
        # loops for each 'b' side value starting at 1
        for b in range(1, perimeter // 2): 
            # rewrites 'a' side pythagoras equation to get rid of c
            a = perimeter / 2 * ((perimeter - 2 * b) / (perimeter - b)) 
            if a.is_integer(): 
                # converts 'a' side into integer for tuple
                a = int(a)
                # creates sorted tuple  
                sides = tuple(sorted((a, b, perimeter-a-b)))
                # check to avoid duplicates 
                if sides not in result: 
                    counter += 1
                    # stores the triangle into result  
                    result.append(sides)
        return counter

# creates dictionary of perimeters as keys and sides as values     
def build_data(limit):
    data = {}
    # loops through every perimeter starting at the smallest right triangle (3-4-5)
    for perimeter in range(limit//2, limit):
        data[perimeter] = get_right_tri_sides(perimeter)
    return data

# finds the perimeter with the maximum number of triangles
def get_most_tri(limit):  
    # max function used to find the highest count of triangles for a perimeter
    return max(range(limit//2, limit), key=get_right_tri_counter)

# main IO
def main():
    # input perimeter limit
    limit = 2018
      
    # outputs
    #print("\n"+"The perimeter of", get_most_tri(limit), "gives a maximum number of", len(build_data(limit)[get_most_tri(limit)]), "triangles.")
    print("\n"+"The perimeter of {} gives a maximum number of {} triangles.".format(get_most_tri(limit), len(build_data(limit)[get_most_tri(limit)])))
    print("\n"+"The triangles are:")
    for i in range(0, len(build_data(limit)[get_most_tri(limit)])):
        # dictionary call is formatted with dictionary[key][tuple value from index 0 - max number of triangles]
        print("\n", build_data(limit)[get_most_tri(limit)][i])
        
    # debug
    #print(build_data(limit)) 
    #print(get_right_tri(limit)) 
    #print(get_most_tri(limit)) 

start = time.time()
# calls main function    
main()

end = time.time()

print("\n"+"Execute time: {} seconds.".format(end-start))
