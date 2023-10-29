"""
Hello!
I'm very, very bad at python- I'm also new to git, so please point out how I could improve my code overall through the issues
tab.

Thanks!
"""

import settings
import discord
import os
from discord.ext import commands

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix="?", intents=intents)

    @bot.event
    async def on_ready():
        """
        The area where cogs are loaded.
        """
        print("""                                                     
                  .---.                                               
                  |   |     .     .--.   _..._         __.....__      
                  |   |   .'|     |__| .'     '.   .-''         '.    
                  |   | .'  |     .--..   .-.   . /     .-''"'-.  `.  
            __    |   |<    |     |  ||  '   '  |/     /________\   \ 
         .:--.'.  |   | |   | ____|  ||  |   |  ||                  | 
        / |   \ | |   | |   | \ .'|  ||  |   |  |\    .-------------' 
        `" __ | | |   | |   |/  . |  ||  |   |  | \    '-.____...---. 
         .'.''| | |   | |    /\  \|__||  |   |  |  `.             .'  
        / /   | |_'---' |   |  \  \   |  |   |  |    `''-...... -'    
        \ \._,\ '/      '    \  \  \  |  |   |  |                     
         `--'  `"      '------'  '---''--'   '--'                     
        """)

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await bot.load_extension(f'cogs.{filename[:-3]}')
                except:
                    print(f"Failed to load: {filename}")
                else:
                    print(f"Loaded: {filename}")

        print(f"\n\nLoaded!\nUsername: {bot.user}\nID: {bot.user.id}")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("**Command not found**", delete_after=5)
            return
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("**You can't run this command, as you don't have the permissions to**", delete_after=5)
            return
        
    bot.run(settings.DISCORD_API_SECRET)

if __name__ == "__main__":
    run()