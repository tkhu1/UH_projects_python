# Solving Discrete Constraint Satisfaction Problems 

Wrote a program which finds solution to the following 3 hierarchically organized constraint satisfaction problems, involving 15 variables {A,B,C,…,N,O} which can take integer values in {1,…,50}. 
a. Problem A: Find a solution to the constraint satisfaction problem involving the six variables A, B, C, D, E and F and constraints C1,…,C4:
 - (C1) A = B+C+E+F
 - (C2) D = E+F+21
 - (C3) D**2 = E*E*A + 417
 - (C4) E+F < A
b. Problem B: Find a solution to the constraint satisfaction problem involving ten variables A,…,J which satisfy constrains C1,…,C9:
 - (C5) H*J+E*12 = (G+I)**2
 - (C6) A+D = (F-G)**2-1
 - (C7) 4*J = G**2+39
 - (C8) (I-G)**9 = (F-H)**3
 - (C9) (G-C)**2 = F*C*C+1
c. Problem C: Find a solution to the constraint satisfaction problem involving 15 variables A,…,O which satisfy constrains C1,..,C15:
 - (C10) 2*M = K**2-6
 - (C11) (N-O)**3+7 = (F-I)*N 
 - (C12) N**2 = M**2 + 291
 - (C13) O**2 = G*H*I*B + 133
 - (C14) M+O = K**2-10
 - (C15) L**3+I = (L+B)*K

The program returns the solution and a counter called nva ("number of variable assignments") that counts the number of times an initial integer value is assigned to a variable or the assigned integer to the particular variable is changed.


**1. SUMMARY**

The program  experimented with two different approaches: 
1) Brute Force Search (BFS)
2) Recursive Backtracking (RBT)

Unfortunately due to time constraints, the BFS method was used more extensively and was more successful than the RBT. The RBT method will require future heuristic improvements implemented to make the approach work.

Programming language used was Python.

Workstation specs: AMD Ryzen 2700X CPU, 32gb DDR4 RAM, Radeon 5700XT GPU, 2TB NVME SSD

1. BRUTE FORCE SEARCH
The Brute Force Method mainly used nested ‘for loops’ to generate the different combinations of integers needed to satisfy the constraints. BFS is very inefficient, as seen by the pseudocode below:

def BruteForceSearch(csp, userProblemChoice):  
    #create the dictionary Vars of variable-value pairs
    Vars = {"A": 0, "B": 0 …}
    #nested loops for searching unknown variable values
    for b in range(1, 47):
      for c in range(1, 47):
        for e in range(1, 29):
          …
	    #collects discovered values into an array
            combo = [b, c, e, f, h, i]
            #assigns discovered values to variables
            Vars["B"] = combo[0]
            Vars["C"] = combo[1]
            …
            counterNVA++ for the number of unknown assignments
            #checks relevant constraints
            if all constraints satisfied:
               #do final derived variable assignments
               Vars["A"] = Vars["B"] + Vars["C"] …
               Vars["D"] = Vars["E"] + Vars["F"] + 21
		    …
               counterNVA++ again for the number of known assignments
               return completed dictionary Vars as solution


The algorithm searches for all the different combinations of integers in the domain for each set of variable, then assigns the values to a dictionary of variable-key pairs, compares the combination with the constraints, then outputs the final solution after calculating the nva. As you can see, the more variables that need to have values searched for, the worse the time complexity. However, I was able to leverage some mathematical analysis on the constraints to lower the number of combinations needed to try on. 

This analysis was able to completely eliminate the need to search for values to assign to some of the Variables. This was done by substituting some variables for other variables to completely get rid of certain Variables. For example, I substituted A and D in C3 by rewriting the equation as (E+F+21)**2 = E*E*(B+C+E+F)+417.
I applied this substitution method as much as possible. For Problem A, the A and D Variables were able to be skipped from having to be searched for in the loops as A can be completely solved separately in C1 by finding B, C, E ,F first and D in C2 can be found by finding E and F first. This reduced the number of loops that need to be computed for Problem A from 6 to 4.  

For Problem B, Variables G and J were able to be completely solved on paper via analysis of C7 and C9. From C9, I was able to derive the fact that G must be >= 3, as the minimum value of G in G=√(F*C^2+1)+C is 3 if F and C are 1. I applied this to C7, where I was able to derive multiple inferences, such as: 1) J must be > 9 as a lower value would result in taking the root of a negative number, 2) G must be < 13 because if J = 50, the square root of 4*J-39 would be too high, 3) for every legal value of J, I was able to find its corresponding G value. This resulted in the partial solution where G = 11 and J = 40, thus decreasing the amount of loops that had to be ran from 10 to 6.

For Problem C, the K,M,N, and O variables were able to be completely analyzed as well. First M was found by solving for the possible legal values of M in the square root function in C10 (5, 15, 29, 47), then inputting those values into C12 to make both constraints true. This yielded that M = 47 and N = 50 via the equation N = sqrt(M**2 + 291) in C12. Therefore, K = 10 by rearranging C10 into K=sqrt(2*M+6), and O = 43 by rearranging C14 into O=K**2-10-M. These analyses resulted in only two extra search loops for the whole program, thus bringing down the total number of search loops from 15 down to 7. 

Other analytical procedures were carried out to reduce the search domain required for each of the loops. I was able to narrow the domain of possible legal values for some of the variables by calculating max values. For example, if D = 50 and C2 states that 50 = E + F + 21, then E or F must be <= 29 combined and <=28 separately. As another example, the domain for F can be lowered even further because the only legal values for F were derived to be only 2, 3, 6, 8, 12, 15, 20 (from analysis of the legal values of the square root function in C9 that would generate whole integers).   

**2. RECURSIVE BACKTRACKING**

The Recursive Backtracking (RBT) Method utilized a different search approach than BFS. RBT leverages the power of recursion to simulate a depth first search technique by exhausting all possible combinations down a “tree branch” before backtracking to a higher level and going down the next tree branch if no solution was found. The pseudocode is below:

Applied to this assignment, the algorithm should function like so: after assigning an initial value to A, it would check if all constraints were satisfied. If not, it would recursively call itself, get a value for B then check constraints again. If the algorithm “inferred” that it was on the right track, it would call the next variable and so on. If not, it would backtrack one level and try again. This algorithm seemed like a good experiment for me to tinker with as a generic solution, but unfortunately, I ran out of time to fully implement this approach, as my current RBT generated unreliable results and unfeasible runtimes. 

**3. RESULTS AND CONCLUSION**

As you can see, the Brute Force Approach was able to derive the solutions with the help of constraint analysis. However, the Recursive Backtracking approach was only able to work with the C1, C2, and C4 constraints as any more added constraints and complexity would stall the program for an unfeasible amount of time. Though brute forcing the Problems worked, the algorithm was highly tailored for specifically that set of constraints. If a new set of constraints were introduced, it would have to be painstakingly re-analyzed by hand again. Therefore, a proper implementation of a generic heuristic algorithm would be much preferred.

Given more time, I would have tried to better implement the recursive backtracking, and implement more heuristic methods into the algorithm, such as Minimum Remaining Values (MRV) to fail early instead of later to remove dead branches from the search tree. I would have also tried to implement a value selection heuristic such as Least Constraining Value (LCV) or Forward Looking to narrow down the search tree even further.

