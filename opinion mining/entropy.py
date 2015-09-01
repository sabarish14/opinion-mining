from collections import defaultdict
import math
import operator
word_sent_count = defaultdict(dict)
feature_file=open("obama_words.txt","r") 
class_file=open("obama_labels.txt","r")
features=feature_file.readlines()
labels=class_file.readlines()
total_words=[]
entropy_store={}
fs=open("obama_words_filtered.txt","w")
fl=open("obama_labels_filtered.txt","w")
entropy={}
for lines,sentiment in zip(features,labels):
    words=lines.split(',')
    for w in words:
        total_words.append(w)
        try:
            word_sent_count[sentiment][w]+=1
        except KeyError:
            word_sent_count[sentiment][w]=1
total_len=len(total_words)
for k1 in word_sent_count:
    print k1
    n=len(word_sent_count[k1])
    prob_sentiment=float(n)/total_len
    #prob_val=float(1)/n
    for k2 in word_sent_count[k1]:
        
        prob_val=(float(word_sent_count[k1][k2])/n)*prob_sentiment
        temp_entropy=(prob_val*math.log(prob_val,2))
        try:
            entropy[k2]+=temp_entropy
            
        except KeyError:
            entropy[k2]=temp_entropy
            
sorted_x = sorted(entropy.items(), key=operator.itemgetter(1))
#print len(word_sent_count[''])
print len(sorted_x)
feature_vector=[None for i in (range(len(sorted_x)))]    
#print sorted_x[2000:len(sorted_x)]
k=0
for  i in range(0, 8000):
    
    feature_vector[k]=sorted_x[i][0]
    k=k+1
#print feature_vector[8000:8100]

for lines,sentiment in zip(features,labels):
    flag=0
    words=lines.split(",")
    for w in words:
        if w in feature_vector:
            fs.write(w+",")
            flag=1
    if flag==1:
        #fs.write("\n")
        fl.write(sentiment)
        
        
#k=word_sent_count.keys()
#print word_sent_count[k[0]]["#teamobama"]
        
        
        
        
        
            
            
        
        