import sys

index_filename = sys.argv[1]

import shelve

import nltk
from nltk.corpus import gutenberg
from nltk.corpus import reuters
with shelve.open(index_filename, 'c') as index:
    for document_id in reuters.fileids()[:100]:
        tokens = nltk.word_tokenize(reuters.raw(document_id))
        for term in tokens:
            if term not in index: 
                index[term] = []
            # index[term].append(document_id)
            words = index[term]
            words.append(document_id)
            index[term] = words
            # print(term, index[term], '\n')
    index.sync()
    print(len(index))

