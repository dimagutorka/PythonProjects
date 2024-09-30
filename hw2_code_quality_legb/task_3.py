discount = 0.1


def create_order(goods_price):
	final_price = goods_price - goods_price * discount

	def apply_additional_discount():
		nonlocal final_price
		final_price -= final_price * discount

		print(f"Your final price is {final_price}")

	return apply_additional_discount


order_creation_plus_discount = create_order(100)
order_creation_plus_discount()
