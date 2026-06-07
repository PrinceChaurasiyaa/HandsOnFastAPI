from fastapi import FastAPI, Query, Body

app = FastAPI()

@app.post("/user")
async def create_user(name: str = Body(...), age: int = Body(...)):
    return {"name": name, "age": age}