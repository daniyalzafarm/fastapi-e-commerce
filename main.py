from fastapi import FastAPI
from core.config import env

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to E-commerce API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=env.host, port=env.port)