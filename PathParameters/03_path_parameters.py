from fastapi import FastAPI
from enum import Enum

class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"

app = FastAPI()


@app.get("/users/{type}/{id}")
async def get_user(type: UserType, id: int):
    return {
        "type": type,
        "id": id
    }


"""
            Theory:

Enum (Enumeration) is a special data type used to define a fixed set of named constants.
Instead of using random values, you use predefined choices.

Enum is a data type that represents a collection of fixed, named constant values, improving 
code readability, safety, and validation.
"""

"""
(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> uvicorn 03_path_parameters:app
INFO:     Started server process [13900]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)


(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> http http://127.0.0.1:8000/users/admin/18
HTTP/1.1 200 OK
content-length: 24
content-type: application/json
date: Sat, 04 Apr 2026 13:40:29 GMT
server: uvicorn

{
    "id": 18,
    "type": "admin"
}


(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> http http://127.0.0.1:8000/users/admins/18
HTTP/1.1 422 Unprocessable Entity
content-length: 156
content-type: application/json
date: Sat, 04 Apr 2026 13:40:38 GMT
server: uvicorn

{
    "detail": [
        {
            "ctx": {
                "expected": "'standard' or 'admin'"
            },
            "input": "admins",
            "loc": [
                "path",
                "type"
            ],
            "msg": "Input should be 'standard' or 'admin'",
            "type": "enum"
        }
    ]
}
"""