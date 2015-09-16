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
    list_with_count = [(key, value) for key, value in word_dict.items()]
    return list_with_count

# sort_list is for the normal mode exercise, to output 20 most frequent words in descending order
# using sort_list causes the test file to fail
def sort_list(unsorted_list):
    sorted_list = sorted(unsorted_list, key=lambda tup: tup[1], reverse=True)
    first_20 = sorted_list[:20]
    return first_20


def word_dictionary(counted_list):
    return dict(counted_list)


def word_frequency(my_string):
    return word_dictionary(get_word_count(get_word_list(my_string)))
    
