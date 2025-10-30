from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(name: str = "Domi"):
    return {"message": f"Hello {name} v4"}