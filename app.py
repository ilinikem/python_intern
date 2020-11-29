import urllib
import aiohttp
import uvicorn
from fastapi import FastAPI
from urllib.parse import urlparse, urlsplit

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Semrush!"}


@app.get('/healthz')
async def is_alive_host(hostname):
    try:
        async with aiohttp.ClientSession() as session:
            o = urlparse(hostname)
            if not o.scheme:
                hostname = urllib.parse.urlunsplit(('http', hostname, '', '', ''))
            async with session.get(hostname) as resp:
                return {'status': 'up' if 100 <= resp.status < 400 else 'down'}
    except aiohttp.ClientError:
        return {"key": "invalid_url!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
