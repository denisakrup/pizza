class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} Kč"


class Pizza(Item):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        self.ingredients[ingredient] = quantity
        self.price += price_per_ingredient

    def update_price(self, price):
        self.price = price

    def __str__(self):
        ingredients_str = ", ".join([f"{ingredient}: {quantity} g" for ingredient, quantity in self.ingredients.items()])
        return f"{self.name} - {ingredients_str}. Cena: {self.price} Kč"


class Drink(Item):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def __str__(self):
        return f"{self.name} - {self.volume} ml. Cena: {self.price} Kč"


class Order:
    def __init__(self, customer_name, delivery_address, items):
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = items
        self.status = "Nová"

    def mark_delivered(self):
        self.status = "Doručeno"

    def __str__(self):
        item_list = "\n".join([str(item) for item in self.items])
        return f"Objednávka od: {self.customer_name}\nAdresa doručení: {self.delivery_address}\n\nPoložky:\n{item_list}\nStav: {self.status}"


class DeliveryPerson:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.available = True
        self.current_order = None

    def assign_order(self, order):
        if self.available:
            self.current_order = order
            order.status = "Na cestě"
            self.available = False
            return True
        else:
            return False

    def complete_delivery(self):
        if self.current_order:
            self.current_order.mark_delivered()
            self.current_order = None
            self.available = True

    def __str__(self):
        availability = "Dostupný" if self.available else "Obsazený"
        return f"{self.name}, {self.phone_number}\n Stav: {availability}"


# Testování tříd
if __name__ == "__main__":
    pizza = Pizza("Pepperoni", 250, {"šunka": 100, "sýr": 150})
    pizza.add_extra("olivy", 50, 30)
    drink = Drink("Cola", 50, 500)

    order = Order("Jan Novák", "Hlavní 5, Praha", [pizza, drink])

    delivery_person = DeliveryPerson("Karel Nový", "123 456 789")

    delivery_person.assign_order(order)
    print(delivery_person)
    print("\nDoručování...\n")
    delivery_person.complete_delivery()
    print(delivery_person)

    # Vytvoření instance pizzy a manipulace s ní
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)

# Vytvoření instance nápoje
cola = Drink("Cola", 1.5, 500)

# Vytvoření a výpis objednávky
order = Order("Jan Novák", "Pražská 123", [margarita, cola])
print(order)

# Vytvoření řidiče a přiřazení objednávky
delivery_person = DeliveryPerson("Petr Novotný", "777 888 999")
delivery_person.assign_order(order)
print(delivery_person)

# Dodání objednávky
delivery_person.complete_delivery()
print(delivery_person)

# Kontrola stavu objednávky po doručení
print(order)