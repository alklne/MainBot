import discord
import time
from discord.ext import commands

class misc(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *text):
        if not text:
            await ctx.message.delete()
            await ctx.send(f"{ctx.author.mention} please send a **valid argument**!", delete_after = 4)
            return
        
        await ctx.send(" ".join(text))
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(misc(bot))