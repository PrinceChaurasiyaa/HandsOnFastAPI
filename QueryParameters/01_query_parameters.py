from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def get_user(page: int = 1, size: int = 10):
    return {
        "page": page,
        "size": size
    }



"""
Query parameters are a common way to add some dynamic parameters to a URL. You can find them 
at the end of the URL in the following form: ?param1=foo&param2=bar. In a REST API, they 
are commonly used on read endpoints to apply pagination, a filter, a sorting order, or selecting fields.
You’ll discover that they are quite straightforward to define with FastAPI. In fact, they use the exact 
same syntax as path parameters:

You simply have to declare them as arguments of your path operation function. If they don’t appear 
in the path pattern, as they do for path parameters, FastAPI automatically considers them to be query 
parameters.
"""



"""
(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> http "http://127.0.0.1:8000/users?page=5&size=50"  
HTTP/1.1 200 OK
content-length: 20
content-type: application/json
date: Sat, 04 Apr 2026 14:23:08 GMT
server: uvicorn

{
    "page": 5,
    "size": 50
}
"""