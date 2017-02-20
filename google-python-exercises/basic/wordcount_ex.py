#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""


import sys

def make_word_list(filename):
    """Returns a word frequency list (of tuples)."""
    f = open(filename, "rU")
    text = f.read()
    words = text.split() #creates a list of all the words in the text
    word_freq = {}
    for word in words: #creates a dictionary of all words as keys with their
    #frequency as values
        word = word.lower() # converts all words to lowercase
        if word in word_freq:
            word_freq[word] += 1 # if a word is already in the dictionary,
            #it increases its frequency value by one
        else:
            word_freq[word] = 1 # if the word isn't already in the dictionary it
            #is added with frequency value 1
    word_list = sorted(word_freq.items(), key = lambda x: (-x[-1], x[0]))
    #Converts the dictionary to a list of tuples and sorts it with two keys,
    #using a lambda function that first returns the value in reverse order
    #(using minus '-' on an int) and then returns the key in ascending order
    #Thank you StackOverflow!
    return word_list
    f.close()

def print_words(filename):
    """Prints all the words along with their frequency."""
    word_list = make_word_list(filename)
    print "Here are all off the words by frequency of occurcence in descending order:"
    for word in word_list:
        print word[0], word[1]

def print_top(filename):
    """Prints the top 20 most frequent words in the file."""
    word_list = make_word_list(filename)
    print "Here are the top 20 most frequent words:"
    for word in word_list[:21]:
        print word[0], word[1]

def main():
    print_words(sys.argv[1])
    print_top(sys.argv[1])

if __name__ == '__main__':
    main()
