FROM python:3.8-slim-buster
COPY ping.py /app/ping.py
RUN pip3 install Flask
EXPOSE 5000
CMD ["python", "/app/ping.py"]