import discord
import settings
from discord.ext import commands

class owner(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def viewServers(self, ctx):
        if ctx.author.id == settings.OWNER_ID:
            await ctx.message.delete()
            print(self.bot.guilds)
            await ctx.send(f"{ctx.message.author.mention}, logged to console.", delete_after=5)
        else:
            await ctx.message.delete()
            await ctx.send(f"{ctx.author.mention}, you cannot use this command.", delete_after=5)

    @commands.command(hidden=True)
    async def viewToken(self, ctx):
        if ctx.author.id == settings.OWNER_ID:
            await ctx.message.delete()
            await ctx.send(f"{ctx.author.mention}, {settings.DISCORD_API_SECRET}")
        else:
            await ctx.message.delete()
            await ctx.send(f"{ctx.author.mention}, you cannot use this command.", delete_after=5)

    @commands.command(hidden=True)
    async def shutdown(self, ctx):
        if ctx.author.id == settings.OWNER_ID:
            await ctx.send(f"The bot will now shut down, {ctx.message.author.mention}.")
            print("\n\nPowering off.")
            await self.bot.close()
        else:
            await ctx.message.delete()
            await ctx.send(f"{ctx.author.mention}, you cannot use this command.", delete_after=5)


async def setup(bot):
    await bot.add_cog(owner(bot))