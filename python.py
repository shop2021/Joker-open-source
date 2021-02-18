import discord  #@@@ pip install discord
import datetime #@@@ pip install datetime
import asyncio  #@@@ pip install asyncio
from captcha.image import ImageCaptcha #@@@pip install ImageCaptcha
from itertools import cycle
import captcha
import random
import time
import urllib
import requests
import openpyxl
from discord.utils import get
from urllib.parse import quote_plus
from captcha.image import ImageCaptcha
import bs4
import json # Json 모듈
from bs4 import BeautifulSoup # Bs4 에서 불러오는 BeautifulSoup 모듈
from urllib.request import Request # Urllib 모듈 1
from urllib.request import URLError # 2
from urllib.request import HTTPError # 3
from urllib.request import urlopen # 4
from urllib.request import Request, urlopen # 5
from urllib.request import quote # 6
from urllib.request import urlopen, Request # 7
from discord.ext import commands
import youtube_dl
import string

token = 'ODA4Njc2Nzc0MzE3MTI5NzY4.YCKA7w.J96uoeNifE7r68usnGgp_LOa7oQ'
client = discord.Client() #클라이언트 설정하기

permiss = discord.Embed(color=0xFF0000)
permiss.add_field(name='❌  권한 부족', value='명령어 사용권한이 부족합니다')

@client.event
async def on_ready():
    print("JOKER")
    while True:
        await client.change_presence(status=discord.Status.online,activity=discord.Game(f'{len(client.guilds)}개의 서버에 참가'))
        await asyncio.sleep(4)

