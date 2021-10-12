my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:
def average(list):
    v=0
    for num in list:
        v= v+ num
    v= v/len(list)
    
    return v
    
print(average(my_list))

