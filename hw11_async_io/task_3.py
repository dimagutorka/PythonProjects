import asyncio


async def producer(queue):
	for i in range(1, 6):

		print(f"Producer: Adding task {i} to the queue")
		await queue.put(i ** i)
		await asyncio.sleep(1)
		print(f'Here the task: {i} Expression {i} ** {i} \n')


async def consumer(queue, consumer_id):
	while True:
		task = await queue.get()

		if task is None:
			print(f'There is no more tasks for you :(')
			break

		print(f'Consumer {consumer_id} executing...')
		await asyncio.sleep(2)
		print(f'Consumer {consumer_id} finished the task. The result of expression is {task}')

		queue.task_done()


async def main():
	queue = asyncio.Queue(maxsize=10)

	producer_task = asyncio.create_task(producer(queue))
	consumer_task = [asyncio.create_task(consumer(queue, i)) for i in range(1, 4)]

	await producer_task
	await queue.join()

	await queue.put(None)
	await asyncio.gather(producer_task, *consumer_task)


asyncio.run(main())
