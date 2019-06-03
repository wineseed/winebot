import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("로그인 중...")
    print(client.user.name)
    print(client.user.id)
    print("================")
    

@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕! 난 준영맨이야!")
        await message.channel.send("필요한게 있다면 !에 도움을 입력해줘!")      
    if message.content.startswith("!도움"):
        await message.channel.send("내가 도와주지!")
        await message.channel.send("간드아!!!!!!!!!!")
        await message.channel.send("참고로 제작자는 jyman0입니다.")                                                                  
    if message.content.startswith("!바보"):
        await message.channel.send("흥!")                                  
    if message.content.startswith("!이스터에그"):
        await message.channel.send("음...나도 몰라.")
        await message.channel.send("하지만 제작자는 알지도?")                                
    if message.content.startswith("!멍청이"):
        await message.channel.send("흥!")
    if message.content.startswith("!나이"):
        await message.channel.send("나이? 나이가 뭐야? 먹는건가?")
        await message.channel.send("제작자: 12살입니다.")
        await message.channel.send("ㅇㅎ!")
    if message.content.startswith("!제작자"):
        await message.channel.send("jyman0 입니다.")
    if message.content.startswith("!성별"):
        await message.channel.send("그런게 왜 중요해!")
    if message.content.startswith("!메롱"):
        await message.channel.send("흥!")
    if message.content.startswith("!와"):
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
    if message.content.startswith("!배그"):
        await message.channel.send("탕탕탕탕! 으악 사람이다 (사망)")
    if message.content.startswith("!배틀그라운드"):
        await message.channel.send("탕탕탕탕! 으악 사람이다 (사망)")
    if message.content.startswith("!레인보우식스"):
        await message.channel.send("그게 머임?")
    if message.content.startswith("!레식"):
        await message.channel.send("그게 머임?")
    if message.content.startswith("!나닛"):
        await message.channel.send("나닛--!!!")
    if message.content.startswith("!햄보칸플리퍼"):
        await message.channel.send("a제곱 더하기 b제곱은 c제곱 피타고라ㅅ..")
    if message.content.startswith("?"):
        await message.channel.send("뭐요....")
    if message.content.startswith("!모두"):
        await message.channel.send("여러분! 이사람의 말을 듣지않으면 저한테 맞을줄 아세요!")
    if message.content.startswith("!소개"):
        await message.channel.send("전..영웅입니다")
    if message.content.startswith("ㅂ"):
        await message.channel.send("그럼 안녕히.......")
    if message.content.startswith("ㅋ"):
        await message.channel.send("ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ")
        await message.channel.send("LOL   하하하하핳하하ㅏ")
        await message.channel.send(".......뭐가 웃기죠?")
    if message.content.startswith("!옵치"):
        await message.channel.send("석양이.....으억")
    if message.content.startswith("!오버워치"):
        await message.channel.send("하늘에서! 정의가! 으억.....")

        
access_token = os.environ["BOT_TOKEN"]    
client.run(access_token)
    
