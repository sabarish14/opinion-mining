import re, math, collections, itertools
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist
from nltk.collocations import BigramCollocationFinder

global best_words
def evaluate_features(feature_select):
    posSentences = open('positive-obama.txt', 'r')
    negSentences = open('negative-obama.txt', 'r')
    neutralSentences = open('neutral-obama.txt', 'r')
    print feature_select
    posSentences = re.split(r'\n', posSentences.read())
    negSentences = re.split(r'\n', negSentences.read())
    neutralSentences=re.split(r'\n', neutralSentences.read())
    
    posFeatures = []
    negFeatures = []
    neuFeatures = []
    #http://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation
    #breaks up the sentences into lists of individual words (as selected by the input mechanism) and appends 'pos' or 'neg' after each list
    for i in posSentences:
        posWords = re.findall(r"[\w']+|[.,!?;]", i)
        
        posWords = [best_word_features(posWords), 'pos']
        posFeatures.append(posWords)
        
    for i in negSentences:
        negWords = re.findall(r"[\w']+|[.,!?;]", i)
        negWords = [best_word_features(negWords), 'neg']
        negFeatures.append(negWords)
    
    for i in neutralSentences:
        neuWords = re.findall(r"[\w']+|[.,!?;]", i)
        neuWords = [best_word_features(neuWords), 'neu']
        neuFeatures.append(neuWords)
   
    #selects 3/4 of the features to be used for training and 1/4 to be used for testing
    posCutoff = int(math.floor(len(posFeatures)*3/4))
    negCutoff = int(math.floor(len(negFeatures)*3/4))
    neuCutoff = int(math.floor(len(neuFeatures)*3/4))
    trainFeatures = posFeatures[:posCutoff] + negFeatures[:negCutoff] + neuFeatures[:neuCutoff]
    testFeatures = posFeatures[posCutoff:] + negFeatures[negCutoff:] + neuFeatures[neuCutoff:]
    referenceSets = collections.defaultdict(set)
    testSets = collections.defaultdict(set)
    classifier = NaiveBayesClassifier.train(trainFeatures)
    
    for i, (features, label) in enumerate(testFeatures):
        referenceSets[label].add(i)
        predicted = classifier.classify(features)
        testSets[predicted].add(i)

    print 'train on %d instances, test on %d instances' % (len(trainFeatures), len(testFeatures))
    print 'accuracy:', nltk.classify.util.accuracy(classifier, testFeatures)
    print 'pos precision:', nltk.metrics.precision(referenceSets['pos'], testSets['pos'])
    print 'pos recall:', nltk.metrics.recall(referenceSets['pos'], testSets['pos'])
    print 'neg precision:', nltk.metrics.precision(referenceSets['neg'], testSets['neg'])
    print 'neg recall:', nltk.metrics.recall(referenceSets['neg'], testSets['neg'])
    print 'neu precision:', nltk.metrics.precision(referenceSets['neu'], testSets['neu'])
    print 'neu recall:', nltk.metrics.recall(referenceSets['neu'], testSets['neu'])
       

def create_word_scores():
    posSentences = open('positive-obama.txt', 'r')
    negSentences = open('negative-obama.txt', 'r')
    neutralSentences = open('neutral-obama.txt', 'r')

    posSentences = re.split(r'\n', posSentences.read())
    negSentences = re.split(r'\n', negSentences.read())
    neutralSentences=re.split(r'\n', neutralSentences.read())
    posWords=[]
    negWords=[]
    neuWords=[]
    allWords=[]
    for i in posSentences:
        pos = re.findall(r"[\w']+|[.,!?;]", i)
        
        #posWords = [feature_select(posWords), 'pos']
        posWords.extend(pos)
    allWords.extend(posWords)   
    for i in negSentences:
        neg = re.findall(r"[\w']+|[.,!?;]", i)
        #negWords = [feature_select(negWords), 'neg']
        negWords.extend(neg)
    allWords.extend(negWords)    
    for i in neutralSentences:
        neu = re.findall(r"[\w']+|[.,!?;]", i)
        #neuWords = [feature_select(neuWords), 'neu']
        neuWords.extend(neu)
    allWords.extend(neuWords)
    
    word_fd=nltk.FreqDist(allWords)
    cond_word_fd = ConditionalFreqDist()
    for word in posWords:
        cond_word_fd['pos'][word]+=1
  
    
    for word in negWords:
        cond_word_fd['neg'][word]+=1
  
    for word in neuWords:
        cond_word_fd['neu'][word]+=1
  
    pos_word_count = cond_word_fd['pos'].N()
    neg_word_count = cond_word_fd['neg'].N()
    neu_word_count = cond_word_fd['neu'].N()
    total_word_count = pos_word_count + neg_word_count + neu_word_count
    word_scores = {}
    postweet= open("pos_best_words.txt","w")
    negtweet= open("neg_best_words.txt","w")
    neutweet= open("neu_best_words.txt","w")
    
    for word, freq in word_fd.iteritems():
        pos_score = BigramAssocMeasures.chi_sq(cond_word_fd['pos'][word],
            (freq, pos_word_count), total_word_count)
        postweet.write(word + " ")
        postweet.write(str(pos_score))
        postweet.write("\n")
        neg_score = BigramAssocMeasures.chi_sq(cond_word_fd['neg'][word],
            (freq, neg_word_count), total_word_count)
        negtweet.write(word + " ")
        negtweet.write(str(neg_score)) 
        negtweet.write("\n")
        neu_score = BigramAssocMeasures.chi_sq(cond_word_fd['neu'][word],
            (freq, neg_word_count), total_word_count)
        neutweet.write(word + " ")
        neutweet.write(str(pos_score))
        neutweet.write("\n")
        word_scores[word] = pos_score + neg_score + neu_score
    
    return word_scores

def find_best_words(word_scores, number):
    best_vals = sorted(word_scores.iteritems(), key=lambda (w, s): s, reverse=True)[:number]
    best_words = set([w for w, s in best_vals])
    return best_words 

def best_word_features(words):
    global best_words
    return dict([(word, True) for word in words if word in best_words])
    
word_scores = create_word_scores()

best_words = find_best_words(word_scores, 50000)
tweet= open("best_words.txt","w")
for x in best_words:
    tweet.write(x+ " ")

evaluate_features(best_word_features)
#print 'evaluating best words + bigram chi_sq word features'
#evaluate_features(best_bigram_word_feats)    
        