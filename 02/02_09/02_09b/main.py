def find_second_smallest(my_list):
  if len(my_list) < 2:
    return None
  my_set = sorted(set(my_list))
  return my_set[1]

print(find_second_smallest([5, 8, 3, 2, 6]))
