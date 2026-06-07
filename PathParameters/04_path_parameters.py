from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/gravity/{id}")
async def get_gravity(id: int = Path(..., ge=17)):
    return {
        "id": id
    }



"""
ellipses(...) are here to tell FastAPI that we don’t want 
a default value

the ... means “this parameter is required and has no default value.”
"""


"""
(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> http http://127.0.0.1:8000/gravity/18     
HTTP/1.1 200 OK
content-length: 9
content-type: application/json
date: Sat, 04 Apr 2026 13:55:58 GMT
server: uvicorn

{
    "id": 18
}


(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> http http://127.0.0.1:8000/gravity/16
HTTP/1.1 422 Unprocessable Entity
content-length: 143
content-type: application/json
date: Sat, 04 Apr 2026 13:56:09 GMT
server: uvicorn

{
    "detail": [
        {
            "ctx": {
                "ge": 17
            },
            "input": "16",
            "loc": [
                "path",
                "id"
            ],
            "msg": "Input should be greater than or equal to 17",
            "type": "greater_than_equal"
        }
    ]
}
"""