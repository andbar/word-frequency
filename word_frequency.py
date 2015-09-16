import string

with open("sample.txt") as infile:
    my_string = infile.read()


word_dict = {}

def get_word_list(string_1):
    for char in string_1:
        if char in string.punctuation:
           string_1 = string_1.replace(char, "")
    word_list = string_1.lower().split()
    return word_list



def get_word_count(list_1):
    for word in list_1:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    list_with_count = [(key, value) for key, value in word_dict.items()]
    sorted_list = sorted(list_with_count, key=lambda tup: tup[1], reverse=True)
    first_20 = sorted_list[:20]
    for pair in first_20:
        print(pair[0], pair[1])
    

get_word_count(get_word_list(my_string))
