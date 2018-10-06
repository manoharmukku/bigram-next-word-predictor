# Author: Manohar Mukku
# Date: 04.09.2018
# Desc: Bigram Next Word Predictor (Server)
# Github: https://github.com/manoharmukku/nlp-projects/bigram-next-word-predictor

import sys
from bigram_next_word_predictor import *
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    Handles the requests from Javascript in the client side.
    It is instantiated for very new connection to the server.
    """

    def handle(self):
        current_word = self.request.recv(1024).strip()
        print (current_word)

        # next_words = get_sorted_next_words_for_given_word(conditional_probabilities, current_word)

        # print (next_words)

        # Format next_words as a string to pass it to the client
        # next_words_string = ""
        # for item in next_words:
        #     next_words_string += item[0]
        #     next_words_string += item[1]

        # # Send the next words formatted string to the client
        # self.request.sendall(self.next_words_string)

# Specify the corpus file to train on
corpus_file = "datasets/shakespeare-hamlet.txt"    # Change the corpus file if required, by specifying the new file path

# Open the corpus file and read it into a string 'corpus'
with open(corpus_file, 'r') as myFile:
    corpus = myFile.read().replace('\n', ' ')

# Build the bigram conditional probabilities from the corpus
conditional_probabilities = train_on_corpus(corpus)

# Host and Port to bind to
HOST, PORT = "localhost", 8080

# Create the server, binding to the HOST and PORT
server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

# Activate the server. Keep on running until you press Ctrl-C
server.serve_forever()