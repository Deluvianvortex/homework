
# Purpose: Basic Python File exercise
import math


# here is our class:
class GeoPoint:
    # this is the constructor.
    def __init__(self, lat=0, lon=0, description='TBD'):
        self.__lat = lat
        self.__lon = lon
        
        self.__description = description
        
    # this sets the latitude and longitute of the class' point
    def SetPoint(self, coords):
        self.__lat = coords[0]
        self.__lon = coords[1]
        
    # this outputs the point that was entered in the previous class
    def GetPoint(self):
        return [self.__lat, self.__lon]

    # this is pretty much exactly P6, but with lat2 and lon2 replaced by self.__lat and self.__lon
    def Distance(self, toPoint):
        lat1 = math.radians(float(toPoint[0]))
        lon1 = math.radians(float(toPoint[1]))
        lat2 = math.radians(float(self.__lat))
        lon2 = math.radians(float(self.__lon))

        r = 6371

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        cos1 = math.cos(lat1)
        cos2 = math.cos(lat2)

        a = (math.sin(dlat/2)**2) + math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2)**2)

        c = 2 * math.asin(math.sqrt(a))
        d = r * c

        return d

    # this sets the description of the point
    def SetDescription(self, description):
        self.__description = description

    # this outputs the description of the point
    def GetDescription(self):
        return self.__description

    # Properties
    Point = property(GetPoint, SetPoint)
    Description = property(GetDescription, SetDescription)


# I couldn't get the built-in python functions to work so I rolled my own
def findMin(x, length):
    minimum = 7918 # diameter of earth in miles
    for i in range(length):
        if x[i] < minimum: minimum = x[i]
    return minimum
    

# open the file (the file needs to be in the root python directory)
with open('cities.txt') as x:
    content = x.read().split('\n')

# declare some list and dicts:
number = len(content)
cityinfo = {}
points = []
distances = {}

# populate variables
for i in range(number):
    cityinfo[i] = content[i].split(',')
    points.append(GeoPoint(cityinfo[i][0], cityinfo[i][1], cityinfo[i][2]))


# main loop:
looper = 0
while (looper == 0):
    print("Please enter your coordinates in degrees!")

    try:
        plat, plon = input("Enter Latitude, Longitude:").split(",")

    except ValueError:
        print("You have entered an incorrect number of variables.")
        break

    userPoint = GeoPoint(float(plat), float(plon))

    for h in range(number):
        distances[h] = points[h].Distance(userPoint.Point)

    least = findMin(distances, number)

    for j in range(number):
        if points[j].Distance(userPoint.Point) == least:
            print("You are closest to {}, which is at {}".format(points[j].Description, points[j].Point))

    inp = input("Would you like to do another distance calculation (y/n)? >").lower()
    
    if inp != 'y': looper = 1

print("Goodbye!")
