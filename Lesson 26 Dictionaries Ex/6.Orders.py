line = input()
products = {}
prices = {}

while line != "buy":
   args = line.split()
   product = args[0]
   price = float(args[1])
   quantity = int(args[2])

   if product not in products:
      products[product] = {"product_price": price, "product_quantity": quantity}
   else:
      products[product]["product_quantity"] += quantity
      products[product]["product_price"] = price

   line = input()

for product, data in products.items():
    total_price = data["product_price"] * data["product_quantity"]
    print(f"{product} -> {total_price:.2f}")