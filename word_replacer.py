with open("Fierce_Bad_Rabbit.txt", "r") as book:
    content = book.read()

# Function to replace words in the content
def word_replacement(old_text, new_text, text):
    return text.replace(old_text, new_text)

# Replace "Rabbit" with "Dragon"
new_content = word_replacement("Rabbit", "Dragon", content)
new_content = word_replacement("Carrot","Flesh", content)
# Write the new content to a new file
with open("Fierce_Bad_Dragon.txt", "w") as new_file:
    new_file.write(new_content)