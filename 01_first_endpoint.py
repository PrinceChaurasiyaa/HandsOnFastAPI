from fastapi import FastAPI

app = FastAPI()   # <---- FastAPI object, app.  the main 
                  # application object that will wire all the API routes

@app.get("/")
async def hello_gravity():
    return {"hello": "Grav!ty"}


"""
            Theory:

It’s worth noting that FastAPI is built upon two main Python libraries: Starlette, a low-level 
ASGI web framework (https://www.starlette.io/), and Pydantic, a data validation 
library based on type hints (https://pydantic-docs.helpmanual.io/).

A decorator is a syntactic sugar that allows 
you to wrap a function or class with common logic without compromising readability. It’s roughly 
equivalent to app.get("/")(hello_gravity).

Note: FastAPI exposes one decorator per HTTP method to add new routes to the application. 
The one shown here adds a GET endpoint with the path as the first argument.

FastAPI exposes an Asynchronous Server Gateway Interface (ASGI)-compatible application.
ASGI (Asynchronous Server Gateway Interface) is a standard that allows Python web apps to handle:
    async requests (non-blocking)
    WebSockets
    high concurrency
Think of ASGI as a bridge between your FastAPI app and the web server
ASGI allows handling multiple requests concurrently using async/await, making applications faster and more scalable.

A web server is required to run a FastAPI application because FastAPI itself cannot directly listen to HTTP requests.
Uvicorn is a lightweight and fast ASGI web server used to run FastAPI applications.
Uvicorn receives client requests, forwards them to the FastAPI app, and sends back the response.
"""

"""
    To run this API:
    $ uvicorn 01_first_endpoint:app

    httpie:
    $ http http://127.0.0.1:8000

    Uvicorn will:
        -> Import 01_first_endpoint.py
        -> Locate app (FASTAPI object)
        -> Start a server (usually at http://127.0.0.1:8000)
        -> Listen for incoming requests (Users)
        -> Forward them to FastAPI
        -> Return responses

        User ->  Uvicorn (ASGI server) -> FastAPI (ASGI app) -> Response -> Uvicorn (ASGI server) -> User
"""

"""
            OutPut:

(venvFastAPI) PS D:\8_FASTAPI\HandsOnFastAPI> uvicorn 01_first_endpoint:app
INFO:     Started server process [20900]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
"""