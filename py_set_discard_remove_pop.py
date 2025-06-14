# Problem: Start with a set of integers, then apply operations.
# Input:
#   n (size of set)
#   line of n space-separated ints
#   N (number of operations)
#   next N lines: "<operation> [value]"
# Output: sum of remaining elements in the set

if __name__ == "__main__":
    n = int(input().strip())
    s = set(map(int, input().split()))
    for _ in range(int(input().strip())):
        parts = input().split()
        op = parts[0]
        if op == "pop":
            s.pop()
        else:
            # discard/remove take one argument
            getattr(s, op)(int(parts[1]))
    print(sum(s))
