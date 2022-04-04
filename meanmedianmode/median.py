import csv

with open("height_weight.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(n_num)

n = len(new_data)
new_data.sort()

if n % 2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2])
    median3 = float(median1 + median2)/2
else:

    median3 = new_data[n//2]

print("Median is: " +str(median3))











