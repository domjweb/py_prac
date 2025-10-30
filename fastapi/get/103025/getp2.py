from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(name: str = "Do"):
    return {"message": f"Hello {name} v2"}