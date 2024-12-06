import uvloop
import asyncio
from fastapi import FastAPI, WebSocket

# Use uvloop as the event loop policy
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = FastAPI()

# Store active websocket connections
websocket_connections = set()

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_connections.add(websocket)
    try:
        await websocket.receive_text()
        # while True:
        #     message = await websocket.receive_text()
        #     # Broadcast message to all connected clients
        #     for conn in websocket_connections:
        #         if conn != websocket:
        #             await conn.send_text(message)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        websocket_connections.remove(websocket)

@app.on_event("shutdown")
async def shutdown_event():
    # Close all websocket connections on shutdown
    for websocket in websocket_connections:
        await websocket.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
