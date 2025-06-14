# exceptions.py
# Problem: For each a, b pair, print a//b or catch and report errors.
# Input:
#   T (number of test cases)
#   next T lines: two values a and b
# Output:
#   result of a//b or "Error Code: <message>"

import sys

def read_int():
    """Keep reading lines until we get a valid integer."""
    while True:
        line = sys.stdin.readline()
        if not line:
            # EOF—stop trying
            sys.exit()
        line = line.strip()
        try:
            return int(line)
        except ValueError:
            # skip this line and try the next
            continue

def main():
    t = read_int()
    for _ in range(t):
        # Read the next non-empty line
        while True:
            line = sys.stdin.readline()
            if not line:
                sys.exit()
            parts = line.strip().split()
            if parts:
                break

        try:
            a, b = map(int, parts)
            print(a // b)
        except Exception as e:
            print("Error Code:", e)

if __name__ == "__main__":
    main()
