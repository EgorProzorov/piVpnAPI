import base64

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from mock_vpn import generate_mock_config
from schemas import ConfigResponse

app = FastAPI(title="PiVPN API")

class VPNRequest(BaseModel):
    wg_name: str
    tg_id: int

# @app.post("/create_config")
# def create_config(name: str):
#     try:
#         subprocess.run(
#             ["pivpn", "add", "-n", name, "-q"],
#             check=True
#         )
#         return {"status": "ok", "name": name}
#     except subprocess.CalledProcessError as e:
#         raise HTTPException(500, f"PiVPN error: {e}")

@app.post("/configs", response_model=ConfigResponse)
async def create_config(tg_id: int):
    return await generate_mock_config(tg_id)

@app.post("/vpn/generate")
async def generate_vpn(req: VPNRequest):
    # Для локальной разработки возвращаем фиктивный конфиг
    dummy_config = f"[Interface]\nPrivateKey = FAKEKEY_{req.tg_id}\nAddress = 10.8.0.{req.tg_id}/24\n"
    dummy_qr = base64.b64encode(dummy_config.encode()).decode()
    return {"config": dummy_config, "qr": dummy_qr}