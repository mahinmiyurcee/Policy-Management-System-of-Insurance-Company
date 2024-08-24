class Product:
    def _init_(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.status = "active"

    def update(self, name=None, description=None, price=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price
        print(f"Product {self.name} has been updated.")

    def suspend(self):
        self.status = "suspended"
        print(f"Product {self.name} has been suspended.")

    def reactivate(self):
        self.status = "active"
        print(f"Product {self.name} has been reactivated.")

    def display_details(self):
        print(f"Product ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: ${self.price}")
        print(f"Status: {self.status}")
