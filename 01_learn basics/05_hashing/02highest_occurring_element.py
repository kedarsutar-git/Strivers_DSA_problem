arr = [2, 3, 5, 3, 2, 3, 3, 4]

freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

highest = max(freq, key=freq.get)

print("Highest occurring element:", highest)
print("Frequency:", freq[highest])




