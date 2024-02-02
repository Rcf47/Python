text = input()
words = text.split()

punctuation = """!.,?;:#$%^&*(),"""
words = [word.translate(str.maketrans("", "", punctuation)).lower() for word in words]
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

filtered_words = [
    word
    for word, count in word_counts.items()
    if len(word) >= 5 and len(set(word)) >= 4 and count > 2
]

filtered_words.sort()


for word in filtered_words:
    print(word)
