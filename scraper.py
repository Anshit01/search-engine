## Scraper
# Scraps text from a web page

from bs4 import BeautifulSoup as bs
from aiohttp import ClientSession
import json
import aiofiles

async def get_page(url: str, session: ClientSession):
    async with session.get(url) as response:
        return await response.text()


async def scrap(url: str, name: str, session: ClientSession):
    page = await get_page(url, session)
    soup = bs(page, 'html5lib')

    # remove all javascript and stylesheet code
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # join lines to make complete text, drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    result = {
        "name": name,
        "url": url,
        "content": text
    }
    async with aiofiles.open(f"database/{name}.json", "w") as f:
        await f.write(json.dumps(result, indent=4))
    print("Scrapped:", name)
