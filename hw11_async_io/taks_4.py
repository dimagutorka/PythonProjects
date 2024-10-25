import asyncio


async def slow_task():
	await asyncio.sleep(2)
	print('Hi')


async def main():
	try:
		await asyncio.wait_for(slow_task(), timeout=5)
	except asyncio.TimeoutError:
		print("Timed out")


if __name__ == '__main__':
	asyncio.run(main())