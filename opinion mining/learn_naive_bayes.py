from sklearn.feature_extraction.text import CountVectorizer
'''from preprocess import  preprocess
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn import cross_validation
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
from sklearn.cross_validation import StratifiedShuffleSplit
from balance_train_data import balance_data
from balance_train_data import voting'''

feature_file=open("obama_words_filtered.txt","r") 
class_file=open("obama_labels_filtered.txt","r")
features=feature_file.readlines()
labels=class_file.readlines()
train_features=list(features[i] for i in range(0,2))
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(train_features)
print X_train_counts