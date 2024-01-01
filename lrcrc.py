from collections import defaultdict


def characterReplacement(s, k):
    l, r = 0, 0
    freq_dict = defaultdict(int)
    max_count = 0
    res = 0

    for r in range(len(s)):
        freq_dict[s[r]] += 1
        max_count = max(max_count, freq_dict[s[r]])

        if r - l + 1 - max_count > k:
            freq_dict[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res


print(characterReplacement("ABABBA", 2))
