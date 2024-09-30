default_time = 60


def training_session(num_rounds):
	time_per_round = {"default_time": 60}

	def adjust_time():
		nonlocal time_per_round

		time_list = []

		down_count = 0
		while num_rounds != down_count:
			down_count += 1
			time_list.append(int(input(f"Enter the time for round {down_count} (minutes): ")))

		time_for_each_round = {"round " + str(a): b for a, b in zip(range(1, num_rounds+1), time_list)}
		time_per_round.update(time_for_each_round)

		return time_per_round

	return adjust_time


training_time_for_each_round = training_session(5)

print(training_time_for_each_round())
