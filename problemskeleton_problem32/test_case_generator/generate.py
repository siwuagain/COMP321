import sys
import os
import random
from solver import solve_for_output

def generate_random_cases(num_files=20):
    # PUBLIC #
    hardcoded = {
      "greedy.in": ["3", "1 10", "10 5", "11 0"],
      "inorder.in": ["3", "1 10", "3 3", "5 0"],
      "mixed.in": ["4", "1 10", "4 6", "25 5", "26 0"]
    }
    
    for filename, lines in hardcoded.items():
      input_f_path = os.path.join("./problemskeleton_problem32/data/sample/", filename)
      
      with open(input_f_path, "w") as f:
        f.write("\n".join(lines) + "\n")
      
      with open(input_f_path, "r") as input_file:
        output_f_name = filename.replace(".in", ".ans")
        output_f_path = os.path.join("./problemskeleton_problem32/data/sample/", output_f_name)
        
        input_lines = input_file.readlines()
        res = solve_for_output(input_lines)
        
        with open(output_f_path, "w") as out:
          out.write(f"{res}\n")
    # PUBLIC #

    # SECRET HARDCODED #
    n_large = 6000
    
    greedy_lines = [str(n_large)]
    steps = 1
    complexity = n_large * 100
    for i in range(n_large):
      if i == n_large - 1:
        complexity = 0
      else:
        complexity = max(0, complexity - random.randint(10, 20))
      greedy_lines.append(f"{steps} {complexity}")
      steps += random.randint(1, 3)
    
    greedy_path = os.path.join("./problemskeleton_problem32/data/secret/", "secret_greedy_large.in")
    with open(greedy_path, "w") as f:
      f.write("\n".join(greedy_lines) + "\n")
    
    with open(greedy_path, "r") as input_file:
      greedy_output_path = os.path.join("./problemskeleton_problem32/data/secret/", "secret_greedy_large.ans")
      input_lines = input_file.readlines()
      res = solve_for_output(input_lines)
      with open(greedy_output_path, "w") as out:
        out.write(f"{res}\n")
    
  
    inorder_lines = [str(n_large)]
    steps = 1
    complexity = n_large
    for i in range(n_large):
      if i == n_large - 1:
        complexity = 0
      else:
        complexity = max(0, n_large - i - 1)
      inorder_lines.append(f"{steps} {complexity}")
      steps += 2
    
    inorder_path = os.path.join("./problemskeleton_problem32/data/secret/", "secret_inorder_large.in")
    with open(inorder_path, "w") as f:
      f.write("\n".join(inorder_lines) + "\n")
    
    with open(inorder_path, "r") as input_file:
      inorder_output_path = os.path.join("./problemskeleton_problem32/data/secret/", "secret_inorder_large.ans")
      input_lines = input_file.readlines()
      res = solve_for_output(input_lines)
      with open(inorder_output_path, "w") as out:
        out.write(f"{res}\n")
    
    mixed_lines = [str(n_large)]
    steps = 1
    complexity = n_large * 2  
    
    for i in range(n_large):
      if i == n_large - 1:
        complexity = 0
      else:
        if i % 3 == 0:
          decrease = random.randint(5, 15)
        elif i % 3 == 1:
          decrease = random.randint(2, 5)
        else:
          decrease = random.randint(1, 3)
        
        min_future_decreases = (n_large - i - 1)
        complexity = max(min_future_decreases, complexity - decrease)
      
      mixed_lines.append(f"{steps} {complexity}")
      steps += random.randint(1, 5)
    
    mixed_path = os.path.join("./problemskeleton_problem32/data/secret/", "secret_mixed_large.in")
    with open(mixed_path, "w") as f:
      f.write("\n".join(mixed_lines) + "\n")
    
    with open(mixed_path, "r") as input_file:
      mixed_output_path = os.path.join("./problemskeleton_problem32/data/secret/", "secret_mixed_large.ans")
      input_lines = input_file.readlines()
      res = solve_for_output(input_lines)
      with open(mixed_output_path, "w") as out:
        out.write(f"{res}\n")
    # SECRET HARDCODED END #

    # RANDOM #
    for i in range(1, num_files + 1):
      input_f_name = f"secret_{i}.in"
      input_f_path = os.path.join("./problemskeleton_problem32/data/secret/", input_f_name)
      
      with open(input_f_path, "w") as f:

        if i == num_files:
          #at least one secret case should test for TLE
          n = 6000
        else:
          # 1 <= n <= 10000
          n = random.randint(1, 1000)
       
        f.write(f"{n}\n")

        lower_complexity_bound = n 
        upper_steps_bound = 50000 - n - 2

        steps = None
        complexity = 50000

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
        output_f_path = os.path.join("./problemskeleton_problem32/data/secret/", output_f_name)        

        lines = input.readlines()
        res = solve_for_output(lines)

        with open(output_f_path, "w") as out:
          out.write(f"{res}\n")

generate_random_cases()
