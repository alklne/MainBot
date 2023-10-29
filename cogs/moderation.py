import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(help = "Remove a set amount of messages from the current channel", brief="Remove messages", description="Yeah, remove messages")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount:int):
        amount = amount or 100
        if amount > 100:
            await ctx.message.delete()
            await ctx.send(f"{ctx.message.author.mention}, you may only purge >100 messages at a time.", delete_after=5)
            return

        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{ctx.message.author.mention} purged {amount} messages successfully.", delete_after=5)

    @commands.command(help = "Kick a user with this command", brief = "Kicks a user", description="Yeah, really, it kicks members...")
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason="no reason was specified!"):
        if member == ctx.message.author:
            await ctx.send("You can't kick yourself.")
        else:
            if member.top_role < ctx.message.author.top_role:
                await member.kick(reason=reason)
                await ctx.send(f'{member.mention} has been kicked for: {" ".join(reason)}')
            else:
                await ctx.send("This user has a higher rank than you, IDIOT.")

async def setup(bot):
    await bot.add_cog(moderation(bot))