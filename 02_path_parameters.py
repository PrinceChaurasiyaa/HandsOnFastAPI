from fastapi import FastAPI

app = FastAPI()

@app.get("/gravity/{type}/{id}")
async def get_gravity(type: str, id: int):
    return {"type": type, "id": id}




"""
(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> uvicorn 02_path_parameters:app
INFO:     Started server process [30900]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:54792 - "GET /gravity/prince/18 HTTP/1.1" 200 OK





(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> http http://127.0.0.1:8000/gravity/prince/18
HTTP/1.1 200 OK
content-length: 25
content-type: application/json
date: Sat, 04 Apr 2026 13:26:35 GMT
server: uvicorn

{
    "id": 18,
    "type": "prince"
}
"""