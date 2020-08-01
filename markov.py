"""Generate Markov text from text files."""

import random 
from collections import defaultdict

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file = open(file_path)
    contents = file.read()
    file.close()

    return contents


def make_chains(text_string):
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

    # chains = {}

    # # your code goes here
    text = text_string.split()
    # for idx in range(0,len(text)-1):
    #     key = (text[idx], text[idx + 1])
    #     value = text[idx+2]
    #     chains[key] = chains.get(key,[]) + [value]
    
    chains = defaultdict(list)

    for idx in range(0,len(text)-2):
        key = (text[idx], text[idx + 1])
        value = text[idx+2]
        chains[key].append(value)
        
        

    return chains


def make_text(chains):
    """Return text from chains."""

    
    '''
    words=[would,you]
    key= (would, you)

    words.append(like)
    words[would,you,like]
    key (you, like)
    
    '''

    link = random.choice(list(chains.keys()))
    words= [link[0],link[1]]
    words.append(random.choice(chains[link]))
    key = (words[-2],words[-1])

    
    while key in chains :
        word = random.choice(chains[key])
        words.append(word)
        key = (words[-2],words[-1])
    

    return " ".join(words)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)

input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)