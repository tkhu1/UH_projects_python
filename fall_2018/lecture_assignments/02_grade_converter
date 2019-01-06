# -*- coding: utf-8 -*-
"""
Tyler Hu 
COSC 1306

1. Program asks the user for a final average, as a floating point number.
2. Uses that number to determine the corresponding letter grade and print out the letter grade in a short message, using the syllabus 
   for the course as a grading guide.
3. Employs a function to handle the letter grade determination and return the letter grade, but not actually print within the function.
4. BONUS - contains a function that will determine the number of points (float) necessary to earn the next higher grade and prints a 
   message showing this number. As an example, if your score is 87.6, you earn a B+, but you are only 0.4 points away from the cutoff 
   for an A-. If the letter grade is already an A, you should instead print a message letting the user know that they have an A and 
   there is no higher grade.
"""

# Variables begin with V
# Vinputs
Vnum_grade = float(input("Please enter a final average: "))

# sets the definition of each lettter grade and returns the appropriate grade
def get_letter_grade(Vnum_grade):
    if Vnum_grade >= 92:
        return "A"
    elif Vnum_grade >= 88:
        return "A-"
    elif Vnum_grade >= 84:
        return "B+"
    elif Vnum_grade >= 80:
        return "B"
    elif Vnum_grade >= 76:
        return "B-"
    elif Vnum_grade >= 72:
        return "C+"
    elif Vnum_grade >= 68:
        return "C"
    elif Vnum_grade >= 64:
        return "C-"
    elif Vnum_grade >= 60:
        return "D+"
    elif Vnum_grade >= 56:
        return "D-"
    else:
        return "F"
    
# Voutputs    
Vletter_grade = get_letter_grade(Vnum_grade)

# bonus
def get_points_needed(Vnum_grade):
    if Vnum_grade >= 92:
        print("You have already received the maximum grade.")
        
    elif Vnum_grade >= 88:
        # format function used to round grade value
        Vpoints_needed = '{0:.1f}'.format(92-Vnum_grade)
        print("You are", Vpoints_needed, "points away from the cutoff for an A.")
    elif Vnum_grade >= 84:
        Vpoints_needed = '{0:.1f}'.format(88-Vnum_grade)
        print("You are", Vpoints_needed, "points away from the cutoff for an A-.")
    elif Vnum_grade >= 80:
        Vpoints_needed = '{0:.1f}'.format(84-Vnum_grade)
        print("You are", Vpoints_needed, "points away from the cutoff for a B+.")
    elif Vnum_grade >= 76:
        Vpoints_needed = '{0:.1f}'.format(80-Vnum_grade)
        print("You are", Vpoints_needed, "points away from the cutoff for a B.")
    elif Vnum_grade >= 72:
        Vpoints_needed = '{0:.1f}'.format(76-Vnum_grade)
        print("You are", Vpoints_needed, "points away from the cutoff for a B-.")
    elif Vnum_grade >= 68:
        Vpoints_needed = '{0:.1f}'.format(72-Vnum_grade)
        print("You are", Vpoints_needed, "points away from the cutoff for a C+.")
    elif Vnum_grade >= 64:
        Vpoints_needed = '{0:.1f}'.format(68-Vnum_grade)
        print("You are", Vpoints_needed, "points away from the cutoff for a C.")
    elif Vnum_grade >= 60:
        Vpoints_needed = '{0:.1f}'.format(64-Vnum_grade)
        print("You are", Vpoints_needed, "points away from the cutoff for a C-.")
    elif Vnum_grade >= 56:
        Vpoints_needed = '{0:.1f}'.format(60-Vnum_grade)
        print("You are", Vpoints_needed, "points away from the cutoff for a D+.")        
    elif Vnum_grade < 56:
        Vpoints_needed = '{0:.1f}'.format(56-Vnum_grade)
        print("You are", Vpoints_needed, "points away from the cutoff for a D-.")        
        
# frontend output
print("\n"+"Congratulations, you earned a/an", Vletter_grade + ".")

# print moved into function to account for string of upper letter grade
get_points_needed(Vnum_grade) 
print("\n"+"="*40)
