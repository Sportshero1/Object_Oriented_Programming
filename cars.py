# import
from Vehicle import Vehicle

# The objects below don't have to contain the _object in the name!
bug_object = Vehicle("beetle", "yellow", 4, "1 MPH") # Object and instance of vehicle class
turtle_object = Vehicle("Turtle Bot", "green", 2, "5 MPH") 
rover_object = Vehicle("Rover", "purple", 4, "25 MPH")

bug_object.print_details()
turtle_object.print_details()
rover_object.print_details()

bug_object.paint_vehicle("blue")

bug_object.print_details()
