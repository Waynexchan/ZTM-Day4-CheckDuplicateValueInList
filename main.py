# # Exercise: check for duplicates in list:
# some_list = ['a', 'b', 'c' , 'b' , 'd' , 'm' , 'n' , 'n']

# # by using for loop
# duplicate_list = []
# for item_outside in range(0 , len(some_list)):
#   for item_inside in range(item_outside + 1, len(some_list)):
#     if some_list[item_inside] == some_list[item_outside]:
#       duplicate_list.append(some_list[item_inside])
# print(duplicate_list)

# # by using set
# some_list = ['a', 'b', 'c' , 'b' , 'd' , 'm' , 'n' , 'n']
# duplicate_list = set()
# Seen_list = set()
# for item in some_list:
#   if item in Seen_list:
#     duplicate_list.add(item)
#      else:
#        Seen_list.add(item)
# print(duplicate_list)    

# by using count
some_list = ['a', 'b', 'c' , 'b' , 'd' , 'm' , 'n' , 'n']
duplicate_list = []
for item in some_list:
  if some_list.count(item) > 1:
    if item not in duplicate_list:
      duplicate_list.append(item)
print(duplicate_list)
    
  
  
  
  