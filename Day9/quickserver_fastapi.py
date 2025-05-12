from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import create_engine, text
import os
import uvicorn

app = FastAPI()

SCHEMA = ["name", "age"]

DATABASE = os.path.join(os.getcwd(), "people.db")
engine = create_engine(f"sqlite:///{DATABASE}")

def initialize_db():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS people (
                name TEXT PRIMARY KEY,
                age INTEGER
            )
        """))
        conn.commit()

initialize_db() 

@app.get("/", response_class=HTMLResponse)
async def index():
    return """<html><head>
    <title>My webserver</title>
    <style>
    .some { color: red; }
    </style></head>
    <body>
        <h1 id="some" class="some">Hello!!!</h1>
        <h1 id="some1" class="some">Hello Again!!!</h1>
    </body>
    </html>"""

@app.get("/env", response_class=HTMLResponse)
@app.post("/env", response_class=HTMLResponse)
async def env(request: Request, envp: str = Form("ALL")):
    envp = envp.upper()
    env_dict = os.environ
    if envp in env_dict:
        env_dict = {envp: env_dict.get(envp)}
    return HTMLResponse(f"""
    <html><head><title>Give Env</title></head>
    <body>
        <form action="/env" method="post">
        Given Env var:
        <input type="text" name="envp" value="ALL"  />
        <br/>
        <input type="submit" value="Submit" />
        </form>
    </body>
    </html>""")

def get_age(name: str):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT age FROM people WHERE name = :name"), {"name": name}).fetchone()
        if result:
            return result[0]
        return None 

@app.get("/helloj/{name}/{format}")
@app.get("/helloj")
@app.post("/helloj")
async def helloj(name: str = "abc", format: str = "json", request: Request = None):
    if request.method == "POST":
        body = await request.json()
        name = body.get("name", name)
        format = body.get("format", format)

    age = get_age(name)

    if age is not None:
        return JSONResponse(content={"name": name, "age": age}, status_code=200)
    else:
        return JSONResponse(content={"name": name, "details": "Not found"}, status_code=404)  

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)