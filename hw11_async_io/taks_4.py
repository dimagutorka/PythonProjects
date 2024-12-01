import asyncio


async def slow_task() -> None:
    """
    Simulates a slow asynchronous task.

    This function waits asynchronously for 2 seconds to emulate a delayed operation
    and then prints a message upon completion.
    """
    await asyncio.sleep(2)  # Simulate a delay
    print('Hi')


async def main() -> None:
    """
    Runs the slow_task function with a timeout limit.

    This function attempts to run `slow_task()` with a 5-second timeout. If the task takes
    longer than the specified timeout, it raises an asyncio.TimeoutError, which is caught and
    handled by printing a timeout message.
    """
    try:
        # Run slow_task with a 5-second timeout
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        # Handle timeout if the task exceeds the given time
        print("Timed out")


# Entry point for asynchronous execution
if __name__ == '__main__':
    asyncio.run(main())
