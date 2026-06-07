from fastapi import FastAPI
from enum import Enum

class UserFormat(str, Enum):
    SHORT = "short"
    FULL = "full"

app = FastAPI()

@app.get("/users")
async def get_user(format: UserFormat):
    return {
        "format": format
    }


"""
(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> http "http://127.0.0.1:8000/users?format=full"
HTTP/1.1 200 OK
content-length: 17
content-type: application/json
date: Sat, 04 Apr 2026 14:44:14 GMT
server: uvicorn

{
    "format": "full"
}
"""