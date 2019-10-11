from api.nokia import generate_image
from sanic import Sanic
from sanic.response import raw

app = Sanic()


# @app.get("/api/index/<text>")
# async def generate(request, text: str):
#     return raw(generate_image(text), content_type="image/png")


@app.post("/api/index")
async def index(request):
    text = request.json.get("text", "ZZKIA")
    return raw(generate_image(text))
