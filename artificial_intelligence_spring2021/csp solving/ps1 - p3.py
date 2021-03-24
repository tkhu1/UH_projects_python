# -*- coding: utf-8 -*-

"""
COSC4368 Fundamentals of A.I. - Spring 2021 
Professor Eick, UH

Problem Set 1 - Problem #3
"""

import sys
import time

##############################################################################
# Brute Force Search (BFS)                                                   #
##############################################################################

#helper function to check constraints
def isConsistent_BFS(assignment, constraints): 
  constraintChecker = []
  #checks each constraint
  for constraint in constraints:
      constraintChecker.append(constraint(assignment))
  if all(constraintChecker):
    return True
  return False

#search algorithm
def bruteForce_Search(csp, choice):
  #sets nva counter
  global counterNVA

  if choice.lower() == 'a':
    #this dict represents the values that need to be discovered
    Vars = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    
    for b in range(1, 48):
      for c in range(1, 48):
        if (b + c <= 48):
          for e in range(1, 29):
            for f in range(1, 29):
              if (e + f <= 29):
                combo = [b, c, e, f]
                #assigns integers to variables
                Vars["B"] = int(combo[0])
                Vars["C"] = int(combo[1])
                Vars["E"] = int(combo[2])
                Vars["F"] = int(combo[3])
                counterNVA += 4
                #checks relevant constraints
                if isConsistent_BFS(Vars, csp[CSP_Constraints]):
                  Vars["A"] = int(Vars["B"] + Vars["C"] + Vars["E"] + Vars["F"])
                  Vars["D"] = int(Vars["E"] + Vars["F"] + 21)
                  counterNVA += 2
                  return Vars

  if choice.lower() == 'b':
    #this dict represents the values that need to be discovered
    Vars = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 11, "H": 0, "I": 0, "J": 40}
    
    for b in range(1, 47):
      for c in range(1, 47):
        if (b + c <= 48):
          for e in range(1, 29):
            for f in [2, 3, 6, 8, 12, 15, 20]:
              if (e + f <= 29):
                for h in range(1, 51):
                  for i in range(1, 51):
                    combo = [b, c, e, f, h, i]
                    #assigns integers to variables
                    Vars["B"] = combo[0]
                    Vars["C"] = combo[1]
                    Vars["E"] = combo[2]
                    Vars["F"] = combo[3]
                    Vars["H"] = combo[4]
                    Vars["I"] = combo[5]
                    counterNVA += 6
                    #checks relevant constraints
                    if isConsistent_BFS(Vars, csp[CSP_Constraints]):
                      Vars["A"] = int(Vars["B"] + Vars["C"] + Vars["E"] + Vars["F"])
                      Vars["D"] = int(Vars["E"] + Vars["F"] + 21)
                      counterNVA += 4 #extra counters for initial assignment of G and J
                      return Vars
                  
  if choice.lower() == 'c':
    #this dict represents the values that need to be discovered
    Vars = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 11, "H": 0, "I": 0, "J": 40, "K": 10, "L": 0, "M": 47, "N": 50, "O": 43}

    for b in range(1, 47):
      for c in range(1, 47):
        if (b + c <= 48):
          for e in range(1, 29):
            for f in [2, 3, 6, 8, 12, 15, 20]:
              if (e + f <= 29):
                for h in range(1, 51):
                  for i in range(1, 51):
                    for l in range(1, 9):
                        combo = [b, c, e, f, h, i, l]
                        #assigns integers to variables
                        Vars["B"] = combo[0]
                        Vars["C"] = combo[1]
                        Vars["E"] = combo[2]
                        Vars["F"] = combo[3]
                        Vars["H"] = combo[4]
                        Vars["I"] = combo[5]
                        Vars["L"] = combo[6]
                        counterNVA += 7
                        #checks relevant constraints
                        if isConsistent_BFS(Vars, csp[CSP_Constraints]):
                          Vars["A"] = int(Vars["B"] + Vars["C"] + Vars["E"] + Vars["F"])
                          Vars["D"] = int(Vars["E"] + Vars["F"] + 21)
                          counterNVA += 8 #extra counters for initial assignment of G, J, K, M, N, O
                          return Vars

#defines each constraint for recursive backtracking. @param 'a' stands for the assignment dict
def C1_BFS(a): 
  #don't need to solve for A 
  A: int = a["A"]
  B: int = a["B"]
  C: int = a["C"]
  E: int = a["E"]
  F: int = a["F"]
  LHS: int = A
  RHS: int = B+C+E+F
  return LHS == RHS

