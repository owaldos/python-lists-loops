
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello=[]
for item in my_list:
    #if str(type(item)).find('dict')>0:
   # print(type(item)== dict)
   if isinstance(item, (dict,list)):
        hello.append(item)
#    if isinstance(item, list):
#         hello.append(item)    
print(hello)         
