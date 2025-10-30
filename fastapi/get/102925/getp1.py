from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(name: str = "Dominique"):

    return {"message": f"Hello {name} v1"}