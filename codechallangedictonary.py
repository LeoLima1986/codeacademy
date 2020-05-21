#Sum Values
def sum_values(my_dictionary):
  sum = 0
  for value in my_dictionary.values():
    sum += value
  return sum
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# Sum Even Keys
def sum_even_keys(my_dictionary):
  sum_even = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      sum_even += my_dictionary[key]
  return sum_even
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# Add Ten
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# Values that are keys
def values_that_are_keys(my_dictionary):
  values_are_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      values_are_keys.append(value)
  return values_are_keys
  
#  min_value = float("-inf")
#  largest_key = " "
#  for i in my_dictionary:
#    if my_dictionary[i] > min_value:
#      min_value = my_dictionary[i]
#      largest_key = i 
#    return largest_key
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  word_lengths = {}
  for w in words:
    word_lengths[w] = len(w)   
  return word_lengths

# Write your frequency_dictionary function here:
def frequency_dictionary1(words):
  frequency_word ={}
  for w in words:
    if w in frequency_word:
      frequency_word[w] += 1
    else:
      frequency_word[w] = 1
  return frequency_word

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# Write your unique_values function here:
def unique_values(my_dictionary):
  seen_values = []
  for key, value in my_dictionary.items():
    if value in seen_values:
      continue
    else:
      seen_values.append(value)
  frequency = len(seen_values)
  return frequency
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# Write your count_first_letter function here:
def count_first_letter(names):
  first_letter = {}
  for key in names.keys():
    if key[0] in first_letter:
      first_letter[key[0]] += len(names[key])
    else:
      first_letter[key[0]] = len(names)
  return first_letter


# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
