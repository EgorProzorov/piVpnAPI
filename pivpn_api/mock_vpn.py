# app/mock_vpn.py
import random

async def generate_mock_config(tg_id: int) -> dict:
    num = random.randint(1, 9999)
    wg_name = f"{tg_id}_{num}"

    return {
        "id": num,
        "wg_name": wg_name,
        "download_url": f"https://example.com/configs/{wg_name}.conf"
    }