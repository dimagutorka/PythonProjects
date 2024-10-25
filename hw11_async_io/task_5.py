from aiohttp import web
import asyncio

routes = web.RouteTableDef()


@routes.get('/')
async def hello1(request):
	return web.Response(text="Hello, world!")


@routes.get('/show')
async def hello2(request):
	await asyncio.sleep(5)
	return web.Response(text="Operation completed")

app = web.Application()
app.add_routes(routes)


if __name__ == '__main__':
	web.run_app(app, host='127.0.0.1', port=8080)
