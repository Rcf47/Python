string = input().lower()
words = string.split()
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

most_frequent_word = max(word_counts, key=word_counts.get)
frequency = word_counts[most_frequent_word]
print(most_frequent_word, frequency)
