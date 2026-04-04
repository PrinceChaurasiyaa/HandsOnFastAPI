from fastapi import FastAPI

app = FastAPI()

@app.get("/gravity/{id}")
async def get_graity(id: int):
    return {"id": id}



"""
To run this use:

$ uvicorn 01_path_parameters(Int):app
$ http http://127.0.0.1:8000/gravity/18
"""

"""
            OutPut:

(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> http http://127.0.0.1:8000/gravity/18
HTTP/1.1 200 OK
content-length: 9
content-type: application/json
date: Sat, 04 Apr 2026 13:10:39 GMT
server: uvicorn

{
    "id": 18
}
"""


"""
Note:
if we pass a value that’s not a valid integer

(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> http http://127.0.0.1:8000/gravity/prince
HTTP/1.1 422 Unprocessable Entity
content-length: 150
content-type: application/json
date: Sat, 04 Apr 2026 13:10:47 GMT
server: uvicorn

{
    "detail": [
        {
            "input": "prince",
            "loc": [
                "path",
                "id"
            ],
            "msg": "Input should be a valid integer, unable to parse string as an integer",
            "type": "int_parsing"
        }
    ]
}
"""