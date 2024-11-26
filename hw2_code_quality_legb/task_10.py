def create_product(name, amount, price):

	product_data = {"Name": name,
	                "Amount": amount,
	                "Price": price
	                }

	def price_change(new_price):
		product_data["Price"] = new_price

		return product_data

	return price_change


a = create_product("Name", 22, 110)
print(a(11))
