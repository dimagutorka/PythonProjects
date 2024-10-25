from aiohttp import web
import asyncio
from typing import Any

# Define route table to hold the application's routes
routes = web.RouteTableDef()


@routes.get('/')
async def hello1(request: web.Request) -> web.Response:
	"""
	Handles GET requests to the root URL ('/').

	Args:
		request (web.Request): The HTTP request object.

	Returns:
		web.Response: A response object with a greeting message.

	This route returns a simple "Hello, world!" text response.
	"""
	return web.Response(text="Hello, world!")


@routes.get('/show')
async def hello2(request: web.Request) -> web.Response:
	"""
	Handles GET requests to the '/show' URL.

	Args:
		request (web.Request): The HTTP request object.

	Returns:
		web.Response: A response object indicating task completion.

	This route simulates a slow operation by adding a 5-second delay
	before returning a response with the message "Operation completed".
	"""
	await asyncio.sleep(5)  # Simulate a delay in processing
	return web.Response(text="Operation completed")


# Create and configure the web application
app = web.Application()
app.add_routes(routes)  # Add routes to the application

# Entry point to run the application
if __name__ == '__main__':
	web.run_app(app, host='127.0.0.1', port=8080)
