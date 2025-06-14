# Problem: Split S into substrings of length k.
#   For each substring, remove subsequent occurrences of any character.
# Input:
#   S (string)
#   k (int)
# Output: each cleaned substring on its own line

def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        segment = s[i:i+k]
        seen = set()
        output = []
        for ch in segment:
            if ch not in seen:
                seen.add(ch)
                output.append(ch)
        print("".join(output))

if __name__ == "__main__":
    s = input().strip()
    k = int(input().strip())
    merge_the_tools(s, k)
