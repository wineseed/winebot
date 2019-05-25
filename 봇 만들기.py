import requests
import discord
import asyncio
from json import loads

client = discord.Client()

@client.event
async def on_ready():
    print("로그인 중...")
    print(client.user.name)
    print(client.user.id)
    print("================")
    twitch = "와인씌"
    name = "와인씌"
    channel = client.get_channel(562226296835407889)
    a = 0
    while True:
        headers = {'Client-ID':'oyetxcfm3x660znecu9tcumeb3wk5t'}
        response = requests.get("http://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await message.channel.send(name + "와인씌가 방송켰다 들어와라.")
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)
            


@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕! 난 똑똑한 와인이야!")
        await message.channel.send("필요한게 있다면 !에 도움말을 입력해줘!")      
    if message.content.startswith("!도움말"):
        await message.channel.send("방송시간,유튜브,그리고....")
        await message.channel.send("이스터에그도 있을려나?")
        await message.channel.send("참고로 제작자는 jyman0입니다.")                                 
    if message.content.startswith("!와인씌"):
        await message.channel.send("구독하고 팔로우 해!!!!")
        await message.channel.send("ㅏ!!!!!")                                  
    if message.content.startswith("!바보"):
        await message.channel.send("흥!")                                  
    if message.content.startswith("!이스터에그"):
        await message.channel.send("음...나도 몰라.")
        await message.channel.send("하지만 제작자는 알지도?")                                  
    if message.content.startswith("!유튜브"):
        await message.channel.send("구독과 좋아요 눌러!!!")
        await message.channel.send("https://www.youtube.com/channel/UCvBQM82NnYbVXcm_VlqMx4g")
    if message.content.startswith("!트위치"):
        await message.channel.send("와인씌 트위치 팔로우 해!!!")
        await message.channel.send("트위치 wineseed")
    if message.content.startswith("!뜨끈뜨끈한와인"):
        await message.channel.send("걔는 필요없거든!!")
        await message.channel.send("걔이름 꺼내지 마!! 추방시킨다??")
    if message.content.startswith("!오래된와인"):
        await message.channel.send("아~ 그 노래만 부르는 애~?")
        await message.channel.send("그래도 그나마 나은애야")
        await message.channel.send("뜨끈뜨끈 보다는...")
    if message.content.startswith("!멍청이"):
        await message.channel.send("흥!")
    if message.content.startswith("!나이"):
        await message.channel.send("나이? 나이가 뭐야? 먹는건가?")
        await message.channel.send("제작자: 12살입니다.")
        await message.channel.send("ㅇㅎ!")
    if message.content.startswith("!방송시간"):
        await message.channel.send("토,일 방송이고 평일도 가끔해!")
    if message.content.startswith("!제작자"):
        await message.channel.send("jyman0 이라는 분이 날 제조 하셨어. 근데 난 참 똑똑해!")
    if message.content.startswith("!성별"):
        await message.channel.send("그런게 왜 중요해!")
    if message.content.startswith("!메롱"):
        await message.channel.send("흥!")
    if message.content.startswith("!와!"):
        await message.channel.send("와! 샌즈! 파피루스!")
        await message.channel.send("아~ 언더테일 아시는구나~")
        await message.channel.send("참고로 겁.나.어.렵.습.니.다.")
        await message.channel.send(".. 라고 하네여")
    if message.content.startswith("!ㅎㅇ"):
        await message.channel.send("ㅎㅇ~")
    if message.content.startswith("!실명"):
        await message.channel.send("그건 바로 &*^*^*&*&(입막기)")
    if message.content.startswith("!jyman0"):
        await message.channel.send("jyman0: 저 불렀어요?")
    if message.content.startswith("!똑똑한와인"):
        await message.channel.send("왜여?")
    if message.content.startswith("!술"):
        await message.channel.send("딸꾹")
    if message.content.startswith("!소주"):
        await message.channel.send("아니 와인이 최고죠~")
    if message.content.startswith("!맥주"):
        await message.channel.send("아니 와인 마십시다!")
    if message.content.startswith("!배그"):
        await message.channel.send("탕탕탕탕! 으악 사람이다 (사망)")
    if message.content.startswith("!배틀그라운드"):
        await message.channel.send("탕탕탕탕! 으악 사람이다 (사망)")
    if message.content.startswith("!레인보우식스"):
        await message.channel.send("그게 머임?")
    if message.content.startswith("!레식"):
        await message.channel.send("그게 머임?")
    if message.content.startswith("!프로필"):
        await message.channel.send("뭐야!! 나 프사 왜이래!!")
    if message.content.startswith("!나닛"):
        await message.channel.send("나닛--!!!")
    if message.content.startswith("!햄보칸플리퍼"):
        await message.channel.send("a제곱 더하기 b제곱은 c제곱 피타고라ㅅ..")
        



        
    
client.run('NTgxMzgwNTc5NzAyODY1OTUw.XOe-Qw.XAKJkfUcIYFCoSwDfrlkyu07zPw')
    
