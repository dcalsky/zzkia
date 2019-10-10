from nokia import generate_image
from sanic import Sanic
from sanic.response import raw

app = Sanic()


@app.get("/<text:string>")
async def index(request, text: str):
    return raw(generate_image(text), content_type="image/png")

