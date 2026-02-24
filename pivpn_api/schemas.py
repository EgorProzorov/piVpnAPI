# app/schemas.py
from pydantic import BaseModel

class ConfigResponse(BaseModel):
    id: int
    wg_name: str
    download_url: str