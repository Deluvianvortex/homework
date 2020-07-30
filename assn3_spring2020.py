
# Purpose: Basic exercise to increase familiarity with string and set methods

# Script asks user for a sentence, then matches fruits in the sentence to a pre-
# defined list, printing all occurances. Script then replaces one occurance with
# the words "brussel sprouts", and prints the output to the screen.

fruits = [
'Apricot',
'Asian Pear',
'Avocado',
'Banana',
'Blackberries',
'Blueberries',
'Boysenberries',
'Cactus Pear',
'Cantaloupe',
'Cherries',
'Coconut',
'Cranberries',
'Figs',
'Gooseberries',
'Grapefruit',
'Grapes',
'Honeydew Melon',
'Kiwifruit',
'Limes',
'Longan',
'Loquat',
'Lychee',
'Madarins',
'Malanga',
'Mandarin Oranges',
'Mangos',
'Mulberries',
'Nectarines',
'Oranges',
'Papayas',
'Passion Fruit',
'Peaches',
'Pears',
'Persimmons',
'Pineapple',
'Plums',
'Pomegranate',
'Prunes',
'Quince',
'Raisins',
'Raspberries',
'Rhubarb',
'Strawberries',
'Tangelo',
'Tangerines',
'Tomato',
'Ugli Fruit',
'Watermelon'
]
# I just hardcoded the fruit instead of loading it from a file because
# this is easier


# now we get some input:
inpt = input("Enter a sentence with fruit in it:").lower().title()
# split the input string by spaces, then convert into a list
li = list(inpt.split(" "))
# convert the fruit list and the input list into sets and get the intersects
intr = list(set(li).intersection(set(fruits)))
# print the length of the intersect set, and the intersects themselves
print("I found {} fruits in your sentence!".format(len(intr)))
print("Those fruits are: ", end = "")
print(intr)
# finally, print the replaced string:
bs = inpt.replace(intr[0], "Brussel Sprouts")
print("Your sentence with some brussel sprouts: {}".format(bs))

