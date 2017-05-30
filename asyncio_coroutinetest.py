import asyncio

async def couroutine1():
    while True:
        for i in range(10):
            await asyncio.sleep(0.1)
        print('couroutine1 : {}'.format("Helllooo"))

async def couroutine2():
    for i in range(25):
        await asyncio.sleep(0.25)
        print("Coroutine2 : {}".format(i))

import logging

logging.getLogger('asyncio').setLevel(logging.DEBUG)

asyncio.ensure_future(couroutine1())
f = asyncio.ensure_future(couroutine2())

loop = asyncio.get_event_loop()
loop.run_until_complete(f)
loop.close()