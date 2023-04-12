import discord
from discord.ext import commands
import asyncio
intents = discord.Intents(messages=True, guilds=True)


import os
import requests
import json
import random
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable","happy","dull","excited","sleepy","amazing","shocked","surprised","scared","not good","not feeling well"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
        await message.channel.send('Hope you are fine!')
      
    if message.content.startswith('inspire'):
      quote = get_quote()
      await message.channel.send(quote)
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(starter_encouragements))

bot=commands.Bot(command_prefix="!",intents=intents)
@bot.command()
async def remind(ctx, h:int, msg):
  await ctx.send(f'**Your Reminder has been set and will go off in {h} hours {ctx.author.mention}**')
  await asyncio.sleep(h*60*60)
  await ctx.send(f'**{ctx.author.mention}\n Reminder to :\n{msg}**')
      
client.run(os.getenv('TOKEN'))
