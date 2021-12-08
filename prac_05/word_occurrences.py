string_input = input("Text: ").lower()
word_to_length = {}
words = string_input.split()
for word in words:
    if word not in word_to_length:
        word_to_length[word] = len(word)

word_to_length_list = [(key, value) for key, value in word_to_length.items()]
word_to_length_list.sort()

for key, value in word_to_length_list:
    print(f"{key} : {value}")
