from typing import Annotated
from fastapi import APIRouter, HTTPException,  Header
import base64
import httpx
from pydantic import BaseModel
from core.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from model.login import LoginRequest

router = APIRouter()
BASE_URL = "https://api.spotify.com/v1"

@router.get("/top-tracks")
async def get_top_tracks():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/search",
                                    headers={"Authorization": f"Basic {SPOTIFY_CLIENT_SECRET}"})
        return response.json()

@router.post("/login")
async def login(data: LoginRequest):
    # Encode client_id e client_secret em Base64 como requer o Spotify
    bytes_utf8 = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode("utf-8")
    base_64 = base64.b64encode(bytes_utf8).decode("utf-8")

    headers = {
        "Authorization": f"Basic {base_64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    body = {
        "grant_type": "client_credentials",
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://accounts.spotify.com/api/token",
            headers=headers,
            data=body
        )

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    try:
        return response.json()
    except ValueError:
        raise HTTPException(status_code=500, detail="Resposta inválida do Spotify, não é um JSON válido.")

class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []

@router.get("/search/")
async def search(Authorization: Annotated[str | None, Header()], artist: str):
    headers = {
        "Authorization": f"{Authorization}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
