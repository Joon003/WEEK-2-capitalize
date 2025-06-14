# alphabet_rangoli.py
# Problem: Print a rangoli pattern of size n using lowercase alphabets.
# Input: integer n
# Output: the rangoli pattern

import string

def print_rangoli(n):
    # List of lowercase letters
    alpha = string.ascii_lowercase
    # Calculate the full width of the pattern
    width = 4 * n - 3

    lines = []
    # Build top half (including middle line)
    for i in range(n):
        # Slice letters for this row: from n-1 down to n-1-i, then back up
        left = alpha[n-1:n-i-1:-1]
        right = alpha[n-i-1:n]
        row = "-".join(left + right[1:])
        lines.append(row.center(width, "-"))

    # Mirror top half (excluding middle) to form bottom half
    full_pattern = lines[::-1] + lines[1:]
    print("\n".join(full_pattern))


if __name__ == "__main__":
    try:
        n = int(input().strip())
        if 1 <= n <= 26:
            print_rangoli(n)
        else:
            print("Error: n must be between 1 and 26")
    except ValueError:
        print("Error: invalid input. Please enter an integer.")
