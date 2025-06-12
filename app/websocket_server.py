import asyncio
import websockets
import json
import logging

logging.basicConfig(level=logging.INFO)
clients = {}

async def register(websocket, user_id):
    clients[user_id] = websocket
    logging.info(f"User {user_id} connected.")

async def unregister(user_id):
    clients.pop(user_id, None)
    logging.info(f"User {user_id} disconnected.")

async def private_message(sender_id, receiver_id, message):
    receiver_ws = clients.get(receiver_id)
    if receiver_ws:
        payload = json.dumps({"from": sender_id, "message": message})
        await receiver_ws.send(payload)

async def handler(websocket):
    try:
        handshake = await websocket.recv()
        data = json.loads(handshake)
        user_id = data.get("user_id")
        if not user_id:
            await websocket.close()
            return

        await register(websocket, user_id)

        async for message in websocket:
            data = json.loads(message)
            receiver_id = data.get("receiver_id")
            content = data.get("message")
            if receiver_id and content:
                await private_message(user_id, receiver_id, content)
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        await unregister(user_id)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        logging.info("WebSocket server started on port 8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())