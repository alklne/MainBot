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
        print('Command ran!')
        offline_247=0
        barely_active=0
        active_degree=0
        active=0
        dangerously_active=0
        member_count = ctx.guild.member_count

        for member in ctx.guild.members:
            if member.bot != True:
                if member.get_role(self.activity_roles[0]) != None:
                    offline_247+=1
                if member.get_role(self.activity_roles[1]) != None:
                    barely_active+=1
                if member.get_role(self.activity_roles[2]) != None:
                    active_degree+=1
                if member.get_role(self.activity_roles[3]) != None:
                    active+=1
                if member.get_role(self.activity_roles[4]) != None:
                    dangerously_active+=1

        print(f"""
        **BETA COMMAND, THIS MAY NOT WORK!**
        Server Members: {member_count}
        Percentages:
            Offline_24/7: {(member_count/offline_247)*100}
            Barely_Active: {(member_count/barely_active)*100}
            Active To A Degree: {(member_count/active_degree)*100}
            Active: {(member_count/active)*100}
            Dangerously Active: {(member_count/dangerously_active)*100}
        """)



async def setup(bot):
    await bot.add_cog(misc(bot))