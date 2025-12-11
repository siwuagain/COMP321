Here are some instructions to help you test the different components of our problem submission
From this directory "problemskeleton_problem32", the solutions are in ./submissions/[type]
under their respective type (accepted, run_time_error, time_limit_exceeded, wrong_answer).

E.g to run optimal solution in python: 
    python3 ./submissions/accepted/accepted.py < ./data/secret/secret_mixed_large.in
    
    You might be interested in running the TLE solution and take notice of the considerable amount of time it takes compared to the optimal one:
    python3 ./submissions/time_limit_exceeded/tle.py < ./data/secret/secret_mixed_large.in

As shown above, the input/output files are in ./data/[sample | secret], the sample contains some hard coded cases that test behaviours on small input, but have equivalents that test it on big inputs (in the ./data/secrets).

The rest of the test cases are randomly generated using the test case generator
which you can run this way:
    
    python3 ./test_case_generator/generate.py 

We created a solver function in the same directory ./test_case_generator/solver.py to help us generate the answer files.

Lastly the input validator is in ./input_format_validators/
You can run it like this on a test case:
    python3 ./input_format_validators/validate.py < data/secret/secret_mixed_large.in