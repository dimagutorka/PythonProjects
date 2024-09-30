subscribers = []


def subscribe(sub_name):
	subscribers.append(sub_name)

	def confirm_subscription():
		print(f"The subscription for {sub_name} is confirmed ")

	confirm_subscription()


def unsubscribe(sub_name):
	if sub_name in subscribers:
		subscribers.remove(sub_name)
		print(f"{sub_name} is unsubscribed successfully ")
	else:
		print(f"{sub_name} is not found in the subscription list")


subscribe("Dima")
subscribe("Nadya")
print(subscribers)
unsubscribe("Dima")
unsubscribe("Anton")
print(subscribers)
