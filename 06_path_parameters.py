from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path(...,  regex=r"^\w{2}-\d{3}-\w{2}$")):
    return {
        "license": license
    }





"""
Parameter metadata
Data validation is not the only option accepted by the parameter function. You can also set 
options that will add information about the parameter in the automatic documentation, such 
as title, description, and deprecated
"""

"""
(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> http http://127.0.0.1:8000/license-plates/AB-123-CD
HTTP/1.1 200 OK
content-length: 23
content-type: application/json
date: Sat, 04 Apr 2026 14:13:21 GMT
server: uvicorn

{
    "license": "AB-123-CD"
}


"""