# Enter your code here. Read input from STDIN. Print output to STDOUT
 
import re
import sys

lines = sys.stdin.read().splitlines()
N = int(lines[0])

for i in range(1, N + 1):
    pattern = lines[i]
    try:
        re.compile(pattern)
        print(True)
    except re.error:
        print(False)