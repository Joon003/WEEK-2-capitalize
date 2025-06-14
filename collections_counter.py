# Problem: Given records of purchases (item name and price),
#   compute total earned per item then answer queries.
# Input:
#   N (number of records)
#   next N lines: "<item> <price>"
#   Q (number of queries)
#   next Q lines: "<item>"
# Output: for each query, print total earned amount for that item

from collections import Counter
import sys

if __name__ == "__main__":
    data = Counter()
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        item, price = sys.stdin.readline().split()
        data[item] += int(price)
    q = int(sys.stdin.readline().strip())
    for _ in range(q):
        query = sys.stdin.readline().strip()
        print(data[query])
