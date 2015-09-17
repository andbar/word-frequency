import string

with open("sample.txt") as infile:
    test_string = infile.read()


words_dont_want = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an', 'and', 'any',
                   'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear', 'did',
                   'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have',
                   'he', 'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its',
                   'just', 'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'neither',
                   'no', 'nor', 'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said',
                   'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then',
                   'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us', 'wants', 'was', 'we', 'were',
                   'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet',
                   'you', 'your']


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


def remove_words(list_2, dict_2):
    for w in list_2:
        if w in dict_2:
            del dict_2[w]
    return dict_2


def sort_list(dict_1):
    sorted_list = [(key, value) for key, value in dict_1.items()]
    sorted_list = sorted(sorted_list, key=lambda tup: tup[1], reverse=True)
    first_20 = sorted_list[:20]
    return first_20


def word_frequency(my_string):
    return get_word_count(get_word_list(my_string))

def important_word_frequency(your_string):
    return remove_words(words_dont_want, word_frequency(your_string))
    
#sort_list(word_frequency(test_string))
#word_frequency(test_string)

# sort_list is for the normal mode exercise, to output 20 most frequent words in descending order
# using sort_list causes the test file to fail
    
