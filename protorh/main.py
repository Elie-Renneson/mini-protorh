from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to allow specific origins
    allow_methods=["*"],  # Adjust this to allow specific methods (e.g., ["GET", "POST"])
    allow_headers=["*"],  # Adjust this to allow specific headers
)


@app.get("/")
async def hello():
    return {"message": "Hello World!!!"}
