# lsof -ti :8765 | xargs kill -9
# Ctrl+C -> Terminate Server
import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO)

async def echo_server(websocket, path):

    try:
        async for message in websocket:
            logging.info(f"received: {message}")
            await websocket.send(message)

    except websockets.exceptions.ConnectionClosed as e:
        if e.code == 1000:  # 1000 indicates a normal closure
            logging.info("connection closed gracefully")
        else:
            logging.info(f"connection closed abruptly")

    except Exception as e:
        logging.info(e)


if __name__ == "__main__":
    print(f"websocket server started")
    start_server = websockets.serve(echo_server, '0.0.0.0', 8010)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()