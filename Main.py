from typing import List
def merge_sort(data):
    size = len(data)//2
    for i in range(len(data)):
        index = i
        for j in range(i+1,size):
            if data[j]<data[index]:
                index = j
        data[index],data[i] = data[i],data[index]
    print(data)


input_data = input()
data = []
for item in input_data.split(', '):
    if item.isnumeric():
        data.append(int(item))
    elif item.lstrip("-").isnumeric():
        data.append(int(item))
merge_sort(data)
