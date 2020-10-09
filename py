import discord

client = discord.Client

@client.event
async def on_ready():
    print('login')
    print(client.user.name)
    print(-------------------)
    await client.change_presence(game=discord.Game(name='test',type))

@client.event
async def on_message(message):
    if message.channel and message.author.id !="763927761668276234"
        await client.send_message(discord.utils.get(cilent.gat_all_members(), id="760879690843684874",id="622691584948961289"), message.author.name + "(" + massege.author.id + ") : " + message.content)

    if message.content.startswitch("!DM"):
        member = discord.utils.get(client.get_all_members(), id=message.content[4:22])
        await client.send_message(member, "FIRE EAGLE관리자 답변 : " + message.content[23:])

