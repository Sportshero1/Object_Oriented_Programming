class Vehicle:
    
    # Class level attribute
    type = "ground"
    propulsion = "battery"


    def __init__(self, name, color, num_wheels, speed):
        self.name = name
        self.color = color
        self.num_wheels = num_wheels
        self.speed = speed
        self.type = "ground"

    def print_details(self):
        print('The', self.name, 'is', self.color, 'and is able to drive', self.speed, 'with', self.num_wheels, 'wheels')

    def paint_vehicle(self, new_color):
        self.color = new_color

