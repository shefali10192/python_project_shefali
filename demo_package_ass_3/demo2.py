class Person:
    tax = 30

    def __init__(self, shirt_price= None, shirt_quantity=None):
        self.shirt_price = shirt_price #non Static Variable
        self.shirt_quantity = shirt_quantity

    def get_total_price(self):
        tax =
        total_price = (self.shirt_price * self.shirt_quantity * Person.tax)/100
        return "Total Cost with tax is:" + str(total_price)