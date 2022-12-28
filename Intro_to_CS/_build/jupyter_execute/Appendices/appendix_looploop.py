#!/usr/bin/env python
# coding: utf-8

# #  Appendix – What for?
# 
#  _Contributed by Audra McNamee_ 
# 
# Python offers convenient and concise ways to write loops, but 
# similarity between different patterns of `for` loops often 
# confuses students.  Using one pattern when another is 
# required often leads to `TypeError` exceptions. 
# 
# This brief walkthrough will help you distinguish between 
# 
# ```python
# for i in range(len(array)):
# ```
# 
# and 
# 
# ```python
# for i in array:
# ```
# 
# ## A list of lists 
# 
# Throughout this walkthrough, 
# assume `array = [[ item1, item2], [item3, item4], [item5, item6 ]]`. 
# We visualize this list of lists as being arranged in rows and columns:
# 
# ```python
# array =    [[item1, item2],
#             [item3, item4],
#             [item5, item6]]
# ```
# 
# We say `array` has three rows and two columns.  
# 
# ## Iteration through the items in a list
# 
# In Python, lists (and strings) are iterable objects. 
# Thus, it’s perfectly valid to write
#  
# ```python
# for row in array:
# ```
# 
# In first iteration, `row` is `[item1, item2]`.
# 
# In the second iteration, `row` is `[item3, item4]`.
# 
# In the third iteration, `row` is `[item5, item6]`.
# 
# Note that when we iterate through *elements* of a list, 
# we get the elements themselves, and not their positions. 
# 
# ## Iteration through the indices of a list
# 
# When you require an item’s position as well 
# as its value, iteration with
# 
# ```python
# for row in range(len(array)):
# ```
#  
# is appropriate.
# 
# In the first iteration, `row` is `0`.
# 
# In the second iteration, `row` is `1`.
# 
# In the third iteration, `row` is `2`.
# 
# 
# ## TypeError from mistaken identity
# 
# Type errors typically result from iterating through 
# loop elements when we need their indices, or using 
# indices as if they were elements. 
# 
# Say you intend to loop through an object by column, and write
# ```
# for col in array[0]:
# 	for row in array:
# 		print(array[row][col])
# ```
# 
# The third line, `print(array[row][col])`, 
# will produce an IndexError after the first iteration. 
# `col` is `item1` and `row` is `[item1, item2, item3]`. 
# To access `array[row][col]` we would need `row` and `col` 
# to be indices, but instead `col` is an element of 
# the list. 
#  `array[[item1, item2, item3]][item1]`
#  is a type error. 
# 
# Since we needed indices for `array[row][col]`, in 
# this case we should use `for` loops that iterate through  
# list indices: 
# 
# ```python
# for col in range(len(array[0])):
# 	for row in range(len(array)):
# 		print(array[row][col])
# ```
# 
# In the first iteration `col` is `0` and `row` is `0`. 
# `array[0][0]` is the element in row `0` and and column `0`, 
# so `item1` will be printed.
# 
# The takeaway: always know whether 
# you’re iterating by item or by index.
# 
# ## IndexError from using the wrong loop bound
# 
# Say you attempt to iterate through `array` 
# by columns with this code:
# 
# ```python
# for col in range(len(array)):
# 	for row in range(len(array)):
# 		print(array[row][col])
# ```
# 
# This code will print a few elements correctly, then crash. 
# Try to spot the error before reading on. 
# 
# ### Which bound is which
# 
# The code  above prints `item1`, ..., `item6` 
# then crashes with `IndexError`. 
# This is because `range(len(array))` 
# iterates from 0 to 2, but there is no column 2. 
# When the loop attempts 
# `print(array[0][2])` Python raises`IndexError`.
# 
# When we write loops to iterate through the indices 
# of list, we need to make sure the bounds of the 
# loop match the list we are iterating through. 
# In the case above, `col` ranges through 
# `range(len(array))`, the indexes of the rows, 
# when we need the indexes of the columns. 
# 
# Correct code to print each element  could be 
# 
# ```python
# for col in range(len(array[0])):
# 	for row in range(len(array)):
# 		print(array[row][col])
# ```
# 
# Now `len(array[0])` is the number of columns, 
# and `len(array)` is the number of rows, so 
# `array[row][col]`  will always be a valid combination 
# of row index and column index (provided each row 
# is the same length). 
# 
# ## Handle empty lists
# 
# If the length of `array` could equal 0, you must be 
# careful not to access the first column (column 0) if 
# there is no such column.  The code above starting with 
# 
# ```python
# for col in range(len(array[0])):
# ```
# will crash if `array` is `[ ]`. For this case 
# we need a _guard_: 
# 
# ```python
# if len(array) == 0: 
#    # Do the appropriate thing for the empty array
# else: 
#    for col in range(len(array[0])):    
#        ... 
# ```
# 
# Often the appropriate action will be to return
# a default value, and we can simplify this to 
# 
# ```python
# if len(array) == 0: 
#    return appropriate_value 
# for col in range(len(array[0])):  
#    ...   
# ```
# 
# ## Mnemonic loop variable names
# 
# A mnemonic is a memory aid.  One of the most 
# valuable mnemonic aids available to programmers is 
# variable names.  Naming variables well can help us 
# keep track of how we are controlling loops and 
# prevent inconsistency.  
# 
# If we loop through the *elements* of a list, we can use 
# variable names that indicate that as clearly as possible. 
# If the rows of our array were teams, and the columns were 
# members of each team, then our loops might have 
# been written 
# 
# ```python
# for team in array:
#     for member in team: 
# ```
# 
# If we loop through the *indexes* of the elements, it can 
# help to use variable names that remind us of that: 
# 
# ```python
# for team_i in range(len(array)):
#     for member_i in range(len(array[0])):
# ```
# 
# Sometimes introducing variables for both the index 
# and the element is useful in keeping the distinction clear: 
# 
# 
# ```python
# # Iteration by row
# for row_i in range(len(array)):
#     row = array[row_i]
#     for col_i in range(len(row)):
#         col = row[col_i]
#         ... 
# ```
# 
# or 
# 
# ```python
# # Iteration by column
# if len(array) == 0: 
#    # Return the appropriate value
# for col_i in range(len(array[0])):
#     for row_i in range(len(array)):
#         row = array[row_i]
#         item = row[col_i]
#         ... 
# ```
# 
# This code is slightly more verbose than code without 
# the extra variables, but the extra lines are worthwhile 
# if they make the code clearer. 
# 
# ## Poisonous variable names
# 
# At the very least we should avoid using misleading
# variable names.  Never ever ever do this: 
# 
# ```python
# for row in range(len(array[0])):
#    for col in range(len(array)):
#        print(array[col][row])
#        # BURN THIS CODE. BURY IT. WEAR GLOVES. 
# ```
# 
# ## Summary
# 
# Python gives you convenient choices in patterns 
# for `for` loops, but you need 
# to choose carefully and consistently. 
# 
# * Use `for element in array:` to loop through list elements, 
#   or `for element in range(len(array))` to loop through 
#   indices. 
#   
# * Use the right list to determine the range of indices. 
#   
# * If the *outer* loop iterates through indices of an 
#   *inner* list, you will probably need to write a 
#   special case handler for an empty *outer* list. 
#   
# * Use variable names that help you remember which
#   list is which, and whether you are iterating through 
#   list elements or list indices. 
# 
# * When we write `a[x][y]`, `x` is always the index of the 
# outer list and `y` is always the index of the inner list, 
# no matter what they are called.
