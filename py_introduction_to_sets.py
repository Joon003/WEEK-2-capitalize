# Problem: Given N integers, build a set and print its average value.
# Input:
#   N
#   N space-separated integers
# Output: floating‑point average of the unique integers

if __name__ == "__main__":
    n = int(input().strip())
    nums = map(int, input().split())
    unique = set(nums)
    # Compute average in one expression
    print(sum(unique) / len(unique))
