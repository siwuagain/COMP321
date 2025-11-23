import sys
import os
import random
from solver import solve_for_output

def generate_random_cases(num_files=20):
  
    for i in range(1, num_files + 1):
      input_f_name = f"secret_{i}.in"
      input_f_path = os.path.join("./problemskeleton_Problem32/data/sample/", input_f_name)
      
      with open(input_f_path, "w") as f:

        if i == num_files:
          #at least one secret case should test for TLE
          n = 10** 5
        else:
          # 1 <= n <= 10^5
          n = random.randint(1, 10**5)
       
        f.write(f"{n}\n")

        lower_complexity_bound = n 
        upper_steps_bound = sys.maxsize - n - 2

        steps = None
        complexity = sys.maxsize

        for j in range(n):
          
          if steps is not None:
            #each step is guaranteed to be greater than the previous
            #guarantee that steps will not exceed the maximum int value 
            steps = random.randint(steps + 1, upper_steps_bound)
          else:
            #set first trap's steps to 1
            steps = 1

          
          if j == n - 1:
            #set last trap's complexity to 0
            complexity = 0
          else:
            #each complexity is guaranteed to be lesser than the previous
            #guarantee that the complexity leaves enough valid values for the next complexity
            complexity = random.randint(lower_complexity_bound, complexity - 1)

          lower_complexity_bound -= 1            
          upper_steps_bound += 1

          f.write(f"{steps} {complexity}\n") 

      res = None

      #after writing the input file, plug it into the solver to obtain result for the output file
      with open(input_f_path, "r") as input:
        output_f_name = f"input_{i}.ans"
        output_f_path = os.path.join("./problemskeleton_Problem32/data/sample/", output_f_name)        

        lines = input.readlines()
        res = solve_for_output(lines)

        with open(output_f_path, "w") as out:
          out.write(f"{res}\n")

generate_random_cases()



