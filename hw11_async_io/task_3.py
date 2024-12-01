import asyncio
from typing import Any


async def producer(queue: asyncio.Queue) -> None:
    """
    Produces tasks and adds them to the queue.

    Args:
        queue (asyncio.Queue): The queue to hold tasks.

    This function simulates a producer that generates tasks, each of which is an expression `i ** i`
    for i in the range 1 to 5. Each task is added to the queue with a brief delay to simulate work.
    """
    for i in range(1, 6):
        print(f"Producer: Adding task {i} to the queue")
        await queue.put(i ** i)  # Add the task result to the queue
        await asyncio.sleep(1)   # Simulate task creation delay
        print(f'Here the task: {i} Expression {i} ** {i} \n')


async def consumer(queue: asyncio.Queue, consumer_id: int) -> None:
    """
    Consumes tasks from the queue and processes them.

    Args:
        queue (asyncio.Queue): The queue from which tasks are fetched.
        consumer_id (int): Identifier for the consumer to differentiate output.

    This function represents a consumer that retrieves tasks from the queue, processes each task
    with a simulated delay, and marks it as done. When there are no more tasks (`None` is found),
    the consumer stops and exits the loop.
    """
    while True:
        task = await queue.get()  # Retrieve a task from the queue

        if task is None:  # Check for termination signal
            print(f'Consumer {consumer_id}: There is no more tasks for you :(')
            break

        print(f'Consumer {consumer_id} executing...')
        await asyncio.sleep(2)  # Simulate task processing delay
        print(f'Consumer {consumer_id} finished the task. The result of expression is {task}')

        queue.task_done()  # Mark task as done


async def main() -> None:
    """
    Orchestrates the producer and multiple consumers.

    This function initializes the queue, starts the producer and consumers, and manages task completion.
    After the producer finishes, it waits until all tasks are processed and then signals consumers
    to terminate by putting `None` in the queue.
    """
    queue = asyncio.Queue(maxsize=10)  # Queue with a max size of 10

    # Start the producer task
    producer_task = asyncio.create_task(producer(queue))
    # Start multiple consumers, each with a unique ID
    consumer_task = [asyncio.create_task(consumer(queue, i)) for i in range(1, 4)]

    # Wait until the producer finishes producing tasks
    await producer_task
    await queue.join()  # Wait for all tasks in the queue to be completed

    # Signal consumers to stop by adding `None` to the queue for each consumer
    for _ in consumer_task:
        await queue.put(None)

    # Wait for all consumers to finish
    await asyncio.gather(*consumer_task)


# Run the main asynchronous function
asyncio.run(main())
