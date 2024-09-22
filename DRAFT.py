subscribers = []


def subscribe(sub_name):
	subscribers.append(sub_name)

	def confirm_subscription():
		print(f"The subscription for    {sub_name} is confirmed ")

	confirm_subscription()
