from fastapi import FastAPI, Query



app = FastAPI()

@app.get("/users")
async def get_user(page: int = Query(1, gt=0), size: int = Query(18, le=100)):
    return {
        "page": page,
        "size": size
    }



"""
We also have access to more advanced validations through the Query function. It works in the same 
way that we demonstrated in the Path parameters section
"""

"""
(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> http "http://127.0.0.1:8000/users?page=8&size=87"
HTTP/1.1 200 OK
content-length: 20
content-type: application/json
date: Sat, 04 Apr 2026 14:48:07 GMT
server: uvicorn

{
    "page": 8,
    "size": 87
}

"""