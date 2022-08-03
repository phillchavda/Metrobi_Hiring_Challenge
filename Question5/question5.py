#   Challenge: Write a testing program for a function that receives an input file (input.txt) and an
# output file (output.txt). Each line of these files corresponds to sample input and expected
# output. In the end, a report (results.txt) is generated with pass/fail for each test. If there is a
# fail, write what was the input, the expected output, and the actual output.
# Finally, write the necessary test files to test the functionality of the code below:

#!/usr/bin/env python

def isPrimeNumber_v1 (n):
    for i in range(2,n):
        if (n % i) == 0:
            return False
        else:
            return True

def isPrimeNumber_v2 (n):
    xrange = range
    return 0 not in map(lambda i: n % i, xrange(2, int(n**0.5+1)))