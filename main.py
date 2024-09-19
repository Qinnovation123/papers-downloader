from asyncio import run

from impl.search import search
from impl.task import articles


async def main():
    for i in articles:
        print(await search(i))


run(main())
