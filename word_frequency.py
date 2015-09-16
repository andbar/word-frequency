import string

my_string = "I like to read books books!"
word_dict = {}

def remove_punc(string_1):
    for char in string_1:
        if char in string.punctuation:
           string_1 = string_1.replace(char, "")
    return string_1.lower()

new_string = remove_punc(my_string).split()

for word in new_string:
    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        word_dict[word] = 1
        
print(word_dict)
