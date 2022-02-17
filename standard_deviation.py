import math
import csv

with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for y in data:
        total += int(y)
    mean = total/n
    return mean

squared_list = []
for number in data:
    a = int(number)-mean
    a = a**2
    squared_list.append(a)



for i in squared_list:
    sum = sum + i


result = sum/(len(data)-1)
standard_deviation = math.sqrt(result)



print(standard_deviation)



