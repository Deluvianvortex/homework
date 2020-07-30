
# Purpose: Basic example of Python modules


# imports
import GeoPoint # the 'GeoPoint.py' file must be in the root python directory

# variable declarations
point1 = GeoPoint.GeoPoint(35.106766, -106.629181, "Albuquerque")
point2 = GeoPoint.GeoPoint(39.742043, -104.991531, "Denver")

looper = 1
# main loop
while(looper == 1):
    print("Please enter your coordinates in degrees!")

    try:
        plat, plon = input("Enter Latitude, Longitude:").split(",")

    except ValueError:
        print("You have entered an incorrect number of variables.")
        break

    userPoint = GeoPoint.GeoPoint(float(plat), float(plon))

    distOne = point1.Distance(userPoint.Point)
    distTwo = point2.Distance(userPoint.Point)

    if distOne < distTwo:
        print("You are closest to {}, which is located at {}".format(point1.Description, point1.Point))
    if distTwo < distOne:
        print("You are closest to {}, which is located at {}".format(point2.Description, point2.Point))

    inp = input("Would you like to do another distance calculation (y/n)? >").lower()

    if inp != 'y': looper = 0

print("Goodbye!")
