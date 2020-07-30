
# Purpose: Incredibly basic example of dictionaries

# Script 'translates' simple phrases from english to spanish by using a
# dictionary datatype.

# first we define the dictionary:
english2spanish={'Good morning.':'Buenos días.',
'Good afternoon.':'Buenas tardes.',
'Good evening. (greeting)':'Buenas noches.',
'Hello, my name is John.':'Hola, me llamo Juan.',
'What is your name?':'¿Cómo se llama usted?',
'How are you?':'¿Cómo está usted?',
'I am fine.':'Estoy bien.',
'Nice to meet you.':'Mucho gusto.',
'Goodbye.':'Adiós.',
'See you later.':'Hasta luego.',
'I am lost. Where is the restroom?':'Estoy perdido. ¿Dónde está el baño?',
'Excuse me.':'Con permiso. OR Perdóname',
'Please.':'Por favor.',
'Thank you.':'Gracías.',
'Bless you.':'Salud.',
'You are welcome (it was nothing).':'De nada.',
'How much does it cost?':'¿Cuánto cuesta?',
'How many are there?':'¿Cuántos hay?',
'There are many.':'Hay muchos.',
'Do you want to buy this?':'¿Quiere comprarlo usted?',
'What time is it?':'¿Qué hora es?',
'How do you say maybe in Spanish?':'¿Cómo se dice maybe en Español?',
'Yes.':'Sí.',
'No.':'No.',
'I do not understand.':'Yo no comprendo.',
'Would you speak slower, please.':'Por favor, habla mas despacio.',
'Who?':'¿Quièn?',
'Why?':'¿Por què?'}

# now we print the dictonary using a simple for loop:
for key in english2spanish:
    print(key)
print("\n")

# get user input:
inp = input("Enter the phrase you would like translated: ")

# translate the phrase
print("The phrase translated into Spanish is: ", end="")
print(english2spanish[inp])

# in its current form, the script has no error checking, so entering anything
# that isn't in the dictionary will result in the program crashing. A simple
# exception handler would fix this, but that's not in the script specs so I'm
# not going to include it.
