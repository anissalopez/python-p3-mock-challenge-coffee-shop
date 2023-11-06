class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3 and not hasattr(self, 'name'):
            self._name = value
        else:
            raise Exception("Error creating coffee")
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return (sum([order.price for order in self.orders()])) / len(self.orders())

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 0 < len(value) <= 15:
            self._name = value
        else:
            raise Exception("Error setting name")
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        # coffees = set([order.coffee for order in self.orders()])
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    

    @property 
    def customer(self):
        return self._customer
    
    customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise Exception("Customer must be an instance of Customer class")
    @property 
    def coffee(self):
        return self._coffee
    
    coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise Exception("Coffee must be an instance of Customer class")
        
    @property 
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not hasattr(self, 'price') and isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise Exception("Error creating price property")
    


    