from discord.ext import commands
import discord
from datetime import datetime
class help_commands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command()
    async def h(self,ctx):
        embed=discord.Embed(title="Command", description="--------------------------------------------------------------------------------------------", color=0x03fc6f)
        embed.set_author(name="Ｍａｆｉａ Ｇｕｎｎｙ", icon_url="https://i.pinimg.com/564x/33/2f/b9/332fb9fcb939a74ed34f13c5e834a682.jpg")
        embed.add_field(name="📙$info", value="Check this discord server and your username.", inline=True)
        embed.add_field(name="🔑$password <password>", value="Check the strength of your password.", inline=True)
        embed.add_field(name="🔺$triangle <number>", value="Create a beautiful triangle.", inline=True)
        embed.add_field(name="⚛️$molecule <molecule>", value="Get the details of the molecule.", inline=True)
        embed.add_field(name="📓$CentralValue <data>", value="Calculate max, min, sum, mean, and sort of data.", inline=True)
        embed.add_field(name=":x:$CrossProduct <vector>", value="Calculate the cross product.", inline=True)
        embed.add_field(name="🆒$word <text>", value="Display letter of the word in Pattern.", inline=True)
        embed.add_field(name="🏭$aqi <district/province>", value="Detail about Real-time Air Quality Index", inline=True)
        embed.add_field(name="🆘$emergency", value="Information about emergency.", inline=True)
        embed.add_field(name="🐮$horny", value="Show NSFW gif", inline=True)
        embed.add_field(name="🐢$rammus ", value="Show RAMMUS", inline=True)
        embed.add_field(name="🦠$covid", value="Information about Covid-19 today.", inline=True)
        embed.add_field(name="🎮$rps <r, p, s>", value="Rock Paper Scissors with Mafia Gunny", inline=True)
        embed.add_field(name="🖼$leaderboard", value="Display scores !", inline=True)
        embed.add_field(name="🌌$nasa", value="Astronomy Picture of the Day by NASA.", inline=True)
        embed.add_field(name="📚$wiki <search>", value="Wikipedia.", inline=True)
        embed.add_field(name="🌎$weather", value="Thailand weather forecast.", inline=True)
        embed.add_field(name="💕$join", value="Join the voice channel.", inline=True)
        embed.add_field(name="💕$leave", value="leave the voice channel.", inline=True)
        embed.add_field(name="🎵$mh", value="Music commands", inline=True)
        embed.set_footer(text=str(ctx.author))
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command()
    async def emergency(self,ctx):
        await ctx.send('```css\n[เบอร์โทรฉุกเฉินเกี่ยวกับโควิด-19]\n\
        #1668 กรมการแพทย์ ช่วยเหลือผู้ติดเชื้อแต่ไม่มีเตียงรักษาและรับคำแนะนำการปฏิบัติตัว\n\
        #1330 สำนักงานหลักประกันสุขภาพ (สปสช.) ช่วยหาเตียงให้ผู้ป่วย และรับคำแนะนำการปฏิบัติตัว หรือตรวจสอบสิทธิการรักษาพยาบาลบัตรทอง และประกันสังคม\n\
        #1323 สายด่วนสุขภาพจิต ขอคำแนะนำเมื่อเกิดภาวะเครียด\n\
        #1111 ศูนย์บริการข้อมูลสอบถามติดตามสถานการณ์โควิด-19 และขอคำแนะนำหรือร้องเรียนในช่วงวิกฤติโควิด-19\n\
        #1422 กรมควบคุมโรค สอบถามสถานการณ์ของการระบาดโควิด-19\n\
        #1506 สำนักงานประกันสังคม (สปส.) ตรวจสอบสิทธิประกันสังคม และขอรับเงินชดเชยการว่างงานช่วงโควิด-19\n\
        #1556 สำนักงานคณะกรรมการอาหารและยา (อย.) หากพบผู้ประกอบการจำหน่ายเจลล้างมือ สบู่ล้างมือ หรือหน้ากากอนามัยที่ไม่ได้คุณภาพ\n\
        #1569 กรมการค้าภายใน เมื่อไม่ได้รับความเป็นธรรมจากการสินค้า และบริการในช่วงโควิด-19```')
        await ctx.send('```css\n[เบอร์โทรฉุกเฉินด้านการแพทย์]\n\
        #1196 เมื่อพบเจออุบัติเหตุทางน้ำ\n\
        #1554 หน่วยแพทย์กู้ชีวิต วชิรพยาบาล\n\
        #1669 สถาบันการแพทย์ฉุกเฉินแห่งชาติ (ทั่วไทย) เมื่อเจอเหตุด่วนเหตุร้ายหรือผู้ได้รับบาดเจ็บ\n\
        #1691 โรงพยาบาลตำรวจ\n```')
        await ctx.send('```css\n[เบอร์ฉุกเฉินเหตุด่วนเหตุร้าย]\n\
        #191 ติดต่อแจ้งเหตุเจ้าหน้าที่ตำรวจ\n\
        #192 ภัยพิบัติแห่งชาติ\n\
        #199 ศูนย์วิทยุพระราม เพื่อแจ้งอัคคีภัย/สัตว์ร้ายบุกรุกบ้าน\n\
        #1418 มูลนิธิปอเต๊กตึ๊ง กทม.\n\
        #1155 ตำรวจท่องเที่ยว (สายด่วนเหตุร้ายที่เกี่ยวข้องกับนักท่องเที่ยว)\n\
        #1192 ศูนย์ปราบขโมยรถ (สตช.)\n\
        #1193 ตำรวจทางหลวง\n\
        #1195 กองปราบ (สายด่วนแจ้งเหตุอาชญากรรม คดีร้ายแรงเป็นภัยต่อประเทศ)\n\
        #1555 ศูนย์ร้องทุกข์กรุงเทพฯ (หน่วยประสานงานกลางเหตุฉุกเฉินในกรุงเทพฯ)\n\
        #1300 ศูนย์ประชาบดี เพื่อแจ้งบุคคลสูญหาย ```')
        await ctx.send('```css\n[เบอร์โทรฉุกเฉินเกี่ยวกับการเดินทาง]\n\
        #1137 วิทยุ จส. 100 (เบอร์โทรฉุกเฉินแจ้งเหตุด่วนบนท้องเพื่อประสานงานต่อ)\n\
        #1146 กรมทางหลวงชนบท (ติดต่อเรื่องท้องถนนเฉพาะพื้นที่ต่างจังหวัด)\n\
        #1197 ศูนย์ควบคุมและสั่งการจราจรตำรวจ\n\
        #1644 สวพ. FM91 (รายงานสภาพจราจรและแจ้งเหตุด่วนบนท้องถนน)\n\
        #1356 ศูนย์ปลอดภัยคมนาคม (ศูนย์ประสานภารกิจด้านความปลอดภัยระบบการขนส่ง)\n\
        #1690 การรถไฟแห่งประเทศไทย (สอบถามสายรถไฟ ตั๋ว และอื่น ๆ )\n\
        #1584 กรมการขนส่งทางบก\n\
        #1586 สายด่วนกรมทางหลวง\n\
        #1543 การทางพิเศษแห่งประเทศไทย\n\
        #1677 วิทยุร่วมด้วยช่วยกัน (เครือข่ายอาสาสมัคร)\n\
        #1490 บริษัท ขนส่ง จำกัด (บขส.)```')

def setup(bot):
    bot.add_cog(help_commands(bot))