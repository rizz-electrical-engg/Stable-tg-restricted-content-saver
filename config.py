# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21857983"))
API_HASH = getenv("API_HASH", "e469e84c943ce3b8b056eb6a296f2c67")
BOT_TOKEN = getenv("BOT_TOKEN", "7267580651:AAF_GwQ6_N8SNF3igIOLkiGHg3Yyn3JiSi8")
OWNER_ID = list(map(int, getenv("OWNER_ID", "833465134").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://dhimanrajat:Y8IAGI0lVrMhjvkU@cluster0.mytkgu6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002164681451")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002221310765"))
