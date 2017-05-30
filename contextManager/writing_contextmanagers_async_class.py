"""
Asyncio based calls
"""
import asyncio


class AsyncGenerator(object):

    def __init__(self):
        self.dataset = [ x for x in range(10) ]

    async def __aenter__(self):
        print("Entering the class method... data should be available in 5secs")
        await asyncio.sleep(5)
        return self.dataset

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return "Exiting the async generator..."

async def test():
    async with AsyncGenerator() as slow_stream:
        for data in slow_stream:
            print(f"processing {data}")

f = asyncio.ensure_future(test())
loop = asyncio.get_event_loop()
loop.run_until_complete(f)