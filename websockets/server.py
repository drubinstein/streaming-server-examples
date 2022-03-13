import asyncio
import json
from websockets import server


async def add_one(websocket: server.WebSocketServerProtocol):
    async for message in websocket:
        await websocket.send(json.dumps([d + 1 for d in json.loads(message)]))


async def main():
    async with server.serve(add_one, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
