import json


async def test_pages(test_cli):
    data = {
        "pages": [
            "google.com/",
            "https://facebook.com/",
            "https://yahoo.com/",
            "https://youtube.com",
            "spotify.com",
            "https://twitter.com"
        ]
    }
    response = await test_cli.post("/pages", data=json.dumps(data))
    assert response.status == 200
    resp_body = await response.json()
    assert len(resp_body) == 6
