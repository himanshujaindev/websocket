FROM python:3.8-slim
COPY server.py /app/server.py
RUN pip3 install websockets
# Expose the WebSocket server port
EXPOSE 8010
CMD ["python", "/app/server.py"]