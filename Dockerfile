FROM python:3.9-bullseye
# FROM gorialis/discord.py

RUN mkdir -p /usr/src/bot

WORKDIR /usr/src/bot

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python3", "main.py"]
