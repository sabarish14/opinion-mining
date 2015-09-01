from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
feature_file=open("obama_words.txt","r") 
class_file=open("obama_labels.txt","r")
features=feature_file.readlines()
labels=class_file.readlines()
features=features[0:2]
print features
#text=["kirkpatrick,wore,basebal,cap,embroid,barack,obama',signatur,hangdog,look,jason,segel,courier,journal"]
count_vect = CountVectorizer()   
X_train_counts = count_vect.fit_transform(features)
print count_vect.vocabulary_
print X_train_counts
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print X_train_tfidf
clf=MultinomialNB()
#clf.fit(X_train_counts, , sample_weight)
