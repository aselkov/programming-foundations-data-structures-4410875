# Linear (Sequential) Search

my_list = [8, 5, 0, 3, 9, 7]
item  = 7

def search(search_element):
  for element in my_list:
    if element == search_element:
      return True
  return False

print(search(item))

item_index = my_list.index(item)
print(item_index)