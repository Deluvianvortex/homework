
# Purpose: Basic example of python classes

# first we need to import the math functions
import math


# here is our class:
class GeoPoint:
    # this is the constructor. In the specs it said to initialize some more variables, which I didn't do. I'm pretty sure I don't even need to.
    def __init__(self):
        self.description = ""
        
    # this sets the latitude and longitute of the class' point
    def SetPoint(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
    # this outputs the point that was entered in the previous class
    def GetPoint(self):
        return [self.lat, self.lon]

    # this is pretty much exactly P6, but with lat2 and lon2 replaced by self.lat and self.lon
    def Distance(self, lat, lon):
        lat1 = math.radians(float(lat))
        lon1 = math.radians(float(lon))
        lat2 = math.radians(float(self.lat))
        lon2 = math.radians(float(self.lon))

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
        self.description = description

    # this outputs the description of the point
    def GetDescription(self):
        return self.description

# declare variables
looper = 1

point1 = GeoPoint()
point2 = GeoPoint()

# set variables
point1.SetPoint(35.106766, -106.629181)
point1.SetDescription("Albuquerque")

point2.SetPoint(39.742043, -104.991531)
point2.SetDescription("Denver")

# main loop of script
while(looper == 1):
    print("Please enter your coordinates in degrees")
    
    #plat = float(input("Enter Latitude:"))
    #plon = float(input("Enter Longitude:"))
    
    #this is the way it was before you changed the assignment
    
    plat, plon = input("Enter Latitude, Longitude:").split(",")
    
    # we have to do it this way now in case someone enters a space after the
    # comma, and since we haven't done exceptions yet, I can't prevent the
    # program from crashing if they enter the wrong number of inputs
    
    plat = float(plat)
    plon = float(plon)


    if point1.Distance(plat, plon) < point2.Distance(plat, plon):
        print("You are closest to {}, which is located at {}".format(point1.GetDescription(), point1.GetPoint()))
    if point2.Distance(plat, plon) < point1.Distance(plat, plon):
        print("You are closest to {}, which is located at {}".format(point2.GetDescription(), point2.GetPoint()))

    inp = input("Would you like to do another distance calculation (y/n)? >").lower()

    if inp != 'y': looper = 0

print("Goodbye!")
