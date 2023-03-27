import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!embed'):
        embed = discord.Embed(title="���������", description="��������", color=0x00ff00)
        embed.add_field(name="���� 1", value="�������� 1", inline=False)
        embed.add_field(name="���� 2", value="�������� 2", inline=False)
        embed.set_footer(text="������ ����������")
        await message.channel.send(embed=embed)

client.run('TOKEN')