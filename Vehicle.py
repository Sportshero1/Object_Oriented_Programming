class Vehicle:
    pass

# The objects below don't have to contain the _object in the name!
bug_object = Vehicle() # Object and instance of vehicle class
turtle_object = Vehicle() 
rover_object = Vehicle()

bug_object.color = "yellow"
bug_object.num_wheels = 4
bug_object.speed = "1 MPH"

turtle_object.color = "green"
turtle_object.num_wheels = 2
turtle_object.speed = "5 MPH"

rover_object.color = "purple"
rover_object.num_wheels = 4
rover_object.speed = "25 MPH"

print('This vehicle is ', bug_object.color, ' and is able to drive ', bug_object.speed)
print('This vehicle is can go ', turtle_object.speed, ' with ', turtle_object.num_wheels, ' number of wheels')
print('This vehicle has ', rover_object.num_wheels, ' and can go ', rover_object.speed)