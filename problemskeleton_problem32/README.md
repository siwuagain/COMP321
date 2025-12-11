# Problem Testing Guide

This guide explains how to test the different components of the problem submission.

## Directory Structure

From the `problemskeleton_problem32` directory:
- Solutions are in `./submissions/[type]` under their respective type:
  - `accepted`
  - `run_time_error`
  - `time_limit_exceeded`
  - `wrong_answer`

## Running Solutions

### Optimal Solution (Python)
```bash
python3 ./submissions/accepted/accepted.py < ./data/secret/secret_mixed_large.in
```

### Time Limit Exceeded Solution
You might be interested in running the TLE solution and taking notice of the considerable amount of time it takes compared to the optimal one:
```bash
python3 ./submissions/time_limit_exceeded/tle.py < ./data/secret/secret_mixed_large.in
```

## Test Data

Input/output files are located in `./data/[sample | secret]`:
- **Sample data**: Contains hard-coded cases that test behaviors on small input, with equivalents that test on big inputs (in `./data/secret`)
- **Secret data**: Contains larger test cases, with the rest randomly generated using the test case generator

## Test Case Generator

Run the test case generator:
```bash
python3 ./test_case_generator/generate.py
```

We created a solver function in `./test_case_generator/solver.py` to help generate the answer files.

## Input Validator

The input validator is in `./input_format_validators/`

Run it on a test case:
```bash
python3 ./input_format_validators/validate.py < data/secret/secret_mixed_large.in
```