def C2_BFS(a): 
  #don't need to solve for D
  D: int = a["D"]
  E: int = a["E"]
  F: int = a["F"]
  LHS: int = D
  RHS: int = E+F+21
  return LHS == RHS

def C3_BFS(a): 
  #constraint analysis reveals that you can skip assigning for D by substituting (E+F+21) for D
  B: int = a["B"]
  C: int = a["C"]
  E: int = a["E"]
  F: int = a["F"]
  LHS: int = (E+F+21)**2
  RHS: int = E*E*(B+C+E+F)+417
  return LHS == RHS

def C4_BFS(a): 
  #constraint analysis reveals that you can skip assigning for A by substituting (E+F) for A
  B: int = a["B"]
  C: int = a["C"]
  E: int = a["E"]
  F: int = a["F"]
  LHS: int = E+F
  RHS: int = B+C+E+F
  return LHS < RHS

def C5_BFS(a): 
  #constraint analysis reveals that you can skip assigning for G by substituting (4*J - 39)**2 for G
  #further analysis of C7 and C9 reveals that G must equal 11 and J = 40
  if a["A"] is not None and a["J"] is not None:
    E: int = a["E"]
    H: int = a["H"]
    I: int = a["I"]
    LHS: int = H*40 + E*12
    RHS: int = (11+I)**2
    return LHS == RHS
  return False 

def C6_BFS(a): 
  #constraint analysis reveals that you can skip assigning for A by substituting (E+F) for A
  #further analysis of C7 and C9 reveals that G must equal 11
  if a["A"] is not None and a["J"] is not None:
    B: int = a["B"]
    C: int = a["C"]
    E: int = a["E"]
    F: int = a["F"]
    LHS: int = (B+C+E+F) + (E+F+21)
    RHS: int = (F-11)**2 - 1
    return LHS == RHS
  return False 

def C7_BFS(a): 
  #don't need to solve for G or J
  if a["A"] is not None and a["J"] is not None:
    G: int = a["G"]
    J: int = a["J"]
    LHS: int = 4*J
    RHS: int = G**2 + 39
    return LHS == RHS
  return False 

def C8_BFS(a): 
  #analysis of C7 and C9 reveals that G must equal 11
  if a["A"] is not None and a["J"] is not None:
    F: int = a["F"]
    H: int = a["H"]
    I: int = a["I"]
    LHS: int = pow((I-11), 9)
    RHS: int = pow((F-H), 3)
    return LHS == RHS
  return False 

def C9_BFS(a): 
  #analysis of C7 and C9 reveals that G must equal 11
  if a["A"] is not None and a["J"] is not None:
    C: int = a["C"]
    F: int = a["F"]
    LHS: int = (11-C)**2
    RHS: int = F*C*C + 1
    return LHS == RHS
  return False 

def C10_BFS(a): 
  #don't need to solve for K or M
  if a["A"] is not None and a["O"] is not None:
    K: int = a["K"]
    M: int = a["M"]
    LHS: int = 2*M
    RHS: int = K**2 - 6
    return LHS == RHS
  return False 

def C11_BFS(a): 
  #analysis of C10 and C12 reveals that N must equal 50
  #further analysis of C14 reveals that O must equal 43
  if a["A"] is not None and a["O"] is not None:
    F: int = a["F"]
    I: int = a["I"]
    LHS: int = pow((50-43), 3) + 7
    RHS: int = (F-I)*50
    return LHS == RHS
  return False 

def C12_BFS(a): 
  #don't need to solve for K or M
  if a["A"] is not None and a["O"] is not None:
    N: int = a["N"]
    M: int = a["M"]
    LHS: int = N**2
    RHS: int = M**2 + 291
    return LHS == RHS
  return False 

def C13_BFS(a): 
  #analysis of C14 reveals that O must equal 43
  if a["A"] is not None and a["O"] is not None:
    B: int = a["B"]
    G: int = a["G"]
    H: int = a["H"]
    I: int = a["I"]
    LHS: int = 43**2
    RHS: int = G*H*I*B + 133
    return LHS == RHS
  return False 

def C14_BFS(a): 
  #don't need to solve for M or O
  if a["A"] is not None and a["O"] is not None:
    M: int = a["M"]
    O: int = a["O"]
    LHS: int = M+O
    RHS: int = (2*M+6)-10
    return LHS == RHS
  return False 

