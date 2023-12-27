import discord
from discord.ext import commands, tasks
import os
import requests
localcache = []
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='ilikeputtingrandomstuffasthecommandprefix 💀',intents=intents)

if "BOT_TOKEN" in os.environ:
    bot_token = os.environ["BOT_TOKEN"]
else:
    with open("env/token.txt", "r") as file:
        bot_token = file.read().strip()

@bot.event
async def on_member_join(member):
    await check(member)

@bot.event
async def on_member_remove(member):
    await check(member)

@tasks.loop(minutes=15)
async def update():
    try:
        global localcache
        requests.get('https://linkleakers--rare1k.repl.co/') # update server cache
        response = requests.get('https://linkleakers--rare1k.repl.co/ids')
        ids = response.json()
        localcache = ids
        print("Cache updated.")
        
        
    except Exception as e:
        print(f"Error updating cache: {e}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await update() # Initial update
    update.start()

async def check(member):
    try:
        global localcache
        mid = str(member.id)
        if mid in localcache:
            reason = "Automatically banned by AntiLinkLeak. Reason: Link Leaking. If this was a mistake, request @rare1k on Discord to remove this user from the list."
            await member.ban(reason=reason)
            print(f"Banned member {member.name}#{member.discriminator} ({member.id}) for link leaking.")
            return True
        return False
        
    except Exception as e:
        print(f"Error checking and banning member: {e}")




@bot.slash_command(name='llban')
async def llban(ctx):
    await ctx.defer();
    total = 0
    unbanned = 0
    try:
        await update()
        members = await ctx.guild.fetch_members(limit=None).flatten()

        for member in members:
            cr = await check(member)
            if (cr == "unban"):
                unbanned += 1
            elif (cr):
                total += 1
        async for banned_user in member.guild.bans():
          if str(banned_user.user.id) not in localcache and 'AntiLinkLeak' in banned_user.reason:
           await member.guild.unban(banned_user.user, reason='AntiLinkLeak: User removed from ban list.')
           print(f"Unbanned member {banned_user.user.name}#{banned_user.user.discriminator} ({banned_user.user.id}).")
           return "unban"

    except Exception as e:
        print(f"Error checking server: {e}")
    await ctx.respond(f'Banned {total} members; unbanned {unbanned} members.')

bot.run(bot_token)
