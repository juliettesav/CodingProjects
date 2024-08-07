class Circle:
    def __init__(self, radius):
        self.radius = radius 
    
    #def area(self):
        #circ_area = 

    def circumference(self):
        circ_circ = 2 * 3.14 * self.radius 
        return circ_circ 

my_circ = Circle(4)
print(my_circ.circumference())