from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path(..., min_length=9, max_length=9)):
    return {
        "license": license
    }




"""
(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> http http://127.0.0.1:8000/license-plates/AB-123-CD
HTTP/1.1 200 OK
content-length: 23
content-type: application/json
date: Sat, 04 Apr 2026 14:07:04 GMT
server: uvicorn

{
    "license": "AB-123-CD"
}
"""