from http import client
from discord.ext import commands
import discord
import datetime
class gen_commands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command()
    async def info(self,ctx):
        await ctx.send(ctx.guild)
        await ctx.send(ctx.author)


    @commands.command()
    async def password(self,ctx, arg):
        from general_commands import password 
        await ctx.send(password.passwordcheck(arg))

    @commands.command()
    async def triangle(self,ctx, arg):
        from general_commands import triangle
        await ctx.send(triangle.triangle(arg))

    @commands.command()
    async def molecule(self,ctx, arg):
        from general_commands import molecule
        await ctx.send(molecule.chem(arg))  

    @commands.command()
    async def CentralValue(self,ctx, arg):
        from general_commands import CentralValue
        await ctx.send(CentralValue.central(arg))  

    @commands.command()
    async def CrossProduct(self,ctx, arg):
        from general_commands import CrossProduct
        await ctx.send(CrossProduct.cross(arg))  

    @commands.command()
    async def word(self,ctx, arg):
        from general_commands import word
        await ctx.send(word.word(arg))
    
    @commands.command()
    async def wiki(self,ctx, arg):
        await ctx.send('https://wikipedia.org/wiki/'+arg) 


    @commands.command()
    async def horny(self,ctx):
        await ctx.send('https://tenor.com/bs7xo.gif') 
    @commands.command()
    async def rammus(self,ctx):
        await ctx.send('https://tenor.com/buBVt.gif') 


def setup(bot):
    bot.add_cog(gen_commands(bot))