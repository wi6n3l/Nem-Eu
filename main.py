import discord
import random

global id
global Frases
Frases = "Olha quem chegou,o ", "Mais um cabeçudo, ", "Mais um viciado para o grupo, "
channel_id = "426766570275078150"

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='A pesquisar no Google como pesquisar no Google'))

@client.event
async def on_member_join(member):
    await client.send_message(discord.Object(id=channel_id), Frases[random.randint(0,2)] + str(member.name) )

@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        if message.content.lower().startswith("!jogos"):
            print(message.channel.id)
            print(str(message.author) + " " + str(message.content))
            embed = discord.Embed(
                title="Escolhe os teus jogos!",
                color=0x0033cc,
                description="- CS:GO = 💣\n"
                            "- GTA V = 🚓\n"
                            "- Fortnite = 🛠\n"
                            "- Rainbow Six = 🌈\n"
                            "- Call of Duty = 🔫\n"
                            "- Rocket Leage = 🏎"
            )
            defenir = await client.send_message(message.channel, embed=embed)
            global defenir_id
            defenir_id = defenir.id
            await client.add_reaction(defenir, "💣")
            await client.add_reaction(defenir, "🚓")
            await client.add_reaction(defenir, "🛠")
            await client.add_reaction(defenir, "🌈")
            await client.add_reaction(defenir, "🔫")
            await client.add_reaction(defenir, "🏎")

        elif message.content.startswith("Votação"):
            print(message.channel.id)
            print(str(message.author) + " " + str(message.content))
            await client.add_reaction(message, "👍")
            await client.add_reaction(message, "👎")

        elif message.content.startswith("!comando"):
            channel = message.channel
            await client.delete_message(message)
            async def executar_comando(comando):
                if comando == "kick":
                    await client.kick(input("ID:"))
                elif comando == "ban":
                    await client.ban(int(input("ID:")))
                elif comando == "falar":
                    msg = str(input("Mensagem: "))
                    cnl = int(input("Canal(" + channel.id + "):"))
                    await client.send_message(discord.Object(cnl), str(msg))
            comando_in = input("Comando: ")
            await executar_comando(comando_in)

@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    if reaction.emoji == "💣" and message.id == defenir_id:
        role = discord.utils.find(lambda r: r.name == "CS:GO", message.server.roles)
        await client.add_roles(user, role)
    elif reaction.emoji == "🚓" and message.id == defenir_id:
        role = discord.utils.find(lambda r: r.name == "GTA V", message.server.roles)
        await client.add_roles(user, role)
    elif reaction.emoji == "🛠" and message.id == defenir_id:
        role = discord.utils.find(lambda r: r.name == "Fortnite", message.server.roles)
        await client.add_roles(user, role)
    elif reaction.emoji == "🌈" and message.id == defenir_id:
        role = discord.utils.find(lambda r: r.name == "Rainbow Six", message.server.roles)
        await client.add_roles(user, role)
    elif reaction.emoji == "🔫" and message.id == defenir_id:
        role = discord.utils.find(lambda r: r.name == "Call of Duty", message.server.roles)
        await client.add_roles(user, role)
    elif reaction.emoji == "🏎" and message.id == defenir_id:
        role = discord.utils.find(lambda r: r.name == "Rocket Leage", message.server.roles)
        await client.add_roles(user, role)

@client.event
async def on_reaction_remove(reaction, user):
    message = reaction.message
    if reaction.emoji == "💣" and message.id == defenir_id:
        role = discord.utils.find(lambda r: r.name == "CS:GO", message.server.roles)
        await client.remove_roles(user, role)
    elif reaction.emoji == "🚓" and message.id == defenir_id:
        role = discord.utils.find(lambda r: r.name == "GTA V", message.server.roles)
        await client.remove_roles(user, role)
    elif reaction.emoji == "🛠" and message.id == defenir_id:
        role = discord.utils.find(lambda r: r.name == "Fortnite", message.server.roles)
        await client.remove_roles(user, role)
    elif reaction.emoji == "🌈" and message.id == defenir_id:
        role = discord.utils.find(lambda r: r.name == "Rainbow Six", message.server.roles)
        await client.remove_roles(user, role)
    elif reaction.emoji == "🔫" and message.id == defenir_id:
        role = discord.utils.find(lambda r: r.name == "Call of Duty", message.server.roles)
        await client.remove_roles(user, role)
    elif reaction.emoji == "🏎" and message.id == defenir_id:
        role = discord.utils.find(lambda r: r.name == "Rocket Leage", message.server.roles)
        await client.remove_roles(user, role)

client.run("NDU3Mjg5NDYxMTYwNDc2Njcz.DgkaAQ.OrfHiXa6MLjJuKK4DS8B-mvIm6U")