def C15_BFS(a): 
  #analysis of C10 and C12 reveals that K must equal 50
  if a["A"] is not None and a["O"] is not None:
    B: int = a["B"]
    I: int = a["I"]
    L: int = a["L"]
    LHS: int = pow(L, 3) + I
    RHS: int = (L+B)*10
    return LHS == RHS
  return False 


##############################################################################
# Recursive Backtracking                                                     #
##############################################################################

#initiates first variable assignment
def initAssignmentVar(csp):
  assignment = {}
  for var in csp[CSP_Variables]:
    assignment[var] = None
  return assignment

#checks if the CSP is completely finished (when all variables have been assigned) 
def isComplete(assignment):  
  if None not in (assignment.values()):
    return True
  return False

#selects an unassigned variable for the next step
def getNewVar(variables, assignment):
  for var in variables:
    if assignment[var] is None:
      return var

#domains derived from mathematical analysis of constraints
def getDomain(var, cspDomain):
  if var == "A":
    return list(range(4,51))
  if var == "B" or var == "C":
    return list(range(1,51))
  if var == "D":
    return list(range(23,51))
  if var == "E" or var == "F":
    return list(range(1,29))
  return cspDomain

def isConsistent_RBT(assignment, constraints): 
  #increments nva counter
  global counterNVA
  counterNVA += 1
  constraintChecker = []
  #checks each constraint
  for constraint in constraints:
      constraintChecker.append(constraint(assignment))
  if all(constraintChecker):
    return False
  return True

# search algorithm
def recursiveBacktracking(assignment, csp):
  #exits if solution found
  if isComplete(assignment):
    return assignment
  #gets new variable
  var = getNewVar(csp[CSP_Variables], assignment)
  #gets domain for each variable
  domain = getDomain(var, csp[CSP_Domain])
  #loops through domain values
  for value in domain:
    localAssignment = assignment.copy()
    localAssignment[var] = value
    #print(localAssignment, value)
    #checks if constraints are satisfied
    if isConsistent_RBT(localAssignment, csp[CSP_Constraints]):
      #recursively calls the backtracking search algorithm
      result = recursiveBacktracking(localAssignment, csp)
      #fail checking
      if result != fail:
        return result
    localAssignment[var] = None
  return fail
  
#defines each constraint for recursive backtracking. @param 'a' stands for the assignment dict
def C1_RBT(a): 
  if a["A"] is not None and a["F"] is not None:
    A: int = a["A"]
    B: int = a["B"]
    C: int = a["C"]
    E: int = a["E"]
    F: int = a["F"]
    LHS: int = A
    RHS: int = B+C+E+F
    return LHS == RHS
  return False

def C2_RBT(a): 
  if a["A"] is not None and a["F"] is not None:
    D: int = a["D"]
    E: int = a["E"]
    F: int = a["F"]
    LHS: int = D
    RHS: int = E+F+21
    return LHS == RHS
  return False 

def C3_RBT(a): 
  #constraint analysis reveals that you can skip assigning for D by substituting (E+F+21) for D
  if a["A"] is not None and a["F"] is not None:
    B: int = a["B"]
    C: int = a["C"]
    E: int = a["E"]
    F: int = a["F"]
    LHS: int = (E+F+21)**2
    RHS: int = (E*E*(B+C+E+F))+417
    return LHS == RHS
  return False 

def C4_RBT(a): 
  #constraint analysis reveals that you can skip assigning for A by substituting (E+F) for A
  if a["A"] is not None and a["F"] is not None:
    B: int = a["B"]
    C: int = a["C"]
    E: int = a["E"]
    F: int = a["F"]
    LHS: int = E+F
    RHS: int = (B+C+E+F)
    return LHS < RHS
  return False 

def C5_RBT(a): 
  #constraint analysis reveals that you can skip assigning for G by substituting (4*J - 39)**2 for G
  #further analysis of C7 and C9 reveals that G must equal 11 and J = 40
  if a["A"] is not None and a["J"] is not None:
    E: int = a["E"]
    H: int = a["H"]
    I: int = a["I"]
    LHS: int = H*40 + E*12
    RHS: int = (11+I)**2
    return LHS == RHS
  return False 

