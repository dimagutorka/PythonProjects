events = [1, 2, 3]


def calendar():
	def inner(action="show", event=None):
		if action == "show":
			print(events)
		elif action == "del":
			events.remove(event)
		else:
			events.append(event)
		return events

	return inner


add_event = calendar()
del_event = calendar()
show_events = calendar()

show_events()
add_event("add", 4)
show_events()
del_event("del", 1)
show_events()
