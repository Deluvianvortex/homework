
# Purpose: Basic exercise to improve python skills using sequences and lists
# Made in Python 3.8.1

# Script will ask the user for a state name and return the capital, the number of congressional districts, and the place in which it joined the United States.
# Or, it will error if input is entered incorrectly.

# I used methods that we haven't been taught yet because I was trying to use the least possible number of lines in the program
# and still maintain full functionality. This attempt uses only 20 lines.

def ordinal(num):
    endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] +  7 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th']
    return str(num) + endings[num - 1]
# this is the same function from the book, but made into a method, and extended up to 50.


with open('P2StateLists.txt', 'r') as f:
    x = f.read().split('\n')
# I decided to load the source file into a list, so the file needs to be in the directory that the python executable is in.
# The entries in the file are delimited by invisible '\n' carriage returns so I split them apart that way.

print("Welcome to the state name finder information thingy.")
print("Enter a state name")
name = input(">").lower().title()
# just like in class, it's better to filter the input by making it lowercase and then using .title().

try:
    findname = '\'' + name + '\','
    loc = x.index(findname)
except ValueError:
    findname = '\'' + name + '\''
    loc = x.index(findname)
# I had to use exception handling for Wyoming, since it was the last entry on the list and as such, doesn't follow the same formatting
# as the other entries.

# since I loaded the source file as a list, each entry (other than wyoming) has single quotes around it and a comma at the end.
# In order to correctly use index() we need to add those characters to the input string
# (or edit the file so they aren't there, but that was lots more work).

loc = x.index(findname)
capitalname = x[loc+53].replace("'","").replace(",", "")
districtname = x[loc+106].replace("'","").replace(",","")
joinednum = x[loc+159].replace("'","").replace(",","")
# the file has 3 useless entries separating each different section, so after the initial state list, each additional string will be offset by
# 53, then 106, then 159, so we need to add those numbers to the index value or we will get incorrect data.
# Then, we need to remove the single quotes and commas from the resulting strings before we print the results.

o = ordinal(int(joinednum))
print("The capital of {} is {}, it has {} congressional districts, and was {} to join the union.".format(name, capitalname, districtname, o))
# finally, we can format everything into a string and print the result.
    






