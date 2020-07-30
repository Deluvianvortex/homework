
# Basic example of Python exceptions

# I wrote a simple divider program so different exceptions can be tested. There are lines you can edit in
# so that different exceptions will be thrown. In addition, you can enter words or 0's for the denominator
# and have exceptions be thrown in that manner too.

doitagain = 'y'
while doitagain != 'n':
    try:
        x = float(input("Enter the numerator:"))
        y = float(input("Enter the denominator:"))
        z = x/y
        # you'll want to edit these next lines one at a time to test the code:
        #NE = m + 3 # this will cause a NameError
        #TE = len(z) # this will cause a TypeError
    except TypeError:
        print("Wrong data type!")
    except NameError:
        print("A variable isn't being used. Edit your code.")
    except Exception as e:
        print("Something went wrong:", e)
            
    else:
        print("The result is {}".format(z))
        
        doitagain = input("Do another? (y/n):").lower()

print("Goodbye!")
