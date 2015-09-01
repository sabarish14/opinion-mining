from textblob import TextBlob
import xlrd 
book = xlrd.open_workbook("training-Obama-Romney-tweets.xlsx")
feature_file=open("obama_words.txt","r") 
class_file=open("obama_labels.txt","r")
features=feature_file.readlines()
labels=class_file.readlines()
worksheet = book.sheet_by_index(0)
end_val=10
start_val=2
features= worksheet.cell_value(2, 3)
dummy=features[0]
for sentence in dummy:
    print features
    testimonial=TextBlob("I'm a good boy")
    print testimonial.sentiment