from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(name: str = "Dom"):
    return {"message": f"Hello {name} v3"}