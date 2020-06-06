import discord,asyncio

client=discord.Client()
check = []
admin = ['657773087571574784','707776936805400627']

@client.event
async def on_ready():
    print(f"{client.user.name}봇 준비!")
@client.event
async def on_message(message):
    if message.content.startswith("//안녕"):
        await message.channel.send("안뇽하세여!")
    if message.content.startswith("//핑"):
        if (round(client.latency*1000)) > 230:
            embed = discord.Embed(color=0x00ff00)
            embed = discord.Embed(title=":ping_pong:퐁!", description="""
            현재 디스코드 api핑: {0}ms
            상태: 매우 나쁨:no_entry:""".format(round(client.latency*1000)), color=0xff0000)
            await message.channel.send(embed=embed)
        if (round(client.latency*1000)) < 230:
            embed = discord.Embed(color=0x00ff00)
            embed = discord.Embed(title=":ping_pong:퐁!", description="""
            현재 디스코드 api핑: {0}ms
            상태: 양호:white_check_mark:""".format(round(client.latency*1000)), color=0x00ff00)
            await message.channel.send(embed=embed)
        if (round(client.latency*1000)) < 185:
            embed = discord.Embed(color=0x00ff00)
            embed = discord.Embed(title=":ping_pong:퐁!", description="""
            현재 디스코드 api핑: {0}ms
            상태: 매우 좋음:green_heart:""".format(round(client.latency*1000)), color=0x0000ff)
            await ctx.channel.send(embed=embed)
    if message.content.startswith("//ㅊㅊ") or message.content.startswith("//출첵") or message.content.startswith("계절아 ㅊㅊ") or message.content.startswith("출석체크"):
        if str(message.author.name) in check:
            await message.channel.send("이미 출석체크를 했습니다")
        else:
            check.append(message.author.name)
            embed = discord.Embed(color=0x1f8b4c)
            embed.add_field(name="출석체크 시스템", value="""
            출석체크가 정상적으로 완료되었습니다.
            """, inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/702088239502065704/718643635662356480/e2e62476320455f2.JPG")
            await message.channel.send(embed=embed)
    if message.content.startswith("//출석 리스트"):
        finalcheck = "계절봇"
        for i in check:
            finalcheck = finalcheck + ", " + (i)
        embed = discord.Embed(color=0x1f8b4c)
        embed.add_field(name="출석체크한 유저", value="""
        {}
        """.format(finalcheck), inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith("//출석초기화"):
        if str(ctx.author.id) in admin:
            check = []
            await message.channel.send("완료!")
client.run("NzE0ODM1Mjg0NzIxNjY0MDIy.Xtrk-Q.uqksJ0PnxbGmZlT-huAT23r7aak")
