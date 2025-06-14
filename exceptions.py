# Problem: For each a, b pair, print a//b or catch and report errors.
# Input:
#   T (number of test cases)
#   next T lines: two values a and b
# Output:
#   result of a//b or "Error Code: <message>"

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except Exception as e:
            print("Error Code:", e)
