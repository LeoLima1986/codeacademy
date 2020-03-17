print("Code Academy - List Challenge\n")
def append_sum(lst):
  i = 0
  while i < 3:
    s = lst[-1]+lst[-2]
    lst.append(s)
    i+=1
  return lst 
print("Append Sum") 
print(append_sum([1, 1, 2]))

print("----------------")
def larger_list(lst1,lst2):
  l1 = len(lst1)
  l2 = len(lst2)
  if l1 > l2:
    return lst1[-1]
  elif l2 > l1:
    return lst2[-1]
  else:
    return lst1[-1]
print("Larger List")
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10,11]))

print("----------------")
def  more_than_n(lst,item,n):
    if item in lst:
      if lst.count(item) > n:
        return True
      else:
        return False
    else:
      return False
print("More Than N")
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

print("----------------")
def append_size(lst):
  l = len(lst)
  if l > 0:
    lst.append(l)
    return lst
print("Append Size")
print(append_size([23, 42, 108]))

print("----------------")
def combine_sort(lst1,lst2):
  newlist = lst1 + lst2
  newlist.sort()
  return newlist
print("Combine Sort")
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

print("----------------")
def every_three_nums(start):
  lst = []
  if start < 101:
    lst = list(range(start,101,3))
    return lst
  else:
    return lst
print("Every Three Nums")
print(every_three_nums(94))

print("----------------")
def remove_middle(lst,start,end):
  return lst[:start]+lst[end+1:]

print("Remove Midle")
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

print("----------------")
def more_frequent_item(lst,item1,item2): 
  print(lst) 
  count1 = lst.count(item1)
  count2 = lst.count(item2)
  if count1 >= count2:
    return item1
  else:
    return item2
print("More Frequent Item")
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

print("----------------")
def double_index(lst,index):
  if index >= len(lst):
    return lst
  else:
    newlist = lst[:index]
    newlist.append(lst[index]*2)
    newlist = newlist + lst[index+1:]
    return newlist
print("Double Index")
print(double_index([3, 8, -10, 12], 2))

print("----------------")
def middle_element(lst):
  if len(lst) % 2 == 1:
    mid = int(len(lst)/2)
    return lst[mid]
  else:
    mid = int(len(lst)/2)
    first_part = lst[:mid]
    second_part = lst[mid:]
    avg = (first_part[-1] + second_part[0])/2
    return avg
print(middle_element([5, 2, -10, -4, 4, 5]))
