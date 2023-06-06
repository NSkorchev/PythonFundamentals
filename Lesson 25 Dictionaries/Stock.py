product_elements = input().split()
products = {}
searched_products = input().split()

for index in range(0, len(product_elements), 2):
    key = product_elements[index]
    value = int(product_elements[index + 1])
    products[key] = value

for searched_product in searched_products:
    if searched_product in products.keys():
        print(f"We have {products[searched_product]} of {searched_product} left")
    else:
        print(f"Sorry, we don't have {searched_product}")
