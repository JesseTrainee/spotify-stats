import base64
from fastapi import APIRouter
import httpx
from core.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

router = APIRouter()
BASE_URL = "https://api.spotify.com/v1"

@router.get("/top-tracks")
async def get_top_tracks():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/search",
                                    headers={"Authorization": f"Basic {SPOTIFY_CLIENT_SECRET}"})
        return response.json()

@router.post("/login")
async def login(username: str, password: str):
    bytes_uft8 = f"{username}:{password}".encode("utf-8")
    base_64 = base64.b64encode(bytes_uft8).decode("utf-8")

    with httpx.AsyncClient() as client:
        response = await client.post("https://accounts.spotify.com/api/token",
                                headers={"Authorization": f"Basic {base_64}"} )
        return response.json()