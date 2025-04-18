from aiohttp import ClientSession, ClientTimeout, ClientError
from asyncio import Semaphore, TimeoutError
from dotenv import dotenv_values
import json
import asyncio
from constants import RAINFOREST_URL


async def extract_json_for_one_asin(session: ClientSession, semaphore: Semaphore, asin: str, category: str) -> None:
    parameters = {
        "api_key": dotenv_values()["API_KEY"],
        "amazon_domain": "amazon.com",
        "asin": asin,
        "type": "product",
    }
    async with semaphore:
        async with session.get(url=RAINFOREST_URL, params=parameters) as response:
            with open(f"../data/json/{category}.json", "a") as json_file:
                res = await response.text()
                json.dump(json.loads(res), json_file, indent=4)


async def main():
    name_file = "CPU_ASINs.txt"
    category = "CPU"
    with open(f"../data/ASINs/{name_file}", 'r') as file:
        asin = file.readline().strip()

    timeout = ClientTimeout(10)
    semaphore = Semaphore(2)
    async with ClientSession(timeout=timeout) as session:
        await extract_json_for_one_asin(session=session, semaphore=semaphore, asin=asin, category=category)


if __name__ == "__main__":
    asyncio.run(main())
