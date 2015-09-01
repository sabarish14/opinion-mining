import xlrd
from collections import defaultdict
book = xlrd.open_workbook("training-Obama-Romney-tweets.xlsx")
worksheet = book.sheet_by_index(0)
end=worksheet.nrows
start=2
num_rows = end-1
        #num_rows =3
num_cells = worksheet.ncols - 1
curr_row = start
fs=open("sentiment.txt","w")
fo=open("featurelist.txt","w")

d2_dict = defaultdict(dict)
while curr_row <= num_rows:          
    row = worksheet.row(curr_row)
    cell_value = worksheet.cell_value(curr_row, 1)
    sentiment=worksheet.cell_value(curr_row, 4)
    if d2_dict.has_key(cell_value) and d2_dict[cell_value].has_key(sentiment): 
        d2_dict[cell_value][sentiment]+=1
    else:
        d2_dict[cell_value][sentiment]=1
    curr_row+=1
print d2_dict