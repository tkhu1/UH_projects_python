# -*- coding: utf-8 -*-
"""
Tyler Hu 
COSC 1306

1. Program requests that the user enter a value for the length and width of a room.
2. Program requests the whole number cost of a bottle of special floor sealant.
3. Program computes the area of room, the number of liters of sealant required to cover the floor, and the number of bottles.
4. Program outputs, in a descriptive format, the area, number of liters, number of bottles, and the total cost of the floor sealant.
"""

import math

def main():
    # constants
    float_rounding = 2
    
    # Variables begin with V
    # Vinputs
    Vroom_length = float(input("Enter the length of the room: "))
    Vroom_width = float(input("Enter the width of the room: "))
    Vbottle_cost = float(input("Enter the cost per bottle: "))
    
    # Voutputs
    Vroom_area = Vroom_length*Vroom_width
    Vseal_need = math.ceil(Vroom_area/6) # math.ceiling to round up to whole numbers
    Vbottle_need = math.ceil(Vseal_need/2)
    Vtotal_cost = Vbottle_need*Vbottle_cost
    
    # frontend output
    print()

    print("="*39)
    # format function is used to add commas to output and round to two decimal places for more precision for area and total cost
    print("Room area      = "+ '{0:,.{1}f}'.format(Vroom_area, float_rounding), "m2")
    print("Sealant needed = "+ '{0:,d}'.format(Vseal_need), "L")
    print("Bottles needed = "+ '{0:,d}'.format(Vbottle_need,))
    print("Total Cost     = $"+'{0:,.{1}f}'.format(Vtotal_cost, float_rounding))
    print("="*39)

main()
