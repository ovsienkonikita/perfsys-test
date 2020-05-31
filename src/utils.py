import asyncio
import time
from http import HTTPStatus

import aiohttp


async def load_pages(urls: list):
    results = await asyncio.gather(*(load_one_page(url) for url in urls))
    return dict(zip(urls, results))


async def load_one_page(url):
    start_time = time.time()
    try:
        status = await make_request(url)
    except asyncio.exceptions.TimeoutError:
        status = False
        load_time = None
    else:
        load_time = time.time() - start_time

    return {"url": url, "status": "ok" if status else "failure", "load_time": load_time}


async def make_request(url):
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
        async with session.get(url) as resp:
            return resp.status == HTTPStatus.OK
