import discord
import os
from discord.ext import commands



client = commands.Bot(command_prefix='$') #กำหนด Prefix

@client.event
async def on_ready() : #เมื่อระบบพร้อมใช้งาน
  print("Gunny Started!") #แสดงผลใน 

#extensions=['cogs.Rock_Paper_Scissors','cogs.help_commands','cogs.gen_commands','cogs.api_web','cogs.music_commands']
if __name__ == '__main__':
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
#--------------------------------------------
client.run('OTM5NjMxODI3MTEzNjMxNzg0.Yf7qVQ.2g1DpGfSpZBWrLEcRgK2W8qgmYA')




