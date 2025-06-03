from aiohttp import web
async def index(request):
    text='<h1>Awesome</h1>'
    return web.Response(text=text,content_type="text/html")

async def hello(request):
    name=request.match_info.get("name","world")
    text=f'<h1>hello, {name}</h1>'
    return web.Response(text=text,content_type="text/html")

app=web.Application()
app.add_routes([web.get('/',index),web.get('/hello/{name}',hello)])

if __name__=='__main__':
    web.run_app(app)

# asyncio是直接操作底层，基于tcp，ssl/tls的传输和安全协议
# aiohttp是基于asyncio的http框架,可以编写异步的web应用，基于应用层http协议
# 使用aiohttp可以编写异步的web应用，并使用asyncio来处理异步请求
