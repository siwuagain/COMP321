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
        print(repr(case_line)) # useful for debugging to see where we have read
        # check the line syntax (integer, integer)
        assert re.match('^[1-9][0-9]* (0|[1-9][0-9]*)\n$', case_line)

        # parse the line
        s, c = case_line.split()
        steps = int(s)
        complexity = int(c)

        #steps_1 should = 1
        if i == 1:
            assert steps == 1
        
        #steps_1 < steps_i < steps_n
        if prev_steps is not None:
            assert steps > prev_steps
        
        #complexity_1 > complexity_i > complexity_n
        if prev_complexity is not None:
            assert complexity < prev_complexity
    
        prev_steps = steps
        prev_complexity = complexity

    #complexity_n should = 0
    assert prev_complexity == 0

    # ensure no extra input
    assert sys.stdin.readline() == ''

    # if we get here, all is well; use exit code 42.
    sys.exit(42)
except:
    # if we get here, the input is invalid, use exit code 1
    sys.exit(1)
