
def find_precision_recall(predicted,label):
    ap={}
    #true positive
    tp={}
    predicted_postive={}
    unique_labels=['-1.0', '0.0', '1.0']
    for i in range(len(label)):
        for j in range(len(unique_labels)):
            if (label[i]==predicted[i]) and (label[i]==unique_labels[j]):
                try:
                    tp[label[i]]+=1
                except KeyError:
                    tp[label[i]]=1
        try:
            ap[label[i]]+=1
            
        except KeyError:
            
            ap[label[i]]=1
        try:
            predicted_postive[predicted[i]]+=1
        except KeyError:
            predicted_postive[predicted[i]]=1
    fp={}
    fn={}
    precision={}
    recall={}
       
    for key in ap.keys():
        fp[key]=predicted_postive[key]-tp[key]
        fn[key]=ap[key]-tp[key]
        precision[key]=float(tp[key])/(float(tp[key]+fp[key]))
        recall[key]=float(tp[key])/float((tp[key]+fn[key]))
    '''print "true positive",tp
    print "false positive:",fp
    print " false negative:",fn'''
    print "precision", precision
    print "recall",recall
    
    
    
    
    