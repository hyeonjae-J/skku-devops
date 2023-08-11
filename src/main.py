# pip install uvicorn
# pip install "fastapi[all]"
# uvicorn src.main:app

from fastapi import FastAPI

app = FastAPI(
    title="FastAPI - Hi World",
    description="This is the Hi World of FastAPI.",
    version="1.0.0",
)


@app.get("/")
def hello_world():
    return {"Hi": "Fucking World"}
