import os

try:
    import discord, requests, json, asyncio
    from colorama import Fore
    from discord.ext import commands

except:
    os.system('pip install discord.py requests asyncio colorama')

def clear():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

with open('config.json', 'r') as config:
    data = json.load(config)
    TOKEN = data['token']
    PREFIX = data['prefix']
    ACTIVITY = data['activity']
    COLOR = int(data['embedColor'], 16)
    AUTHOR = data['author']

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    clear()
    print(Fore.RED + f'[*] Bot connected as {bot.user}')
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=ACTIVITY))

bot.remove_command('help')

async def handle_reactions(message, embeds, user):
    emojis = ['◀️', '▶️']
    
    for emoji in emojis:
        await message.add_reaction(emoji)

    current_page = 0

    while True:
        try:
            reaction, reaction_user = await bot.wait_for(
                'reaction_add', timeout=120, check=lambda r, u: r.message.id == message.id and u.id == user.id and r.emoji in emojis
            )
        except asyncio.TimeoutError:
            await message.clear_reactions()
            break

        if reaction.emoji == '◀️' and current_page > 0:
            current_page -= 1
        elif reaction.emoji == '▶️' and current_page < len(embeds) - 1:
            current_page += 1
        else:
            continue

        await message.edit(embed=embeds[current_page])

        if message.channel.type == discord.ChannelType.text:
            try:
                await message.remove_reaction(reaction.emoji, reaction_user)
            except discord.Forbidden:
                pass  

@bot.command()
async def snusbase(ctx, *, search_term: str = None):
    if search_term is None:
        embed = discord.Embed(
            title="System Error",
            description="",
            color=COLOR
        )
        embed.add_field(name="Please add a `query` for search", value="", inline=False)
        embed.set_footer(text=AUTHOR)
        await ctx.send(embed=embed)  
        return

    waiting_message = await ctx.send('**I am `gathering the information`, please wait...**')

    snusbase_auth = 'sbyjthkoft4yaimbwcjqpmxs8huovd'
    snusbase_api = 'https://api-experimental.snusbase.com'

    url = f"{snusbase_api}/data/search"
    headers = {
        'auth': snusbase_auth,
        'Content-Type': 'application/json',
    }
    body = {
        'terms': [search_term],
        'types': ["email", "username", "lastip", "hash", "password", "name"],
        'wildcard': False,
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        result = response.json()

        if "results" in result:
            results = result["results"]

            if isinstance(results, dict):
                all_results = []
                for key in results:
                    all_results.extend(results[key])
            elif isinstance(results, list):
                all_results = results
            else:
                await ctx.send("**Response error: `unexpected structure` detected**")
                return

            page_size = 10
            embeds = []
            num_pages = (len(all_results) - 1) // page_size + 1
            for i in range(0, len(all_results), page_size):
                embed = discord.Embed(
                    title="Search Results",
                    description="Here is the `results` of the search",
                    color=discord.Color.blue()
                )
                page_results = all_results[i:i + page_size]
                for idx, result in enumerate(page_results):
                    description = json.dumps(result, indent=2)
                    embed.add_field(name=f"Result `{i + idx + 1}`", value=f"```json\n{description}\n```", inline=False)
                embed.set_footer(text=f"Page: `{len(embeds) + 1}/{num_pages}`")
                embeds.append(embed)

            await waiting_message.delete()

            try:
                dm_message = await ctx.author.send(embed=embeds[0])
                await handle_reactions(dm_message, embeds, ctx.author)
            except discord.Forbidden:
                await ctx.send("**Results `sent` to your DM!**")
        else:
            await ctx.send("**No results found for the `query`**")
    else:
        await ctx.send(f'**Error while searching: `{response.status_code}`**')

@bot.command(name="help")
async def helpcommands(ctx):
    embed = discord.Embed(
        title="SnusBase Commands",
        description="",
        color=COLOR
    )
    
    embed.add_field(name="☝️ `.snusbase` <username>", value="", inline=False)
    embed.add_field(name="🛠️ `.snusbase` <email>", value="", inline=False)
    embed.add_field(name="🚀 `.snusbase` <ip>", value="", inline=False)
    embed.add_field(name="❓ `.snusbase` <password>", value="", inline=False)
    embed.add_field(name="🌐 `.snusbase` <hash>", value="", inline=False)
    embed.add_field(name="📫 `.snusbase` <name>", value="", inline=False)

    embed.set_footer(text=AUTHOR)

    await ctx.send(embed=embed)        

bot.run(TOKEN)
