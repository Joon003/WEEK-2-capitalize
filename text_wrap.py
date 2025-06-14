# Problem: Wrap a string into lines of width w.
# Input:
#   s (string)
#   w (integer line width)
# Output: the wrapped paragraph

import textwrap

if __name__ == "__main__":
    s = input().strip()
    w = int(input().strip())
    # textwrap.fill returns the wrapped text directly
    print(textwrap.fill(s, w))
