# Problem: Given a string, capitalize the first letter of each word.
# Input: a single line string
# Output: the same string with each word’s first letter capitalized

def solve(s):
    # Split on spaces, capitalize each word, then rejoin
    return " ".join(word.capitalize() for word in s.split(" "))

if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
