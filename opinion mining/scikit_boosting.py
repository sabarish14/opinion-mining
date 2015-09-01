from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from preprocess import  preprocess
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn import cross_validation
from sklearn.metrics import precision_recall_fscore_support
p=preprocess()
feature_file=open("obama_words.txt","r") 
class_file=open("obama_labels.txt","r")
features=feature_file.readlines()
labels=class_file.readlines()
i=0
for str in labels:
    labels[i]=str.replace("\n", "")
    i=i+1
kf = cross_validation.StratifiedKFold(labels, n_folds=10,shuffle=False)
accuracy=0
precision=[0 for i in range(3)]
recall=[0 for i in range(3)]
fscore=[0 for i in range(3)]
for train_index, test_index in kf:
        #print("TRAIN:", (train_index), "TEST:", (test_index)) 
    train_features=list( features[i] for i in train_index ) 
    train_labels=list( labels[i] for i in train_index )
    test_features=list( features[i] for i in test_index )
    test_labels=list( labels[i] for i in test_index )
    count_vect = CountVectorizer(ngram_range=(1, 3))
    X_train_counts = count_vect.fit_transform(train_features)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    clf = AdaBoostClassifier(n_estimators=100)
    clf.fit(X_train_tfidf, train_labels)  
    X_new_counts = count_vect.transform(test_features)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    predicted = clf.predict(X_new_tfidf)
    accuracy+= metrics.accuracy_score(test_labels, predicted, normalize=True, sample_weight=None)
    metric= precision_recall_fscore_support(test_labels, predicted)
    precision+=metric[0]
    recall+=metric[1]
    fscore+=metric[2]
        #for doc, category,actual in zip(test_features, predicted,test_labels):
            #print('%r => predicted: %s   actual:%s ' % (doc, category,actual))
    #print(metrics.classification_report(test_labels, predicted,target_names=['-1','0','1']))
precision=precision/10
recall=recall/10
fscore=fscore/10
print precision,"\n", recall,"\n",fscore,"\n"  
print accuracy/10 
#print len(test_labels)       