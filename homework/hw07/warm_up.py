"""
warm_up.py - 6 points
=====

Write the following 2 functions:

1. get_unique_values(values)
2. create_sentence(words)


get_unique_values
-----

1. Create a function called get_unique_values
2. The function should take one argument, a list named values
3. The function should return a new list composed of only the unique values 
   in the original list of values
4. An empty list should result in an empty list
5. Ignore the case where the function receives a value that is not a list
6. Write four assertions for the example output below

Hints:

* it may help to start with a new empty list and build from there
* how do you determine if something is a duplicate / already exists?  There
  may be operators, methods or functions that may help you

Example Output:

>>> print(get_unique_values(['foo', 'foo', 'bar', 'baz', 'bar']))
['foo', 'bar', 'baz']
>>> print(get_unique_values([1, 1, 1, 1, 1]))
[1]
>>> print(get_unique_values([]))
[]
>>> print(get_unique_values(["just me"]))
['just me']

create_sentence
-----
1. define a function called create_sentence
2. it should have one parameter, a list called words
3. it will give back a string... composed of the first three letters of all 
   of the words in the list passed in that start with the letter a 
4. in the body of the function...  create an empty string called sentence
5. loop over every element in the list passed in, words
6. if the word starts with the letter a, add the first three letters of the
   word to the string called sentence
7. return the string, sentence

Example:

>>> random_words = ['bland', 'anxious', 'beetle', 'crass', aardvark']
>>> create_sentence(random_words) # should return "anxaar"
"""
