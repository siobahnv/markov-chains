"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    return open(file_path).read()


def make_chains(text_string, n_grams):
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
    counter = 0

    while counter < (len(split_string) - n_grams):
        key = []
        value = []

        for n in range(n_grams):
            new_count = (counter) + n
            (key.append(split_string[new_count]))
        
        key = tuple(key)
        value = split_string[new_count + 1]

        if key not in chains:
            chains[key] = [value]
        else:
            chains[key].append(value)

        counter += 1
    return chains

def make_text(chains, n_grams):

    key = choice(list(chains))
    word_list = list(key)
    word_value = choice(chains[key])

    while word_value is not " ":
        key = (key[1::])
        key = list(key)
        key.append(word_value)
        key = tuple(key)
        word_list.append(word_value)
        word_value = choice(chains[key])


    return " ".join(word_list)




input_path = sys.argv[1]
second_input = sys.argv[2]
n_grams = int(sys.argv[3])
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
second_text = open_and_read_file(second_input)
input_text = input_text + second_text
# Get a Markov chain
chains = make_chains(input_text, n_grams)
# Produce random text
random_text = make_text(chains, n_grams)

print(random_text)