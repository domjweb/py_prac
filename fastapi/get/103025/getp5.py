from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(name: str = "Domin"):
    return {"message": f"Hello {name} v5"}