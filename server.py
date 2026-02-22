import asyncio
import json
import websockets

# A set to keep track of all active client connections.
connected_clients = set()

chat_history = []

async def chat_handler(websocket):
    """
    Handles the lifecycle of a WebSocket connection.
    """
    # Register the new client
    connected_clients.add(websocket)
    await PrintChatHistory(websocket)
    print(f"New client connected. Total clients: {len(connected_clients)}")
    
    try:
        async for message in websocket:
            # expects message to be a JSON string
            data = json.loads(message)
            
            # Broadcast the received message to all connected clients
            websockets.broadcast(connected_clients, json.dumps(data))
            chat_history.append(data) 
            
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Client disconnected: {e}")
    finally:
        # Ensure the client is removed from the set when they disconnect or close the tab
        connected_clients.remove(websocket)
        print(f"Client removed. Total clients: {len(connected_clients)}")

async def PrintChatHistory(websocket):
    """
    Sends the chat history to a newly connected client.
    """
    for message in chat_history:
        message["user"] = message["user"] + " (history)"
        await websocket.send(json.dumps(message))

async def main():
    async with websockets.serve(chat_handler, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        # Run the event loop forever
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())