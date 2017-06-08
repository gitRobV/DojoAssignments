class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self

    def ride(self):
        print "Riding..."
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing ..."
        if self.miles < 5:
            self.miles = 0
        else:
            self.miles -= 5
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(300, "50mph")
bike3 = Bike(400, "75mph")

bike1.ride().ride().ride().reverse().displayInfo()
