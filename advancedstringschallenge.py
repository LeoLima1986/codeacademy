letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  common_word = []
  for w in word:
     if w in letters and w not in common_word:
       common_word.append(w)
  return len(common_word)

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
print(unique_english_letters("AAaBBbbCCcc"))
# should print 6

# Write your count_char_x function here:
def count_char_x(word,x):
  count = 0
  for w in word:
    if w == x:
      count += 1
  return count

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

# Uncomment these function calls to test your  function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  startindex = word.find(start)
  endindex = word.find(end)
  
  if startindex == -1 or endindex == -1:
    return word
  else:
    return word[startindex+1:endindex]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# Write your x_length_words function here:
def x_length_words(sentence,x):
  sentence_split = sentence.split()
  for word in sentence_split:
    if len(word) <  x:
      return False
    else:
      return True
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

# Write your check_for_name function here:

def check_for_name(sentence, name):
  for s in sentence.split():
    if s.lower() == name.lower():
      return True
  for i in sentence.split():
    if sentence.find(name) == -1:
      return False
# Uncomment these function calls to test your function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# Write your every_other_letter function here:
def every_other_letter(word):
  sentence = ""
  for i in range(len(word)):
    if i % 2 == 0:
      sentence += word[i]
  return sentence

   
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

# Write your reverse_string function here:
def reverse_string(word):
  return word[:-1]
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

def make_spoonerism(word1, word2):
  word1_index = word1[0]
  word2_index = word2[0]
  sentence1 = ""
  sentence2 = ""
  fullsentence = ""

  sentence1 = word2_index + word1[1::]
  sentence2 = word1_index + word2[1::]
  fullsentence = sentence1 + " " + sentence2
  return fullsentence

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# Write your add_exclamation function here:
def add_exclamation(word):
  newstring ="!"
  while len(word) < 20:
    word+= newstring
  return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