def C6_RBT(a): 
  #constraint analysis reveals that you can skip assigning for A by substituting (E+F) for A
  #further analysis of C7 and C9 reveals that G must equal 11
  if a["A"] is not None and a["J"] is not None:
    B: int = a["B"]
    C: int = a["C"]
    E: int = a["E"]
    F: int = a["F"]
    LHS: int = (B+C+E+F) + (E+F+21)
    RHS: int = (F-11)**2 - 1
    return LHS == RHS
  return False 

def C7_RBT(a): 
  #don't need to solve for G or J
  if a["A"] is not None and a["J"] is not None:
    G: int = a["G"]
    J: int = a["J"]
    LHS: int = 4*J
    RHS: int = G**2 + 39
    return LHS == RHS
  return False 

def C8_RBT(a): 
  #analysis of C7 and C9 reveals that G must equal 11
  if a["A"] is not None and a["J"] is not None:
    F: int = a["F"]
    H: int = a["H"]
    I: int = a["I"]
    LHS: int = pow((I-11), 9)
    RHS: int = pow((F-H), 3)
    return LHS == RHS
  return False 

def C9_RBT(a): 
  #analysis of C7 and C9 reveals that G must equal 11
  if a["A"] is not None and a["J"] is not None:
    C: int = a["C"]
    F: int = a["F"]
    LHS: int = (11-C)**2
    RHS: int = F*C*C + 1
    return LHS == RHS
  return False 

def C10_RBT(a): 
  #don't need to solve for K or M
  if a["A"] is not None and a["O"] is not None:
    K: int = a["K"]
    M: int = a["M"]
    LHS: int = 2*M
    RHS: int = K**2 - 6
    return LHS == RHS
  return False 

def C11_RBT(a): 
  #analysis of C10 and C12 reveals that N must equal 50
  #further analysis of C14 reveals that O must equal 43
  if a["A"] is not None and a["O"] is not None:
    F: int = a["F"]
    I: int = a["I"]
    LHS: int = pow((50-43), 3) + 7
    RHS: int = (F-I)*50
    return LHS == RHS
  return False 

def C12_RBT(a): 
  #don't need to solve for K or M
  if a["A"] is not None and a["O"] is not None:
    N: int = a["N"]
    M: int = a["M"]
    LHS: int = N**2
    RHS: int = M**2 + 291
    return LHS == RHS
  return False 

def C13_RBT(a): 
  #analysis of C14 reveals that O must equal 43
  if a["A"] is not None and a["O"] is not None:
    B: int = a["B"]
    G: int = a["G"]
    H: int = a["H"]
    I: int = a["I"]
    LHS: int = 43**2
    RHS: int = G*H*I*B + 133
    return LHS == RHS
  return False 

def C14_RBT(a): 
  #don't need to solve for M or O
  if a["A"] is not None and a["O"] is not None:
    M: int = a["M"]
    O: int = a["O"]
    LHS: int = M+O
    RHS: int = (2*M+6)-10
    return LHS == RHS
  return False 

def C15_RBT(a): 
  #analysis of C10 and C12 reveals that K must equal 50
  if a["A"] is not None and a["O"] is not None:
    B: int = a["B"]
    I: int = a["I"]
    L: int = a["L"]
    LHS: int = pow(L, 3) + I
    RHS: int = (L+B)*10
    return LHS == RHS
  return False 

##############################################################################
# Main                                                                       #
##############################################################################

#global var definitions
CSP_Variables = "variables"
CSP_Domain = "domain"
CSP_Constraints = "constraints"
fail = "fail"
a = []

counterNVA = 0 #global nva counter

#defines the CSPs for each algorithm
CSP_ProblemA_BFS = {CSP_Variables: ["A","B","C","D","E","F"], 
                    CSP_Domain: list(range(1, 51)), 
                    CSP_Constraints: [C3_BFS,C4_BFS]}

CSP_ProblemB_BFS = {CSP_Variables: ["A","B","C","D","E","F","G","H","I","J"], 
                    CSP_Domain: list(range(1, 51)), 
                    CSP_Constraints: [C3_BFS,C4_BFS,C5_BFS,C6_BFS,C8_BFS,C9_BFS]}

CSP_ProblemC_BFS = {CSP_Variables: ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"], 
                    CSP_Domain: list(range(1, 51)), 
                    CSP_Constraints: [C3_BFS,C4_BFS,C5_BFS,C6_BFS,C8_BFS,C9_BFS,C11_BFS,C13_BFS,C15_BFS]}

CSP_ProblemA_RBT = {CSP_Variables: ["A","B","C","D","E","F"], 
                    CSP_Domain: list(range(1, 51)), 
                    CSP_Constraints: [C1_RBT,C2_RBT,C3_RBT,C4_RBT]}

