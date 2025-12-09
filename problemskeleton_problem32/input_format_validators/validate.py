#!/usr/bin/env python3

import sys
import re

######
try:
    n_line = sys.stdin.readline()
    print(repr(n_line)) # useful for debugging to see where we have read
    assert re.match('^[1-9][0-9]{0,5}\n$', n_line) # note: no leading zeros

    n = int(n_line)
    assert 1 <= n <= 10**5

    prev_steps = prev_complexity = None
    for i in range(1, n+1):
        case_line = sys.stdin.readline()
        
        print(f"Line {i}: {repr(case_line)}")
        assert re.match('^(0|[1-9][0-9]{0,5}) (0|[1-9][0-9]{0,5})\n$', case_line)
        print("Line has expected format")
        
        # parse the line
        print("Parsing values...")
        s, c = case_line.split()
        steps = int(s)
        complexity = int(c)
        print(f"Done... steps: {steps} complexity: {complexity}")

        #steps_1 should = 1
        if i == 1:
            print("steps_1 should be 1")
            assert steps == 1
            print("steps_1 is valid")
        
        #steps_1 < steps_i < steps_n
        if prev_steps is not None:
            print(f"Validating steps_{i}: {steps} is greater than the previous: {prev_steps}...")
            assert steps <= 100000
            assert steps > prev_steps
            print(f"steps_{i} is valid")
        
        #complexity_1 > complexity_i > complexity_n
        if prev_complexity is not None:
            print(f"Validating complexity_{i}: {complexity} is lesser than the previous: {prev_complexity}...")
            assert complexity <= 100000
            assert complexity < prev_complexity
            print(f"complexity_{i} is valid")
    
        prev_steps = steps
        prev_complexity = complexity

    #complexity_n should = 0
    print(f"complexity_n should be 0")
    assert prev_complexity == 0
    print("complexity_n is valid")

    print("Validating no input left...")
    # ensure no extra input
    assert sys.stdin.readline() == ''
    print("Input file is valid, exiting successfully...")
    
    # if we get here, all is well; use exit code 42.
    sys.exit(42)
except Exception as e:
    print(f"Error: {e}")
    # if we get here, the input is invalid, use exit code 1
    sys.exit(1)
