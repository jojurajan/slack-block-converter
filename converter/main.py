from fastapi import FastAPI, HTTPException, Request, Response
from typing import Awaitable, Callable  # , Dict, Optional, Union

from utils.headers import load_default_headers
from block_converter.converter import SlackBlockConverter
from models.blocks import SlackJsonBlocks

default_headers = load_default_headers()

app = FastAPI()

@app.post("/convert")
async def convert_blocks(sjb: SlackJsonBlocks) -> dict:
    """
    Endpoint for converting slack json blocks into Python objects
    """

    errors = ""
    output = ""
    try:
        output = SlackBlockConverter.convert(sjb.blocks)
    except Exception as exc:
        errors = str(exc)

    return {
        "output": output,
        "errors": errors
    }

@app.middleware("http")
async def add_default_headers(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """
    Middleware function that will add a list of default headers if they are not already set by any underlying function
    """
    response = await call_next(request)
    for header, value in default_headers.items():
        if header not in [key.lower() for key in response.headers.keys()]:
            response.headers[header] = value
    return response
