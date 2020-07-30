
# Purpose: Simple demonstration of functions





import math

looper = 0

def header():
    'this function prints a header that explains what the program is made to do'
    print("This program calculates the distance between two points")

def get_location():
    'this funtion gets the latitude and longitude'
    lat = float(input("Enter latitude:"))
    lon = float(input("Enter longitude:"))

    loc = [lat, lon]
    return loc

def distance(point1, point2):
    'this function calculates the distance between the two points on a sphere using the haversine equation'
    # first we convert our inputs to radians
    # I chose to use lists because I've been programming for decades and this is easier for me
    
    lat1 = math.radians(float(point1[0]))
    lat2 = math.radians(float(point2[0]))
    lon1 = math.radians(float(point1[1]))
    lon2 = math.radians(float(point2[1]))

    # this is the radius of the earth in km. If you change this to miles, the result will be in miles
    R = 6371

    # this is some pythagorean triangle stuff
    dlat = lat2-lat1
    dlon = lon2-lon1

    # this is the meat of the conversion. It has to be done this way because there is no sin**2 func in python
    cos1 = math.cos(lat1)
    cos2 = math.cos(lat2)

    A = (math.sin(dlat/2)**2) + math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2)**2)
   
    C = 2 * math.asin(math.sqrt(A))
    # atan2(sqrt(a), sqrt(1-a)) is the same as asin(sqrt(a))
    D = R * C
   
    return D


header()

while looper == 0:
    print("First point in degrees:")
    loc = get_location()
    print("Second point in degrees:")
    loc2 = get_location()
    dist = distance(loc, loc2)
    print("The distance between the two points is {} km".format(dist))
    inp = input("Would you like to determine another distance? (y/n):").lower()
    if inp == 'n': looper = 1
   
print("Goodbye!")
