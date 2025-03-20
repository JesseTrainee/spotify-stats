from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.spotify_req import router as get_top_tracks

app = FastAPI(title="Spotify Charts API", version="1.0")

# Configuração do CORS para permitir requisições do frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Alterar para o domínio do frontend em produção
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

# Incluindo as rotas do charts.py
app.include_router(charts_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "API Gateway para os Charts do Spotify 🎵"}

# Ponto de entrada para rodar com uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
