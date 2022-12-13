from collections import Counter
print(Counter(open("names.txt", "r").read().split()))