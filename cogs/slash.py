import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, SlashCommand
import discord_slash



class Slash(commands.Cog):

    guild_ids = [824394116568842290]
    global guild_id
    guild_id = guild_ids[0]



    def __init__(self, bot):
        self.bot = bot
        
    #, guild_ids=guild_ids
    @cog_ext.cog_slash(name="delete_all_global_commands", description="Only the Bot Developer can use this command | Deletes all global slash commands")
    async def delete_all_global_commands(self, ctx: SlashContext):
        bot_id = 824392788258979913
        author_id = str(ctx.author.id)
        bot_token = "Put Token Here"
        if author_id == "268221711344730115":
            await discord_slash.utils.manage_commands.remove_all_commands_in(bot_id=bot_id, bot_token=bot_token, guild_id=guild_id)
            await ctx.send("Commands have been successfully removed!")
        else:
            await ctx.send("Only KKhaoSZ can run this command.", hidden=True)

    @cog_ext.cog_slash(name="delete_all_guild_commands", description="Only the Bot Developer can use this command | Deletes all guild slash commands")
    async def delete_all_guild_commands(self, ctx: SlashContext):
        bot_id = 824392788258979913
        author_id = str(ctx.author.id)
        bot_token = "ODI0MzkyNzg4MjU4OTc5OTEz.YFutnQ.qjIVcKxxyTc9M7JArf-TA9Ifmuw"
        if author_id == "268221711344730115":
            await discord_slash.utils.manage_commands.remove_all_commands_in(bot_id=bot_id, bot_token=bot_token, guild_id=guild_id)
            await ctx.send("Commands have been successfully removed!")
        else:
            await ctx.send("Only KKhaoSZ can run this command.", hidden=True)
    


    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Slash is ready.")
    
    
def setup(bot):
    bot.add_cog(Slash(bot))
