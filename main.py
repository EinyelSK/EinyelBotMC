import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO
import openai

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="GeneticsMC"))



bot.run('MTE4MTI1NjQzNDU1MDMwODk5NA.GlWg8B.X0yq5q4vzzNA13zGq0H8W3QWXu1z6RLBaIA3Mc')

