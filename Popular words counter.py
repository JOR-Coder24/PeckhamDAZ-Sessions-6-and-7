# Open and read the file
with open("Fierce_Bad_Rabbit.txt", "r") as book:
    content = book.read()

# Remove punctuation
punc = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
for char in punc:
    content = content.replace(char, "")

# Split content into words
words = content.split()


# Function to find the most frequent words
def top_frequent(words_list, n=5):
    word_frequency = {}

    for word in words_list:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    sorted_words = sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:n]


# Find and print the top 5 most frequent words
f=open("Word count.txt","w")
top_words = top_frequent(words)
for word, frequency in top_words:
    print(f"{word}: {frequency}")
    f.write(f" {word}: {frequency} ")
