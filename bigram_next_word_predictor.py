# Author: Manohar Mukku
# Date: 04.09.2018
# Desc: Bigram Next Word Predictor
# Github: https://github.com/manoharmukku/nlp-projects/bigram-next-word-predictor

from collections import defaultdict
from operator import itemgetter
import re

def train_on_corpus(corpus):
    """
    This function builds a dictionary of conditional probability
    for a next word given a current word, for all the pairs of current
    and next words
    """

    # Remove punctuations from the corpus
    corpus = re.sub(r'[^\w\s]', '', corpus)

    # Split the corpus into individual words and then convert to lower case
    all_words = [word.lower() for word in corpus.split()]

    # Dictionary which stores the conditional probabilities of the next words for a given word
    next_words_dict = defaultdict(list)

    # For each word in all_words, append its next word to the dictionary[current_word]

    current_word = ""
    for next_word in all_words:
        if (current_word != ""):
            next_words_dict[current_word].append(next_word)
        current_word = next_word

    # Find the conditional probability for each next word of a current word as follows:
    # prob(next_word/current_word) = count(next_word given current_word) / count(next_words for given current_word)
    # conditional_probabilities[current_word][next_word] = cond. probability for the next word appearing given the current word appeared

    conditional_probabilities = {}

    for key in next_words_dict.keys():
        next_words = next_words_dict[key]
        unique_next_words = set(next_words)
        n_next_words = len(next_words)

        cond_probs_for_key = {}

        for unique_next_word in unique_next_words:
            cond_probs_for_key[unique_next_word] = (float)(next_words.count(unique_next_word)) / n_next_words

        conditional_probabilities[key] = cond_probs_for_key

    return conditional_probabilities

def get_sorted_next_words_for_given_word(conditional_probabilities, current_word):
    """
    This function returns a list of next words with probabilities, for the given current word,
    sorted descending with respect to the conditional probabilities for the
    next word given the current word, using the conditional probabilities
    dictionary specified
    """

    # Convert the current word to lower case
    current_word = current_word.lower()

    next_words = []

    if (current_word in conditional_probabilities):
        probs = conditional_probabilities[current_word]
        next_words = sorted(probs.items(), key=itemgetter(1), reverse=True)

    return next_words
