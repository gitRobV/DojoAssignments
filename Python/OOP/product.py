class Product(object):
    """docstring for ."""
    def __init__(self, item_name, price, weight, brand, cost, status = "for sale"):
        self.item_name = item_name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax_rate):
        if isinstance(tax_rate, float):
            self.price = self.price + (self.price * tax_rate)
            return self
        else:
            print "Please provide tax rate in decimal format"

    def returns(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        elif reason == "like new":
            self.status = "for sale"
            return self
        elif reason == "open box":
            self.status = "used"
            self.price = self.price - (self.price * .20)
            return self
        else:
            print "Please provide a valid reason code: ( defective, like new, open box )"
            return self

    def display_all(self):
        print "******************"
        print "Item Name: " + self.item_name
        print "Price: " + str(self.price)
        print "Weight: " + self.weight
        print "Brand: " + self.brand
        print "Cost: " + str(self.cost)
        print "Status: " + self.status
        print "******************"
        print " "
        return self


toy1 = Product("truck1", 15.99, "3kg", "Tonka", 5.50)
toy2 = Product("truck2", 14.99, "3kg", "Tonka", 4.50)
toy3 = Product("truck3", 13.99, "3kg", "Tonka", 3.50)
toy4 = Product("truck4", 12.99, "3kg", "Tonka", 2.50)

toy1.add_tax(.20).sell().display_all()
toy1.returns("defective").display_all()

toy2.add_tax(.20).sell().display_all()
toy2.returns("like new").display_all()

toy3.add_tax(.20).sell().display_all()
toy3.returns("open box").display_all()

toy4.add_tax(.20).sell().display_all()
toy4.returns("it sucks").display_all()
