default_time = 60


def training_session(num_rounds):
	time_per_round = default_time

	def adjust_time(new_time):
		nonlocal time_per_round
		time_per_round = new_time

	for round_num in range(1, num_rounds + 1):
		if round_num % 2 != 0:
			new_time = int(input(f"Enter the time for round {round_num} (minutes): "))
			adjust_time(new_time)

		print(f"Round {round_num}: {time_per_round} minutes")


num_rounds = int(input("Enter the number of training rounds: "))
training_session(num_rounds)