import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(help = "Remove a set amount of messages from the current channel", brief="Remove messages", description="Yeah, remove messages")
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, amount:int):
        amount = amount or 100
        if amount > 100:
            await ctx.message.delete()
            await ctx.send(f"{ctx.message.author.mention}, you may only purge >100 messages at a time.", delete_after=5)
            return

        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{ctx.message.author.mention} purged {amount} messages successfully.", delete_after=5)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def kick(self, ctx, user : discord.User, *reason:str):
        if ctx.author.top_role > user.top_role:
            try:
                await user.kick(reason=" ".join(reason))
            except:
                await ctx.message.delete()
                await ctx.send(f"{ctx.message.author.mention}, failed to kick that user!") 
            else:
                await ctx.message.delete()
                await ctx.send(f"{ctx.message.author.mention}, failed to kick that user!") 
        else:
            await ctx.message.delete()
            await ctx.send(f"{ctx.message.author.mention}, successfully kicked")

async def setup(bot):
    await bot.add_cog(moderation(bot))