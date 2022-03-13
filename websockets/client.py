import asyncio
import json
from websockets import client


async def add_one_1(
    incoming: client.WebSocketClientProtocol, outgoing: client.WebSocketClientProtocol
):
    for i in range(10):
        await incoming.send(json.dumps([i]))
        await outgoing.send(await incoming.recv())


async def add_one_2(incoming: client.WebSocketClientProtocol):
    async for message in incoming:
        print(message)


async def main():
    async with client.connect("ws://localhost:8765") as websocket1:
        async with client.connect("ws://localhost:8765") as websocket2:
            await asyncio.gather(
                add_one_1(websocket1, websocket2), add_one_2(websocket2)
            )


if __name__ == "__main__":
    asyncio.run(main())
