from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(name: str = "Dominick"):
    return {"message": f"Hello {name} v2"}