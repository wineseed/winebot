import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print("로그인 중...")
    print(client.user.name)
    print(client.user.id)
    print("================")

food = ['카레', '스파게티', '집밥', '라면', '짜장면', '김치볶음밥', '우동', '쫄면', '국수', '돈까스', '엿(?)', '삼계탕', '치킨']
    
@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        a = ['안녕! 나는 준영맨이야!', '안녕! 내가 널 구하러 왔어!', '안녕! 어디서 많이 본거같은데...', '안녕! 무슨일이야?']
        await message.channel.send(random.choice(a))         
    if message.content.startswith("!운빨게임"):
        luck = ['니가 이김', '니가 짐', '비김']
        await message.channel.send(random.choice(luck))
    if message.content.startswith("!배고파"):
        await message.channel.send("배고파?")
        await message.channel.send("그럼 오늘은...")
        await message.channel.send(random.choice(food))
        await message.channel.send("어때?")
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
    if message.content.startswith("ㄹㅇ"):
        await message.channel.send("진짜요!!!!")
    if message.content.startswith("!빠루"):
        await message.channel.send("고든프리맨, 그는 좋은박사였지만.....")
        await message.channel.send("(하프라이프 후속작 안나온대)")
    if message.content.startswith("!고든프리맨"):
        await message.channel.send("그는 자유인이다!!!!!")
    if message.content.startswith("욕"):
        await message.channel.send("뒤지실?")
    if message.content.startswith("!도배"):
        await message.channel.send("너 진짜 미친놈인가 보구나.")
        await message.channel.send("샌즈 올림")
    if message.content.startswith(“테스트욕”):
        await message.channel.send(“욕했네?? 관리자께 보고해야지”)
        await message.g

        
access_token = os.environ["BOT_TOKEN"]    
client.run(access_token)
    
