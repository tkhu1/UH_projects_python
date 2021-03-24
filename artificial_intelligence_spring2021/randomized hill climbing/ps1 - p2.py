# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:57:02 2021

@author: Tyler Hu
"""

import random
import time
from decimal import Decimal

##############################################################################
# Randomized Hill Climbing (RHC) Search of a Minimization Problem            #
##############################################################################

# helper function to return the f solution of the input point
def functionSolver(candidate):
  Fxy = 0
  x = candidate[0]
  y = candidate[1]
  
  if -2 <= x <= 2 and -2 <= x <= 2: 
    Fxy = (1+(x+y+1)**2 * (19 - 14*x + 3*x**2 - 14*y+ 6*x*y + 3*y**2))*(30 + (2*x-3*y)**2 * (18 - 32*x + 12*x**2 + 4*y - 36*x*y + 27*y**2))
  return Fxy

# helper function to find the neighbor point that returns the local minima
def isMinimum(neighbors, solution, count):
  newSolution = solution
  solutionF = functionSolver(solution)
  
  for neighbor in neighbors:
    neighborF = functionSolver(neighbor)
    if neighborF < solutionF:
      newSolution = neighbor
      count += 1
  return [newSolution, count]

# main heuristic
def randomizedHillClimbing(sp, p, z, seedNum, runCounter):
  # defines the random seed
  random.seed(seedNum)
  # defines the point
  s = sp
  
  # defines the list of neighbor points
  neighbors = []
  neighbors.append(sp)
     
  # gets the neighbors
  for neighbor in range(p):
    # gets neighborhood size bounds
    z_lower = -1 * z
    z_upper = z
    # gets z1 and z2 values
    z1 = sp[0] + random.uniform(z_lower, z_upper)
    z2 = sp[1] + random.uniform(z_lower, z_upper)
    neighbors.append([z1,z2])
    #print('neighbors:', neighbors)
  
  # finds the minimum point  
  s, runCounter = isMinimum(neighbors, s, runCounter)
  
  # exit condition for recursive heuristic
  if s == sp:
    s_vector = s
    s_fValue = functionSolver(s)
    # returns a solution's values
    return [s_vector, s_fValue, runCounter]
  # keeps recursing to find global minima
  else:
    return randomizedHillClimbing(s, p, z, seedNum, runCounter)


##############################################################################
# Main                                                                       #
##############################################################################

# defines the starting points of the RHC runs
sp_list = [(0.4,-0.5),(-0.5,0.3),(1,-2),(0,0)]
# defines the number of neighbors of the current solution that will be generated
p = 75
# defines the neighborhood size
z = 0.05
# defines the seed
seed_tuple = (1, 11)
# defines the total number of solutions
runCounter = 0

timeStart = time.perf_counter()

# performs the RHC search
for sp in sp_list: 
  for seedNum in seed_tuple:
    print('\n===== SP:', sp, ' || seed:', seedNum)
    #calls main heuristic function
    solution = randomizedHillClimbing(sp, p, z, seedNum, runCounter)
    solution_vector = solution[0]

    # outputs solutions rounded to 5 decimal places
    rounded_x = round(Decimal(solution_vector[0]), 5)
    rounded_y = round(Decimal(solution_vector[1]), 5)
    rounded_f = round(Decimal(solution[1]), 5)
    print('best x =', rounded_x)
    print('best y =', rounded_y)
    print('best f(x,y) =', rounded_f)
    print('run counter:', solution[2])
    
timeEnd = time.perf_counter()

# outputs runtime
print(f"\nHeuristic finished in {timeEnd - timeStart:0.4f} seconds")
