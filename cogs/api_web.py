from discord.ext import commands
import discord
import urllib.request
from datetime import datetime
from urllib.request import urlopen
from xml.etree.ElementTree import parse

class api_web(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def covid(self,ctx):
        embed=discord.Embed(title="COVID-19 situation in Thailand", description="-----------------------------------------------------", color=0x03fc6f)
        embed.set_author(name='COVID-19', icon_url='https://hive.rochesterregional.org/-/media/health-hive/icons/covid_blue01.png')
        embed.set_image(url='https://www.vejthani.com/wp-content/uploads/2020/05/A-bad-virus-destroys-the-heart-TH.jpg')
        embed.set_thumbnail(url='https://www.unescap.org/sites/default/d8files/inline-images/COVID-19_Response.png')
        url='https://covid19.ddc.moph.go.th/api/Cases/today-cases-all'
        web=urllib.request.urlopen(url)
        data=web.read().decode()[1:-1]
        data=eval(data)
        d=["txn_date","new_case","total_case","new_death","total_death","new_recovered","total_recovered"]
        for i in d:
            if i == "txn_date": a='Date';embed.add_field(name=a, value=data[i], inline=False)
            else:
                if i== "new_case":a='New case'
                elif i=="new_death":a="New death"
                elif i=="total_death":a='Total death'
                elif i=='new_recovered':a='New recovered'
                elif i=='total_recovered':a='Total recovered'
                embed.add_field(name=a, value=data[i], inline=True)

        embed.set_footer(text='Source:https://ddc.moph.go.th/covid19-dashboard/')
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed) 

    @commands.command()
    async def nasa(self,ctx):
        url = 'https://api.nasa.gov/planetary/apod?api_key=ABReFVZPEx00AuwSie3NuvdufNyX1cb1YMcokdaE'
        web=urllib.request.urlopen(url)
        data=eval(web.read().decode())
        embed=discord.Embed(title=data['title'],
        description=data["explanation"],color=0x03fc6f)  
        embed.set_footer(text=str(ctx.author))
        embed.set_image(url=data["url"])
        embed.set_thumbnail(url=data["url"])
        embed.set_author(name='Astronomy Picture of the Day', icon_url='https://i.pinimg.com/564x/33/2f/b9/332fb9fcb939a74ed34f13c5e834a682.jpg')
        embed.set_footer(text=str(ctx.author))
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def aqi(self,ctx, arg):
        embed=discord.Embed(title="Air Pollution: Real-time Air Quality Index (AQI)", description="-----------------------------------------------------", color=0x03fc6f)
        embed.set_author(name='Air Quality Index : AQI', icon_url='https://media.istockphoto.com/vectors/air-quality-index-educational-scheme-with-excessive-quantities-of-or-vector-id1256527934?k=20&m=1256527934&s=612x612&w=0&h=WE8qA7HnNMzrJEc1lJhD49b8P71OcgqWfFMlj0Ge2pM=')
        embed.set_image(url='https://www2.iqair.com/sites/default/files/inline-images/AQI%29Chart_US.png')
        embed.set_thumbnail(url='https://thumbs.dreamstime.com/b/man-wearing-protective-medical-face-mask-cartoon-design-icon-vector-illustration-infectious-control-protection-against-190663201.jpg')
        a,b=[i for i in arg.split('/')]
        url='http://air4thai.pcd.go.th/services/getNewAQI_XML.php'
        web=urllib.request.urlopen(url)
        data=web.read().decode()
        datalist=[i for i in data.split('\n')]
        result=""
        for i in range(len(datalist)):
            if a in datalist[i] and b in datalist[i]:
                re=[datalist[i+1]]+datalist[i+6:i+10]+[datalist[i+14]]
                rec=""
                for i in range(len(re)):
                    if i==0:
                        rec+='Area: '+re[i][8:-9:] +'\n'
                        embed.add_field(name='Area', value=str(re[i][8:-9:]), inline=False)
                    elif i==1:
                        rec+='Date: '+str(re[i][15:17])+'/'+str(re[i][12:14])+'/'+str(re[i][7:11])+ '\n'
                        embed.add_field(name='Date', value=str(re[i][15:17])+'/'+str(re[i][12:14])+'/'+str(re[i][7:11]), inline=True)
                    elif i==2:
                        rec+='Time: '+re[i][7:12]+'\n'
                        embed.add_field(name='Time', value=str(re[i][7:12]), inline=True)
                    elif i==3:
                        k1=re[i].find('"')
                        k2=re[i].find('"',k1+1)
                        rec+='PM 2.5: '+ re[i][k1+1:k2] +' µg/m³\n'
                        embed.add_field(name='PM 2.5', value=str(re[i][k1+1:k2])+ ' µg/m³', inline=True)
                    elif i==4:
                        k1=re[i].find('"')
                        k2=re[i].find('"',k1+1)
                        rec+='PM 10: '+ re[i][k1+1:k2] +' µg/m³\n'
                        embed.add_field(name='PM 10', value=str(re[i][k1+1:k2])+ ' µg/m³', inline=True)
                    elif i==5:
                        k1=re[i].find('"')
                        k2=re[i].find('"',k1+1)
                        k3=re[i].find('"',k2+1)
                        k4=re[i].find('"',k3+1)
                        rec+='AQI level: '+ re[i][k1+1:k2] +' \nAQI: ' + re[i][k3+1:k4] +'\n'
                        embed.add_field(name='AQI level', value=str(re[i][k1+1:k2]), inline=True)
                        embed.add_field(name='AQI', value=str(re[i][k3+1:k4])+ ' µg/m³', inline=True)
                result+= rec+'\n'
        await ctx.send(embed=embed) 

    @commands.command()
    async def weather(self,ctx):
        var_url = urlopen('https://www.tmd.go.th/xml/region_daily_forecast.php?RegionID=7')
        xmldoc = parse(var_url)
        data=""
        for item in xmldoc.iterfind('channel/item'):
            line = item.findtext('description')
            data+=line
        idx_date=data.find('<')
        idx_detail=data.find("'>")
        idx_stop=data.find('<br',idx_detail)
        idx_icon=data.find("img src='")
        idx_icon_s=data.find("'",idx_icon+9)
        embed=discord.Embed(title='Weather',description='Get the Thailand weather forecast.\n พยากรณ์อากาศสำหรับกรุงเทพฯ และปริมณฑล',color=0x03fc6f)  
        embed.set_footer(text=str(ctx.author))
        embed.set_image(url='https://www.amazingdesignservices.co.uk/wp-content/uploads/2014/04/earth-space-hd-wallpaper-1920x1080-9805.jpg')
        embed.set_thumbnail(url='https://store-images.s-microsoft.com/image/apps.16894.c02476d2-2378-4f60-8290-b6d4b3842643.79a2ef6a-4775-4c79-8d93-9caf077660eb.1bbd88a4-0a17-4750-91a0-cd7d98f58e9d')
        embed.set_author(name='Thailand weather forecast 🌎 ', icon_url=str(data[idx_icon+9:idx_icon_s:]))
        embed.add_field(name=str(data[:idx_date:]),value=str(data[idx_detail+2:idx_stop-1:]),inline=True)
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(api_web(bot))