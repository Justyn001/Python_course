class Car():

    wheels = 4          #Taka wartość bazowa zawsze tyle będzie wynosić dla nowego obiektu

    def __init__(self, brand, model, year, colour):
        self.brand = brand.upper()
        self.model = model
        self.year = year
        self.colour = colour.capitalize()

    def drive(self):
        print("The {} is driving".format(self.model))

    def stop(self):
        print("The {} is stopped".format(self.model))