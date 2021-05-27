import csv

with open("data1.csv" , newline = '') as f : 
    reader = csv.reader(f)
    file_Data = list(reader)

file_Data.pop(0)
new_Data = []

for i in range(len(file_Data)) : 
    number = file_Data[i][1]
    new_Data.append(float(number))

n = len(new_Data)
total = 0

for x in new_Data : 
     total = total + x

mean = total/n
print(mean)