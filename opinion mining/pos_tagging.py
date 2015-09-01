import nltk
from nltk import word_tokenize
from nltk.tag.hunpos import HunposTagger
ht = HunposTagger('en_wsj.model')

text =word_tokenize("Obama supports Slaughter ")
print ht.tag('Not all of hollywood has his back  Gene Simmons yanks Obama support, calls him a piss poor president'.split())