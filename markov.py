"""Generate Markov text from text files."""

from random import choice
import random
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    return open(file_path).read()


def make_chains(text_string, size_n_grams):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here

    split_string = text_string.split()
    split_string.append(" ")


    for index in range(len(split_string) - int(size_n_grams)):
        
        value = []
        key = []
        for n in range(int(size_n_grams)):
            key.append(split_string[index + n])
        
        value = split_string[index + int(size_n_grams)]
        key = tuple(key)

        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]
    return chains


def make_text(chains, size_n_grams):
    """Return text from chains."""
    key = random.choice(list(chains))   
    print(key)

    word_list = list(key)
    print (word_list)

    word_value = random.choice(chains[key])

    while word_value is not " ":
        
        list(key[1:]).append(word_value)
        key = tuple(key)
        word_list.append(word_value)
        word_value = random.choice(chains[key])
   

    
    return " ".join(word_list)


# input_path = "green-eggs.txt"
input_path = sys.argv[1]
input_n_grams = sys.argv[2]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, input_n_grams)

# Produce random text
random_text = make_text(chains, input_n_grams)

print(random_text)
