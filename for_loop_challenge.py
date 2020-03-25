def divisible_by_ten(lst_nums):
  count = 0
  for nums in lst_nums:
    if nums % 10 == 0:
      count +=1
  return count
  
#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40])) # print 3

def add_greetings(names):
  name = []
  string1 = 'Hello, '
  for firstname in names:
    name.append(string1 + firstname)
  return name

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

def delete_starting_evens(lst):
  
  while (len(lst) > 0) and lst[0] % 2 == 0:
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15])) # print 11,12,15

def odd_indices(lst):
  newlist = []
  i = 0
  while i < len(lst):
    if i % 2 == 1:
      newlist.append(lst[i])
    i +=1
  return newlist
  
  #Uncomment the lines below when your function is done
  print(odd_indices([4, 3, 7, 10, 11, -2])) # 3,10,-2
  
  def exponents(bases,powers):
  lst = []
  for base in bases:
    for power in powers:
      basetoPower = base ** power
      lst.append(basetoPower)
  return lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

#Write your function here
def larger_sum(lst1,lst2):
  if sum(lst1) > sum(lst2):
    return lst1
  elif sum(lst2) > sum(lst1):
    return lst2
  else:
    return lst1

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#Write your function here
def over_nine_thousand(lst):
  sum_of_numbers = 0
  if not len(lst) == 0:
    for i in lst:
      sum_of_numbers += i
      if sum_of_numbers > 9000:
        break
    return sum_of_numbers
  else:
    return 0

#Uncomment the line below when your function is done
print(over_nine_thousand([400,100,900,8000,400]))

def same_values(lst1,lst2):
  newlist = []
  for index in range(len(lst1)):
    for index in range(len(lst2)):
      if lst1[index] == lst2[index]:
        newlist.append(index)
    return newlist

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

def reversed_list(lst1, lst2):
  rev_lst2 = lst2[::-1]

  if lst1 == rev_lst2:
    return True
  else:
    return False

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
