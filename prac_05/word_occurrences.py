string_input = input("Text: ").lower()
word_to_length = {}
words = string_input.split()
for word in words:
    if word not in word_to_length:
        word_to_length[word] = len(word)

for key, value in word_to_length.items():
    print(f"{key} : {value}")
