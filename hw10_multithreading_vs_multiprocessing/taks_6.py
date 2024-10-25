import multiprocessing
import random
import time


class Organism:
    """
    Represents an individual organism with attributes that evolve over time.
    """
    def __init__(self, id, nutrition=50, age=0, lifespan=10, reproduction_rate=0.3):
        self.id = id
        self.nutrition = nutrition
        self.age = age
        self.lifespan = lifespan
        self.reproduction_rate = reproduction_rate

    def feed(self):
        """
        Simulates feeding, where the organism gains nutrition.
        """
        food = random.randint(5, 15)
        self.nutrition += food
        print(f"Organism {self.id}: Gained {food} nutrition. Current nutrition: {self.nutrition}")

    def reproduce(self):
        """
        Simulates reproduction if nutrition is above a threshold.
        """
        if self.nutrition > 80:
            offspring = random.randint(1, 3) if random.random() < self.reproduction_rate else 0
            print(f"Organism {self.id} reproduced with {offspring} offspring.")
            return offspring
        return 0

    def age_one_cycle(self):
        """
        Ages the organism by one cycle, decreasing nutrition and increasing age.
        """
        self.nutrition -= random.randint(5, 10)
        self.age += 1
        print(f"Organism {self.id}: Aged to {self.age}. Nutrition: {self.nutrition}")

    def is_alive(self):
        """
        Checks if the organism is still alive.
        """
        return self.nutrition > 0 and self.age < self.lifespan


def simulate_organism(organism, population_queue):
    """
    Simulates an organism's lifecycle until it dies or reaches the maximum age.
    """
    while organism.is_alive():
        organism.feed()
        offspring_count = organism.reproduce()
        organism.age_one_cycle()

        # Send offspring count to the population manager
        if offspring_count > 0:
            population_queue.put(offspring_count)

        time.sleep(1)  # Simulate a time delay for each evolution cycle

    print(f"Organism {organism.id} has died.")


def manage_population(initial_population=5):
    """
    Manages the overall population of organisms, spawning new ones based on reproduction.
    """
    population_queue = multiprocessing.Queue()
    organisms = [Organism(id=i) for i in range(initial_population)]
    processes = []

    # Start processes for each initial organism
    for org in organisms:
        p = multiprocessing.Process(target=simulate_organism, args=(org, population_queue))
        p.start()
        processes.append(p)

    # Monitor the queue for new offspring
    organism_count = initial_population
    try:
        while any(p.is_alive() for p in processes):
            while not population_queue.empty():
                new_offspring = population_queue.get()
                for _ in range(new_offspring):
                    organism_count += 1
                    new_org = Organism(id=organism_count)
                    p = multiprocessing.Process(target=simulate_organism, args=(new_org, population_queue))
                    p.start()
                    processes.append(p)
    except KeyboardInterrupt:
        print("Simulation interrupted.")

    # Wait for all processes to finish
    for p in processes:
        p.join()


if __name__ == "__main__":
    manage_population(initial_population=5)
