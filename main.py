from fastapi import FastAPI

app = FastAPI(title="Smart Asset Manager")

@app.get("/")
async def root():
    return {"message": "Server is running"}