@client.event
async def on_message(message): #사용자가 메시지를 입력했을때
    if message.content == "조":
        message = await message.channel.send(embed=discord.Embed(title='커', colour=discord.Colour.green()))     
    if message.content == "SHOP":
        message = await message.channel.send(embed=discord.Embed(title='#2021', colour=discord.Colour.green()))


    if message.content.startswith('.관리자'):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                message = await message.channel.send(embed=discord.Embed(title='⛔️관리자 명령어⛔️', description='`.청소 (수)`,서버의 채팅을 청소해줍니다 ㅣ`.채널삭제`,채널을 삭제 후 재생성 함으로써 채널의 모든 채팅을 순식간에 삭제 가능합니다', colour=discord.Colour.green()))
            else:
                message = await message.channel.send(embed=discord.Embed(title='⛔️명령어 사용권한이 없습니다', colour=discord.Colour.red()))
        except:
            pass
            


    if message.author.bot: return
    if message.content == ".도움말":
        embed = discord.Embed(
            title = ":white_check_mark: DM을 확인해주세요.",
            colour = 0x2ecc71
        )
        await message.channel.send(embed=embed)
        description = """`.내정보`,`유저의 정보를 알려줍니다`
`.실검`,`네이버 실시간 검색어를 알려줍니다`
`.문상`,`랜덤으로 문상 코드를 보내줍니다.(가능성 있습니다 차라리 복권을 사는게 나을수도)`
`.니트로`,`랜덤으로 니트로 코드를 선물해 줍니다 (이것도 가능성 있음 복권뽑히는 정도의 가능성)`
`.코로나`,`실시간 코로나 확진자 및 코로나 사망자 수를 알려줍니다`
`.주사위`,`주사위 게임을 합니다`
`.한강`,`오늘의 한강 수온을 알려줍니다` 
`.위성`,`위성에서 찍은 위성사진을 보내줍니다`
`.공식서버`,`JOKER봇 공식 서버 링크를 전송합니다`
`.봇초대`,`봇을 본인의 서버에 초대합니다`
`.봇소스`,`봇 소스 관련 안내를 합니다`
`.사람인증`,`봇인지 사람인지 인증을 하는 재밌는 놀이가 될수 있는 명령어 입니다`
"""
        embed = discord.Embed(
            title = ":white_check_mark: \"JOKER\" 도움말",

            description = description,
            colour = 0x2ecc71
        )
        await message.author.send(embed=embed)
    if isinstance(message.channel, discord.channel.DMChannel):
        return
    member: discord.Member = message.author    

    if message.author.bot: return
    if message.content == ".봇초대":
        embed = discord.Embed(
            title = ":white_check_mark: DM을 확인해주세요.",
            colour = 0x2ecc71
        )
        await message.channel.send(embed=embed)
        description = """ ` 봇 초대 ` 
봇 초대 링크 : https://discord.com/api/oauth2/authorize?client_id=808676774317129768&permissions=8&scope=bot
"""
        embed = discord.Embed(
            title = ":white_check_mark: \"JOKER\" 도움말",

            description = description,
            colour = 0x2ecc71
        )
        await message.author.send(embed=embed)
    if isinstance(message.channel, discord.channel.DMChannel):
        return
    member: discord.Member = message.author         

    if message.author.bot: return
    if message.content == ".봇소스":
        embed = discord.Embed(
            title = ":white_check_mark: DM을 확인해주세요.",
            colour = 0x2ecc71
        )
        await message.channel.send(embed=embed)
        description = """ ` 봇 소스 안내 ` 
봇 소스는 공식 서버에서 Github링크로 오픈소스로 공개중입니다. https://discord.gg/seq7fQHTEc 이곳으로 접속해서 봇 오픈소스를 다운받아 보세요!
"""
        embed = discord.Embed(
            title = ":white_check_mark: \"JOKER\" 도움말",

            description = description,
            colour = 0x2ecc71
        )
        await message.author.send(embed=embed)
    if isinstance(message.channel, discord.channel.DMChannel):
        return
    member: discord.Member = message.author                          
 
    if message.content.startswith('.주사위'):
        randomNum = random.randrange(1, 7)
        if randomNum == 1:
            await message.channel.send(embed=discord.Embed(description=':one:', color=0x7C40E5))
        if randomNum == 2:
            await message.channel.send(embed=discord.Embed(description=':two:', color=0x7C40E5))
        if randomNum == 3:
            await message.channel.send(embed=discord.Embed(description=':three:', color=0x7C40E5))
        if randomNum == 4:
            await message.channel.send(embed=discord.Embed(description=':four:', color=0x7C40E5))
        if randomNum == 5:
            await message.channel.send(embed=discord.Embed(description=':five:', color=0x7C40E5))
        if randomNum == 6:
            await message.channel.send(embed=discord.Embed(description=':six: ', color=0x7C40E5))

    if message.content.startswith('.청소'):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(embed=discord.Embed(title='🧹 메시지 ' + str(amount) + '개 삭제됨', colour=discord.Colour.green()))
                await asyncio.sleep(2)
                await message.delete()
            else:
                message = await message.channel.send(embed=discord.Embed(title='⛔️명령어 사용권한이 없습니다', colour=discord.Colour.red()))
        except:
            pass

    if message.content.startswith(".내정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="`이름`", value=message.author.name, inline=True)
        embed.add_field(name="`별명`", value=message.author.display_name, inline=False)
        embed.add_field(name="`가입일`", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="`아이디`", value=message.author.id, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith('.채널삭제'):
        if message.author.guild_permissions.ban_members:
            aposition = message.channel.position
            new = await message.channel.clone()
            await message.channel.delete()
            await new.edit(position=aposition)

            embed = discord.Embed(title='⛔️채널삭제가 완료되었습니다⛔️', colour=discord.Colour.red())
            #embed.set_image(url='https://media.giphy.com/media/HhTXt43pk1I1W/giphy.gif')
            await new.send(embed=embed)
        else:
                message = await message.channel.send(embed=discord.Embed(title='⛔️명령어 사용권한이 없습니다', colour=discord.Colour.red()))

    if message.content.startswith('.실시간검색어') or message.content.startswith('.실검'):
        json = requests.get('https://www.naver.com/srchrank?frm=main').json()
        ranks = json.get("data")
        data = []
        for r in ranks:
            rank = r.get("rank")
            keyword = r.get("keyword")
            if rank > 10:
                break
            data.append(f'**{rank}**위 {keyword}')

        dat = str(data)
        dat = dat.replace("'","")
        dat = dat.replace(", ","\n")
        dat = dat[1:-1]
        print(dat)
        embed = discord.Embed(title= '네이버 실시간 검색어 순위', description=(dat),colour=0x19CE60)
        await message.channel.send(embed=embed)

    if message.content.startswith('.문상') or message.content.startswith('.문화상품권'):
        a = random.randint(2000, 4900)
        b = random.randint(1000, 9999)
        b2 = random.randint(1000, 9999)
        c = random.randint(100000,999999)
        TICKETembed = discord.Embed(title='문상 생성기', description=str(a) + '-' + str(b) + '-' + str(b2) + '-' + str(c))
        await message.channel.send(embed=TICKETembed)

    if message.content == '.니트로':
        ranNitro = ""
        for i in range(0, 16):
            ranNitro += str(random.choice(string.ascii_letters))
            NitroEmbed = discord.Embed(title='니트로 생성기', description='https://discord.gift/' + ranNitro)
        await message.channel.send(embed=NitroEmbed)

    if message.content.startswith('.코로나'):
        url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        datecr = soup.find('span', {'class': 't_date'}) #기준날짜
        #print(f'기준일: {datecr.string}')

        totalcovid = soup.select('dd.ca_value')[0].text #누적 확진자수
        #print(f'누적 확진자: {totalcovid} 명')

        todaytotalcovid = soup.select('p.inner_value')[0].text #당일 확진자수 소계
        #print(f'확진자 소계: {todaytotalcovid} 명')

        todaydomecovid = soup.select('p.inner_value')[1].text #당일 국내발생 확진자수
        #print(f'국내발생: {todaydomecovid} 명')

        todayforecovid = soup.select('p.inner_value')[2].text #당일 해외유입 확진자수
        #print(f'해외유입: {todayforecovid} 명')

        totalca = soup.select('dd.ca_value')[2].text #누적 격리해제
        #print(f'누적 격리해제: {totalca} 명')

        todayca = soup.select('span.txt_ntc')[0].text #당일 격리해제
        #print(f'격리해제: {todayca} 명')

        totalcaing = soup.select('dd.ca_value')[4].text #누적 격리중
        #print(f'누적 격리중: {totalcaing}')

        todaycaing = soup.select('span.txt_ntc')[1].text #당일 격리중
        #print(f'격리중: {todaycaing} 명')

        totaldead = soup.select('dd.ca_value')[6].text #누적 사망자
        #print(f'누적 사망자: {totaldead} 명')

        todaydead = soup.select('span.txt_ntc')[2].text #당일 사망자
        #print(f'사망자: {todaydead} 명')

        covidembed = discord.Embed(title='코로나19 국내 발생현황', description="", color=0xFF0F13, url='http://ncov.mohw.go.kr/')
        covidembed.add_field(name='🦠 확진환자', value=f'{totalcovid}({todaytotalcovid}) 명'
                                                f'\n\n국내발생: {todaydomecovid} 명\n해외유입: {todayforecovid} 명', inline=False)
        covidembed.add_field(name='😷 격리중', value=f'{totalcaing}({todaycaing}) 명', inline=False)
        covidembed.add_field(name='🆓 격리해제', value=f'{totalca}({todayca}) 명', inline=False)
        covidembed.add_field(name='💀 사망자', value=f'{totaldead}({todaydead}) 명', inline=False)
        covidembed.set_footer(text=datecr.string)
        await message.channel.send(embed=covidembed)

    if message.content.startswith('.공식서버'):
        jkembed = discord.Embed(title='공식서버 초대 링크', description="", color=0xFF0F13, url='https://discord.com/invite/seq7fQHTEc')
        jkembed.add_field(name='JOKER 봇 공식서버', value='JOKER 봇 공식 커뮤니티 서버 주소입니다. 업데이트 및 공지사항 확인을 위해선 위의 글을 클릭하셔서 공식서버에 접속해주세요!', inline=False)
        await message.channel.send(embed=jkembed)

    if message.content.startswith('.한강'):
        json = requests.get('http://hangang.dkserver.wo.tc/').json()
        temp = json.get("temp") # 한강온도
        time = json.get("time") # 측정시간

        embed = discord.Embed(title='💧 한강온도', description=f'{temp}°C', colour=discord.Colour.blue())
        embed.set_footer(text=f'{time}에 측정됨')

        await message.channel.send(embed=embed)

    if message.content.startswith('.위성'):
        url = 'https://www.weather.go.kr/weather/images/satellite_service.jsp'
        res = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(res, 'html.parser')
        soup = soup.find("div", class_="image-player-slide")
        imgUrl = 'https://www.weather.go.kr' + soup.find("img")["src"]

        typoonEmbed = discord.Embed(title='천리안 2A호 위성사진', description='제공: 기상청', colour=discord.Colour.dark_grey())
        typoonEmbed.set_image(url=imgUrl)
        await message.channel.send(embed=typoonEmbed)

    if message.content == (".사람인증"):
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author.id) + ".png"
        Image_captcha.write(a, name)


        await message.channel.send(file=discord.File(name))
        def check(msg):
            return msg.author == message.author and message.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.channel.send(embed=discord.Embed(title='시간이 초과되었습니다', colour=discord.Colour.green()))
            return

        if msg.content == a:
            await message.channel.send(embed=discord.Embed(title='당신은 사람입니다!', colour=discord.Colour.green()))
        else:
            await message.channel.send(embed=discord.Embed(title='당신이 사람인지 의심이 되는군요...', colour=discord.Colour.green()))

client.run(token)