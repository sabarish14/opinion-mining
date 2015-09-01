from sklearn.feature_extraction.text import CountVectorizer
from preprocess import  preprocess
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn import cross_validation
def tf_idf_transfrom():
    p=preprocess()
    feature_file=open("featurelist1.txt","r") 
    class_file=open("sentiment.txt","r")
    features=feature_file.readlines()
    labels=class_file.readlines()
    i=0
    for str in labels:
        labels[i]=str.replace("\n", "")
        i=i+1
    kf = cross_validation.KFold(len(features), n_folds=10)
    accuracy=0
    for train_index, test_index in kf:
        #print("TRAIN:", (train_index), "TEST:", (test_index)) 
        train_features=list( features[i] for i in train_index ) 
        train_labels=list( labels[i] for i in train_index )
        test_features=list( features[i] for i in test_index )
        test_labels=list( labels[i] for i in test_index )
        count_vect = CountVectorizer()
        X_train_counts = count_vect.fit_transform(train_features)
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)