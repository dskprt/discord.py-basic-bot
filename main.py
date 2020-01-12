import discord
import json

client = discord.Client()
config = json.load(open("config.json", "r"))

@client.event
async def on_ready():
    print(f"Logged in as {client.user}!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!ping"):
        await message.channel.send("Pong!")
    
client.run(config["token"])
