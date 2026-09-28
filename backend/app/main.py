from fastapi import FastAPI

app = FastAPI(title="SafeMap API")


@app.get("/")
def root():
    return {"message": "SafeMap API is running"}


@app.get("/api/health")
def health_check():
    return {"status": "ok"}