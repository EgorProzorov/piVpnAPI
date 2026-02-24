from fastapi import FastAPI, HTTPException

from mock_vpn import generate_mock_config
from schemas import ConfigResponse

app = FastAPI(title="PiVPN API")

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
