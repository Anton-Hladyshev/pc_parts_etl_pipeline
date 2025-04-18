from typing import Dict

import selectolax as slx
import asyncio
import fake_useragent as fua
from aiohttp import ClientError
from asyncio import TimeoutError
from asyncio import Semaphore
from aiohttp import ClientTimeout
from aiohttp import ClientSession
from utils.controllers import is_targeted_product


#Extracting data from Amazon
async def fetch_data(url: str, parameters_url: Dict[str, str], session: ClientSession, semaphore: Semaphore, max_attempts: int = 3) -> str:
    async with semaphore:
        for attempt in range(max_attempts):
            try:
                async with session.get(url, params=parameters_url) as response:
                    if response.status == 200:
                        print(response.url)
                        response_data = await response.text()
                        return response_data
                    else:
                        print(f"Error: {response.status}")
            except ClientError as ce:
                print(f"Error: During the scrapping of page {parameters_url["page"]} something went wrong on a client side: {ce}")
            except TimeoutError:
                print("Error: Session timeout exceeded")

            await asyncio.sleep(3)

    return f"Error: connection is not esteblished after {max_attempts} retries"


#Scrapping of asins
async def extract_asin(html: str, category: str) -> None:
    if len(html) == 0:
        print("Can't extract data from an empty html")
        return

    try:
        parser = slx.parser.HTMLParser(html=html)

        goods = set()

        for node in parser.css("[data-asin]"):
            asin = node.attributes.get("data-asin")
            try:
                label = node.css_first("h2", "[aria-label]").text()
                if asin and is_targeted_product(label, category):
                    goods.add(f"{asin}: {label}")
            except AttributeError:
                pass

        with open(f"../data/ASINs/{category.replace(" ", "_")}_ASINs.txt", "a") as file:
            for el in goods:
                file.write(f"{el}\n")

    except TypeError:
        pass


async def main(category: str):
    categories = {"CPU": "cpu",
                  "Graphics card": "graphicscard",
                  "RAM": "ram"}

    url = f"https://www.amazon.com/s"
    timeout = ClientTimeout(10)
    ua = fua.UserAgent()
    headers = {
        "User-Agent": ua.safari,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive"
    }
    semaphore = Semaphore(2)

    async with ClientSession(headers=headers, timeout=timeout) as session:
        tasks = []
        for page in range(1, 5):
            parameters = {"k": categories[category], "page": page}
            tasks.append(fetch_data(url, parameters, session, semaphore))
        html_pages = await asyncio.gather(*tasks, return_exceptions=True)
    for html_page in html_pages:
        await extract_asin(html_page, category)


if __name__ == "__main__":
    asyncio.run(main("CPU"))
