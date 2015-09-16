import string

with open("sample.txt") as infile:
    test_string = infile.read()


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
    return word_dict


def sort_list(dict_1):
    sorted_list = [(key, value) for key, value in dict_1.items()]
    sorted_list = sorted(sorted_list, key=lambda tup: tup[1], reverse=True)
    first_20 = sorted_list[:20]
    return first_20


def word_frequency(my_string):
    return get_word_count(get_word_list(my_string))
    
#sort_list(get_word_count(get_word_list(test_string)))
#word_frequency(test_string)

# sort_list is for the normal mode exercise, to output 20 most frequent words in descending order
# using sort_list causes the test file to fail
    
