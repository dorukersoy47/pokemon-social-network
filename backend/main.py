from fastapi import FastAPI

# Web App Object (title and version are optional for /docs)
app = FastAPI(title="Pokemon Relation Graph API", version="0.0.1")

# Simple root endpoint
@app.get("/")
def root():
    return {
        "ok": True,
        "service": "pokemon-type-api",
        "version": "0.0.1"
    }

# 3) Optional but useful: a tiny health check endpoint.
@app.get("/health")
def health():
    return {"status": "healthy"}