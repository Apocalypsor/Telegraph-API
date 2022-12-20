from fastapi import FastAPI, Request
from pydantic import BaseModel

from telegraph import generateTelegraph

app = FastAPI()


class Req(BaseModel):
    access_token: str
    title: str
    author: str
    content: str


@app.post("/")
async def process(req: Request):
    req = await req.json()

    tg_url = generateTelegraph(
        req['access_token'], req['title'], req['author'], req['content'].strip().strip('\n')
    )
    if tg_url:
        return {
            "success": True,
            "url": tg_url,
        }
    else:
        return {
            "success": False,
            "message": "Cannot generate Telegraph."
        }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )