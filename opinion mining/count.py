def count():
    class_file=open("sentiment.txt","r")
    labels=class_file.readlines()
    count=[0 for i in range(3)]
    for i in labels:
        i=i.replace("\n", "")
        i=float(i)
        i=int(i)
        count[i+1]+=1
    print count

count()