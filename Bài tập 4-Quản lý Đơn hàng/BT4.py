class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products
        self.total_amount = 0
    def add_product(self):
        name = input("Ten sp: ")
        price = float(input("Gia: "))
        quantity = int(input("So luong: "))
        self.products.append({"Ten": name, "gia": price, "so luong": quantity})
    def calculate_total(self):
        for product in self.products:
            self.total_amount += product["gia"] * product["so luong"]
order1 = Order(1, [])
while True:
    add_more = input("Ban co muon them san pham khong? (y/n) ")
    if add_more.lower() == "n":
        break
    order1.add_product()
order1.calculate_total()
print(order1.total_amount)