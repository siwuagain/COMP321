#!/usr/bin/env python3

import sys
import re

######
try:
    n_line = sys.stdin.readline()
    print(repr(n_line)) # useful for debugging to see where we have read
    assert re.match('^[1-9][0-9]*\n$', n_line) # note: no leading zeros
    n = int(n_line)
    assert 1 <= n <= 100000

    prev_steps = prev_complexity = None
    for i in range(1, n+1):
        case_line = sys.stdin.readline()
        
        print(f"current line: {i + 1}")
        print(f"Validating line format {repr(case_line)} against regex...")
        assert re.match('^(0|[1-9][0-9]*) (0|[1-9][0-9]*)\n$', case_line)
        print("Done validating line format against regex..")
        # parse the line

        print("Parsing line values...")
        s, c = case_line.split()
        steps = int(s)
        complexity = int(c)
        print(f"Done parsing line values... steps: {steps} complexity: {complexity}")

        #steps_1 should = 1
        if i == 1:
            print("Validating first trap's step value")
            assert steps == 1
            print("Done validating first trap's step value")
        
        #steps_1 < steps_i < steps_n
        if prev_steps is not None:
            print(f"Validating current steps value {steps} is greater than the previous {prev_steps}...")
            assert steps > prev_steps
            print("Steps value is valid")
        
        #complexity_1 > complexity_i > complexity_n
        if prev_complexity is not None:
            print(f"Validating current complexity value {complexity} is lesser than the previous {prev_complexity}...")
            assert complexity < prev_complexity
            print("Complexity value is valid")
    
        prev_steps = steps
        prev_complexity = complexity

    #complexity_n should = 0
    print(f"Validating last complexity's value {prev_complexity}")
    assert prev_complexity == 0
    print("Done validating last complexity's value")

    print("Validating no input left...")
    # ensure no extra input
    assert sys.stdin.readline() == ''
    print("Input file is valid, exiting successfully...")
    
    # if we get here, all is well; use exit code 42.
    sys.exit(42)
except:
    # if we get here, the input is invalid, use exit code 1
    sys.exit(1)
