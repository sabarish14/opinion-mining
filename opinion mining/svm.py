from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.feature_extraction.text import TfidfTransformer

from sklearn import metrics
from sklearn import cross_validation
from sklearn.metrics import precision_recall_fscore_support
from metric import find_precision_recall
feature_file=open("romney_words.txt","r") 
class_file=open("romney_labels.txt","r")
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
    count_vect = CountVectorizer()   
    X_train_counts = count_vect.fit_transform(train_features,train_labels)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts,train_labels)
    clf = svm.LinearSVC()
    clf.fit(X_train_counts, train_labels)  
    X_new_counts = count_vect.transform(test_features)
    X_new_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    predicted = clf.predict(X_new_counts)
    accuracy+= metrics.accuracy_score(test_labels, predicted, normalize=True, sample_weight=None)
    metric= precision_recall_fscore_support(test_labels, predicted)
    precision+=metric[0]
    recall+=metric[1]
    fscore+=metric[2]
    predicted,target_names=['-1','0','1']))
precision=precision/10
recall=recall/10
fscore=fscore/10
print precision,"\n", recall,"\n",fscore,"\n"  
print accuracy/10 
#print len(test_labels)       