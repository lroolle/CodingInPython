
import asyncio


async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)

async def yahaha():
    async for yahaha in ticker(1.1, 11.11):
        print(yahah)

