string_input = input("Text: ").lower()
word_to_length = {}
words = string_input.split()
maximum_length = 0
for word in words:
    if word not in word_to_length: # check if word is in dictionary
        word_to_length[word] = len(word)
        if len(word) > maximum_length:  # get the length of the longest word
            maximum_length = len(word)

word_to_length_list = [(key, value) for key, value in word_to_length.items()]
word_to_length_list.sort()

for key, value in word_to_length_list:
    print(f"{key:{maximum_length}} : {value}")