CSP_ProblemB_RBT = {CSP_Variables: ["A","B","C","D","E","F","G","H","I","J"], 
                    CSP_Domain: list(range(1, 51)), 
                    CSP_Constraints: [C1_RBT,C2_RBT,C3_RBT,C4_RBT,C5_RBT,C6_RBT,C7_RBT,C8_RBT,C9_RBT]}

CSP_ProblemC_RBT = {CSP_Variables: ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"], 
                    CSP_Domain: list(range(1, 51)), 
                    CSP_Constraints: [C1_RBT,C2_RBT,C3_RBT,C4_RBT,C5_RBT,C6_RBT,C7_RBT,C8_RBT,C9_RBT,C10_RBT,C11_RBT,C12_RBT,C13_RBT,C14_RBT,C15_RBT]}

#print('max:', max(CSP_ProblemA.get(CSP_Domain)))
#print(str(CSP_ProblemA_RBT))

userChoice = 'input'

#input loop with validation 
while True:
  userChoice = input("Please input which problem set you would like to solve (A,B,C) or type 0 to exit: ")
  if userChoice == '0':
    sys.exit()
  elif userChoice.lower() not in ('a', 'b', 'c'):
    print("Not an appropriate choice, please try again.")
  else:
      break

timeStart = time.perf_counter()

#calls main program loop
if userChoice.lower() == 'a':
  timeStart = time.perf_counter()
  solutionBruteForce = bruteForce_Search(CSP_ProblemA_BFS, userChoice)
  timeEnd = time.perf_counter()
  #outputs brute force search solution
  print ('\nBFS:\nNVA counter:', counterNVA, '\nSolution:', solutionBruteForce)
  #outputs runtime
  print(f"Algorithm finished in {timeEnd - timeStart:0.4f} seconds")
  
  counterNVA = 0
  
  timeStart = time.perf_counter()
  solutionBacktracking = recursiveBacktracking(initAssignmentVar(CSP_ProblemA_RBT), CSP_ProblemA_RBT)
  timeEnd = time.perf_counter()
  #outputs recursive backtracking solution
  print ('\n\nRBT:\nNVA counter:', counterNVA, '\nSolution:', solutionBacktracking)
  #outputs runtime
  print(f"Algorithm finished in {timeEnd - timeStart:0.4f} seconds")
  
elif userChoice.lower() == 'b':
  timeStart = time.perf_counter()
  solutionBruteForce = bruteForce_Search(CSP_ProblemB_BFS, userChoice)
  timeEnd = time.perf_counter()
  #outputs brute force search solution
  print ('\nBFS:\nNVA counter:', counterNVA, '\nSolution:', solutionBruteForce)
  #outputs runtime
  print(f"Algorithm finished in {timeEnd - timeStart:0.4f} seconds")
  '''
  counterNVA = 0
  
  timeStart = time.perf_counter()
  solutionBacktracking = recursiveBacktracking(initAssignmentVar(CSP_ProblemB_RBT), CSP_ProblemB_RBT)
  timeEnd = time.perf_counter()
  #outputs recursive backtracking solution
  print ('\n\nRBT:\nNVA counter:', counterNVA, '\nSolution:', solutionBacktracking)
  #outputs runtime
  print(f"Algorithm finished in {timeEnd - timeStart:0.4f} seconds")'''
  
elif userChoice.lower() == 'c':
  timeStart = time.perf_counter()
  solutionBruteForce = bruteForce_Search(CSP_ProblemC_BFS, userChoice)
  timeEnd = time.perf_counter()
  #outputs brute force search solution
  print ('\nBFS:\nNVA counter:', counterNVA, '\nSolution:', solutionBruteForce)
  #outputs runtime
  print(f"Algorithm finished in {timeEnd - timeStart:0.4f} seconds")
  '''
  counterNVA = 0
  
  timeStart = time.perf_counter()
  solutionBacktracking = recursiveBacktracking(initAssignmentVar(CSP_ProblemC_RBT), CSP_ProblemC_RBT)
  timeEnd = time.perf_counter()
  #outputs recursive backtracking solution
  print ('\n\nRBT:\nNVA counter:', counterNVA, '\nSolution:', solutionBacktracking)
  #outputs runtime
  print(f"Algorithm finished in {timeEnd - timeStart:0.4f} seconds")'''
  
else:
  sys.exit()