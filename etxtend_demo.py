from collections import Counter
A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
A2 = [2, 1, 8, 3]
res = []
freq = Counter(A1)


for num in A2:
    # freq[num] -> value of frequency
    # extend is spread operator from js
    res.extend([num] * freq[num])

print(res)