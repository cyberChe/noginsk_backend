from fastapi import FastAPI

app = FastAPI()


@app.get("/noginsk")
async def root():
    return {"message": "Hello Noginsk"}