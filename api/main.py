import os
from nokia import generate_image
from sanic import Sanic
from sanic.response import raw

app = Sanic()

PRODUCTION = bool(os.environ.get("PRODUCTION"))


@app.post("/api/nokia")
async def index(request):
    text = request.json.get("text", "ZZKIA")
    return raw(generate_image(text))


app.run(host="0.0.0.0", port=3000, debug=False if PRODUCTION else True)

