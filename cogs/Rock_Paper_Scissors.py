from discord.ext import commands
import random
from datetime import datetime
import discord
class rps(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def rps(self, ctx, arg):
        t=arg
        t=t.upper()
        check=['R','P','S']
        key=random.choices(check)
        result=''
        if t == 'R' and key == ['R']:result='Tie!'
        elif t=='R' and key == ['P']:result='You lose!'
        elif t=='R' and key == ['S']:result='You win!'
        elif t=='P' and key == ['R']:result='You win!'
        elif t=='P' and key == ['P']:result='Tie!'
        elif t=='P' and key == ['S']:result='You lose!'
        elif t=='S' and key == ['R']:result='You lose!'
        elif t=='S' and key == ['P']:result='You win!'
        elif t=='S' and key == ['S']:result='Tie!'
        else:await ctx.send( 'error input' );return
        if key == ['R']:key='Rock!'
        elif key == ['P']:key='Paper!'
        elif key == ['S']:key='Scissors!'
        await ctx.send( 'My choice is ' + key +'\n'+result )
        f = open('score.txt', "r")
        data={}
        for line in f:
            data=eval(line)
        f.close()
        d = open('score.txt', "w")
        if str(ctx.author) not in data :
            data[str(ctx.author)]=0
        if str(ctx.author) in data:
            if result=='You win!':
                if int(data[str(ctx.author)]) < 5 :
                    data[str(ctx.author)]=int(data[str(ctx.author)])+2
                    await ctx.send('Point + 2 !')
                elif int(data[str(ctx.author)]) < 20 :
                    data[str(ctx.author)]=int(data[str(ctx.author)])+4
                    await ctx.send('Point + 4 !')
                elif int(data[str(ctx.author)]) >= 20:
                    data[str(ctx.author)]=int(data[str(ctx.author)])+5
                    await ctx.send('Point + 5 !')

            elif result=='You lose!':
                if int(data[str(ctx.author)]) < 5 :
                    data[str(ctx.author)]=int(data[str(ctx.author)])-1
                    await ctx.send('Point - 1 !')        
                elif int(data[str(ctx.author)]) < 20 :
                    data[str(ctx.author)]=int(data[str(ctx.author)])-2
                    await ctx.send('Point - 2 !')        
                elif int(data[str(ctx.author)]) >= 20:
                    data[str(ctx.author)]=int(data[str(ctx.author)])-2
                    await ctx.send('Point - 2 !')        
                elif result=='Tie!':
                    data[str(ctx.author)]=int(data[str(ctx.author)])
                    await ctx.send('Point + 0 !')        
        d.write(str(data))
        d.close()

    @commands.command()
    async def leaderboard(self,ctx):
        embed=discord.Embed(title="Leaderboard", description="-----------------------------------------------------------", color=0x03fc6f)
        embed.set_author(name="Mafia Gunny", icon_url="https://i.pinimg.com/564x/33/2f/b9/332fb9fcb939a74ed34f13c5e834a682.jpg")
        embed.set_image(url='https://www.rocketreferrals.com/wp-content/uploads/2019/11/Leaderboard-blog.png')
        embed.set_thumbnail(url='https://static.vecteezy.com/system/resources/previews/000/691/497/original/rock-paper-scissors-neon-icons-vector.jpg')
        data=''
        f=open('score.txt','r')
        for line in f:
            data+=line
        data=eval(data)
        sort=[]
        for i in data:
          sort.append([data[i],i])
        sort=sorted(sort)[::-1]
        for i in range(len(sort)):
            embed.add_field(name=str(sort[i][1]), value=str(sort[i][0])+' Points', inline=True)
            embed.set_footer(text=str(ctx.author))
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(rps(bot))