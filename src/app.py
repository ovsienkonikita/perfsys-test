from mangum import Mangum
from sanic import Sanic
from sanic.response import json

from .utils import load_pages

app = Sanic(__name__)

handler = Mangum(app)


@app.route("/pages", methods=["POST"])
async def pages(request):
    urls = request.json["pages"]
    result = await load_pages(urls)
    return json(result)


if __name__ == "__main__":
    app.run()
