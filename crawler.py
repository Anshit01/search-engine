## Crawler
# Crawls wikipedia for all the countries and scrap respective pages for content

from bs4 import BeautifulSoup as bs
import asyncio
from aiohttp import ClientSession
from scraper import scrap, get_page

main_url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area"

async def crawl(session: ClientSession):
    page_text = await get_page(main_url, session)
    soup = bs(page_text, 'html5lib')
    table = soup.find_all('table')[1]
    rows = table.find_all('tr')

    jobs = []
    for row in rows[2:]:
        cells = row.find_all('td')
        c = cells[1]
        if c.text != "Antarctica" and c.find('span', {'class': 'flagicon'}) is None:
            c = cells[0]
        name = c.text
        if '[' in name:
            name = name[:name.index('[')]
        name = name.strip()
        print("Found:", name)
        url = "https://en.wikipedia.org" + c.find('a').get('href')
        jobs.append(scrap(url, name, session))
    await asyncio.gather(*jobs)


async def main():
    async with ClientSession() as session:
        await crawl(session)

asyncio.run(main())
