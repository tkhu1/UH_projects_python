# -*- coding: utf-8 -*-
"""
Tyler Hu 
COSC 1306

Drawing shapes according to user input
"""

# prints out list of user choices
def get_menu():
    print("Please select from the following shapes: "+"\n")
    print("1 - Square")
    print("2 - Rectangle")
    print("3 - Right Triangle (left)")
    print("4 - Right Triangle (right)")
    print("5 - Kite (left-right)")
    print("0 - Exit")

# prints out and gets shape choice and size
def get_shape():
    while True:     
        user_selection = int(input("Please enter your selection: "))
        
        #square option
        if user_selection == 1: 
            # init value
            size = 0 
            
            while size <= 0: 
                # gets the size of the shape
                size = int(input("Please enter the size of the square: "))
                if size <= 0:
                    print("\n"+"Invalid size ("+str(size)+"). Please enter a positive value.")
                    
            # return breaks for formatting        
            print() 
            print()
            # calls the corresponding draw function
            draw_square(size) 
            print()
            print()
            # calls the menu function again first
            get_menu() 
        
        # rectangle option
        elif user_selection == 2: 
            # init value
            base = 0 
            height = 0
            
            while base <= 0: 
                # gets the base and height of the rectangle
                base = int(input("Please enter the base of the rectangle: "))
                
                # only continues to height with a valid entry
                if base <= 0: 
                    print("\n"+"Invalid base ("+str(base)+"). Please enter a positive value.")
                    
            while height <= 0:     
                height = int(input("Please enter the height of the rectangle: "))
                
                # only continues to draw function with a valid entry
                if height <= 0: 
                    print("\n"+"Invalid height ("+str(height)+"). Please enter a positive value.")
            
            print()
            print()
            draw_rectangle(base, height) 
            print()
            print()
            get_menu() 

        # right triangle left option
        elif user_selection == 3: 
            # init value
            size = 0 
            
            while size <= 0: 
                # gets the size of the shape
                size = int(input("Please enter the size of the right triangle (left): "))
                if size <= 0:
                    print() #return break for formatting
                    print("Invalid size ("+str(size)+"). Please enter a positive value.")
            
            print() 
            draw_tri_left(size) 
            print()
            print()
            get_menu() 

        # right triangle right option
        elif user_selection == 4: 
            # init value
            size = 0 
            
            while size <= 0: 
                #gets the size of the shape
                size = int(input("Please enter the size of the right triangle (right): "))
                if size <= 0:
                    print("\n"+"Invalid size ("+str(size)+"). Please enter a positive value.")
            
            print() 
            draw_tri_right(size) 
            print()
            print()
            get_menu() 
            
        # kite option
        elif user_selection == 5: 
            # init value
            size = 0 
            
            while size <= 0: 
                # gets the size of the shape
                size = int(input("Please enter the size of the kite: "))
                if size <= 0:
                    print("\n"+"Invalid size ("+str(size)+"). Please enter a positive value.")
            
            print() 
            print()
            draw_kite(size) 
            print()
            print()
            get_menu()
            
        # exit option
        elif user_selection == 0: 
            print("\n"+"Good-bye!")
            break
            
        # returns to main menu
        else: 
            print("\n"+"Invalid selection ("+str(user_selection)+").")    
    
# draw square function    
def draw_square(size):
    row = 0
    while row < size:
        # added a space after the equal symbol to make it more aesthetically squarish
        print("= "*size,)      
        row += 1
        
# draw rectangle function    
def draw_rectangle(base, height):
    row = 0
    while row < height:
        # added a space after the equal symbol to make it more aesthetically correct     
        print("= "*base,) 
        row += 1

# draw triangle left function        
def draw_tri_left(size):          
    row = 0
    while row <= size:
        print("^"*row)    
        row += 1

# draw triangle right function        
def draw_tri_right(size):          
    row = 0
    while row <= size:
        print(" "*(size-row)+"^"*row)    
        row += 1
    
# draw kite function        
def draw_kite(size):          
    row = 0
    while row < size:
        print("%"*row)    
        row += 1
        
    while row > 0:
        print(" "*(size-row)+"%"*row)
        row -= 1
        
# output to obtain input   
get_menu()        
get_shape()
