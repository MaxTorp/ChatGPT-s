import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix='!')

images = ['image1.png', 'image2.png', 'image3.png']

@bot.command()
async def send_image(ctx, index: int):
    if index < 1 or index > len(images):
        await ctx.send('Invalid index!')
        return
    
    image_file = disnake.File(images[index-1])
    await ctx.send(file=image_file)

bot.run('TOKEN')