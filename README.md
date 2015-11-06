# opinion-mining
This is the course project for CS 582 -Data and Text mining. This tool predicts the sentiment of a tweet ( positive,negative or neutral). The dataset used is the set of 7500 tweets from 2012 US Presidential elections.
#Usage:
Run the preprocess_main.py  to preprocess the tweets file.It will clean the data by removing stop words, apply stemming and store Obama and Romney tweets in two separate files.
Run the naivebayes.py to use Naive Bayes classifier to predict the sentiment of a tweet. 
Run the svm.py to use the SVM classifier to predict the sentiment of a tweet
Run the svm_bagging.py to use the SVM classifier with bagging to predict the sentiment of a tweet
