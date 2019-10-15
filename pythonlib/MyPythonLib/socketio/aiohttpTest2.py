from aiohttp import web
from MyPythonLib.Util import QrCodeUtil

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    #FileResponse
    #return web.Response(text=text)
    return web.Response(body=QrCodeUtil.createQrcode(text))
    

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

web.run_app(app,host="127.0.0.1")