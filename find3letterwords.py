# find 3 letter words starting with b inside a file
import sys
punctuation = ", . ? !' ;\""
def find_words(filename):
    """
    Prints 3 letter words starting with b from a file
    :param filename: the name ofthe file
    :return: None (nothing)
    """
    with open(filename) as f:
        for line in f:
            for p in punctuation:
                line = line.replace(p," ")
            words = line-split()
            for word in words:
                if len(word) == 4 and word[0] in "bB":
                    print(word)
find_words("input.txt")