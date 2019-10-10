from nokia import generate_image
from sanic import Sanic
from sanic.response import raw

app = Sanic()


@app.get("/<text>")
async def generate(request, text: str):
    return raw(generate_image(text), content_type="image/png")


@app.get("/")
async def index(request):
    return raw(generate_image("ZZKIA"), content_type="image/png")
