import re
from collections import defaultdict

def extract_hash_words():
    fh=open("hash_words.txt","w")
    fl=open("hash_labels.txt","w")
    feature_file=open("obama_words.txt","r") 
    class_file=open("obama_labels.txt","r")
    tweet=feature_file.readlines()
    labels=class_file.readlines()
    
    for lines,label in zip(tweet,labels):
        flag=0
        
        words=lines.split(',')
        for w in words:
        
            match=re.match( r'#.*',w)
            if match:
                flag=1
                fh.write(w+",")
        if flag==1:
            fh.write("\n")
            fl.write(label)
        
    #print hash_words
def cluster_hash_words():
    hash_file=open("hash_words.txt","r") 
    hash_words=hash_file.readlines()
    d2_dict = defaultdict(dict)
    fh=open("hash_cluster.txt","w")
    for lines in hash_words:
        
        words=lines.split(',')
        n=len(words)
        sentiment=words[n-1]
        sentiment=sentiment.replace("\n", "")
        for i in range(n-1):
            if d2_dict.has_key(words[i]) and  d2_dict[words[i]].has_key(sentiment):
                d2_dict[words[i]][sentiment]+=1
            else:
                d2_dict[words[i]][sentiment]=1
    
    print d2_dict     
    for k1 in d2_dict.keys():
        for k2 in d2_dict[k1].keys():
            fh.write(k1+" "+k2+"  "+ str(d2_dict[k1][k2]))
            fh.write("\n")
            
        
extract_hash_words()
cluster_hash_words()
        