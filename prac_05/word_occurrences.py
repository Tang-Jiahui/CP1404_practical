"""
Word Occurrences
Estimate: 30 minutes
Actual:   50 minutes
"""

result = {}
max_length = 0
text = input("Text:")
words = text.split()
words.sort()
for i in range(0, len(words)):
    count_number = words.count(words[i])
    result[words[i]] = count_number
    if len(words[i]) > max_length:
        max_length = len(words[i])

for i in range(0, len(result)):
    print(f"{list(result.keys())[i]:{max_length}} = {list(result.values())[i]}")