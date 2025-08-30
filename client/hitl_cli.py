import websockets, asyncio, json, uuid

async def main():
    session_id = input("Session ID: ")
    async with websockets.connect(f"ws://localhost:8000/connect?session_id={session_id}") as ws:
        while True:
            data = await ws.recv()
            msg = json.loads(data)
            if msg["type"] == "clarification":
                print("SERVER:", msg["prompt"])
                answer = input("YOU: ")
                await ws.send(json.dumps({
                    "request_id": msg["request_id"],
                    "response_type": "clarification",
                    "payload": answer
                }))

if __name__ == "__main__":
    asyncio.run(main())
