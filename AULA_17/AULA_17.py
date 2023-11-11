class House:
    def __init__(self, length, color):
        self.length= length
        self.color = color
        
    def display(self):
        print(self.length, self.color)
# instancia
house = House(100, 'green')
house.display

house2 = House(200, 'red')
house2.display()
