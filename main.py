from fastapi import FastAPI

app = FastAPI(title="NHS Digital Hospital Agent")


@app.get("/")
def home():
    return {
        "message": "NHS Digital Hospital Agent is running",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
