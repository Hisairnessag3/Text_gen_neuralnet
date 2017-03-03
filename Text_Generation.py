import numpy
from keras.models import Sequential
from keras.layers import *
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

#converts text to lowercase
filename = "huckfinn.txt"
raw_text = open(filename).read()
raw_text = raw_text.lower()

#Creates Character mapping
chars = sorted(list(set(raw_text)))
chars_to_int = dict((c,i) for i, c in enumerate(chars))

n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)
