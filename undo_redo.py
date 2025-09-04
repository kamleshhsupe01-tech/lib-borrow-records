records = {1,2,3,4,0,5,3,0}

average = sum(records) / len(records)
non_zero = [v for v in records if v > 0]
max_borrow = max(records)
min_borrow = min(non_zero)
zero_borrow = list(records).count(0)

from collections import Counter
most_common = Counter(non_zero).most_common(1)[0][0]

print("Average books borrowed:", average)
print("Maximum books borrowed by any member:", max_borrow)
print("Minimum books borrowed by any member (excluding zero):", min_borrow)
print("Members who borrowed 0 books:", zero_borrow)
print("Most frequently borrowed count (mode, excluding zero):", most_common)
