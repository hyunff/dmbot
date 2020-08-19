
import discord
import asyncio
import datetime

token = "NzI3MzQ3NDU4Mjg3MzM3NTEy.XvqhGw.kNw4z7Akvq3VIHMF-6ifiGwM1k8"
client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('두리 디자인 전용') #<- 봇 상태 구문
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'): #<- 봇 명령어
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 709224875562106910: #<-본인 디코아이디 기재 (사용할 유저등록)
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="공지") 
                        embed.add_field(name="두리 디자인에서 발송하였습니다.", value=msg, inline=True)
                        embed.set_footer(text=f"두리디자인에 있어주셔서 감사합니다! 앞으로더 발전하는 두리디자인이 되겠습니다!")
                        await i.send(embed=embed)
                except:
                    pass


client.run(token)
