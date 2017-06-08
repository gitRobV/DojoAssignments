class Car(object):
    """docstring for Car."""
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

        self.display_all()

    def display_all(self):
        print "****************"
        print "Price: " + str(self.price)
        print "Speed: " + self.speed
        print "Fuel: " + self.fuel
        print "Mileage: " + self.mileage
        print "Tax: " + str(self.tax)
        print "****************"
        print " "


new_car1 = Car(2000, '35mph', 'Full', '15mpg')
new_car2 = Car(2000, '35mph', 'Full', '15mpg')
new_car3 = Car(2000, '35mph', 'Full', '15mpg')
new_car4 = Car(2000, '35mph', 'Full', '15mpg')
new_car5 = Car(2000, '35mph', 'Full', '15mpg')
new_car6 = Car(2000, '35mph', 'Full', '15mpg')
