
# Purpose: Intermediate example of python classes, constructors, and properties.

# first we need to import the math functions
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

# declare & set variables
looper = 1

# using constructor
point1 = GeoPoint(35.106766, -106.629181, "ABQ")

# using properties
point2 = GeoPoint()
point2.Point = 39.742043, -104.991531
point2.Description = "Denver"

# main loop of script
while(looper == 1):
    print("Please enter your coordinates in degrees")

    
    try:
        plat, plon = input("Enter Latitude, Longitude:").split(",")
    except ValueError:
        print("You entered an incorrect number of variables.")
        break
    # we have to do it this way in case someone enters a space after the comma
    
    userPoint = GeoPoint(float(plat), float(plon))

    distOne = point1.Distance(userPoint.Point)
    distTwo = point2.Distance(userPoint.Point)

    if distOne < distTwo:
        print("You are closest to {}, which is located at {}".format(point1.Description, point1.Point))
    if distTwo < distOne:
        print("You are closest to {}, which is located at {}".format(point2.Description, point2.Point))

    inp = input("Would you like to do another distance calculation (y/n)? >").lower()

    if inp != 'y': looper = 0

print("Goodbye!")
