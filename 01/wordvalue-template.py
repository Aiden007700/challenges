from data import DICTIONARY, LETTER_SCORES

def load_words():
    f = open(DICTIONARY, "r")
    return f.readlines()

def calc_word_value():
    data = load_words()
    return list(len(word) for word in data)

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    pass # run unittests to validate


print(calc_word_value())