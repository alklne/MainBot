import discord
import time
from discord.ext import commands

class misc(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.time = 0
        self.activity_roles = [1167952127742718032,1167503980369289218,1167951576581820426,1167951629614587954,1167951691648356393]

    @commands.command()
    async def say(self, ctx, *text):
        if not text:
            await ctx.message.delete()
            await ctx.send(f"{ctx.author.mention} please send a **valid argument**!", delete_after = 4)
            return
        
        await ctx.send(" ".join(text))
        await ctx.message.delete()

    @commands.command()
    async def activity_stats(self, ctx):
        """
        okay im sorry but im not amazing at python so i don't know how to use cases/switches, sorry!
        """
        member_count = ctx.guild.member_count
        count=[0,0,0,0,0,0]

        for member in ctx.guild.members:
            if member.bot != True:
                roles = member.roles
                for role in roles:
                    if role.id==self.activity_roles[0]:
                        count[0]+=1
                    elif role.id==self.activity_roles[1]:
                        count[1]+=1
                    elif role.id==self.activity_roles[2]:
                        count[2]+=1
                    elif role.id==self.activity_roles[3]:
                        count[3]+=1
                    elif role.id==self.activity_roles[4]:
                        count[4]+=1
                    else:
                        count[5]+=1

        await ctx.send(f"Offline 24/7: {(member_count/count[0])*100}%\nBarely Active: {(member_count/count[1])*100}%\nSort of Active: {(member_count/count[2])*100}%\nActive: {(member_count/count[3])*100}%\nDangerously Active: {(member_count/count[4])*100}%")


        
                

        
        




async def setup(bot):
    await bot.add_cog(misc(bot))