import threading
import asyncio
import websockets
import time

class WebSocketClientThread(threading.Thread):
    def __init__(self, uri, name, duration):
        super().__init__(name=name)  # Set the thread name
        self.uri = uri
        self.duration = duration
        self.thread_name = name

    def run(self):
        try:
            asyncio.run(self.connect_and_listen())
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    async def connect_and_listen(self):
        try:
            async with websockets.connect(self.uri) as websocket:
                start_time = time.time()
                while time.time() - start_time < self.duration:
                    try:
                        print(f"[info] client sends: {self.thread_name}")
                        await websocket.send(self.thread_name)
                        
                        message = await websocket.recv()
                        print(f"[info] client receives: {message}")
                        
                        time.sleep(2)
                    except websockets.exceptions.ConnectionClosed as e:
                        # Handle abrupt connection closure
                        if e.code == 1000:  # 1000 indicates a normal closure
                            print("[error] connection closed gracefully.")
                        else:
                            print(f"[error] connection closed abruptly with code {e.code}: {e.reason}")
                        break
                    except Exception as e:
                        print(f"An error occurred: {str(e)}")
                
                await websocket.close()

        except websockets.exceptions.WebSocketException as e:
            # Handle WebSocket-related exceptions (e.g., connection error)
            print(f"WebSocket exception: {e}")

        except Exception as exc:
            print(f"An error occurred: {str(exc)}")

if __name__ == "__main__":
    print(f"[info] websocket client started\n---")

    NUM_OF_CLIENTS = 6
    WS_SERVER_URI = "ws://localhost:8020" # Load Balancer URI
    LOAD_DURATION_SEC = 10

    threads = []
    for name in range(NUM_OF_CLIENTS):
        t = WebSocketClientThread(uri=WS_SERVER_URI, name='t'+str(name+1), duration=LOAD_DURATION_SEC)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
