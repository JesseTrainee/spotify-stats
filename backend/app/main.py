from fastapi import FastAPI
from api.spotify_req import router
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API Gateway para os Charts do Spotify 🎵"}

app.include_router(router, prefix="/api")
# Ponto de entrada para rodar com uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
