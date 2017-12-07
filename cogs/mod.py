import discord
import sys
import os
import io
from discord.ext import commands


class mod:

    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    async def dm(self, ctx, user: discord.Member, *, msg: str):
        """Escort your DM to someone thru the bot. Usage: *dm [tag person] [msg]"""
        try:
            await user.send(msg)
            await ctx.send("SuccESS! Your DM has made it! :white_check_mark: ")
        except:
            await ctx.send("Error :x:. Make sure your message is shaped in this way: *dm [tag person] [msg]")
            
            
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.Member):
        """Kicks a member into the world outside your server."""
        await ctx.channel.send(f"Be gone {user.name}! Oh, and close the door on the way out :door:.")
        await user.kick()
            
            
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Member):
        """Swings the mighty Ban Hammer on that bad boy."""
        await ctx.channel.send(f"The ban hammer has fallen. And it has struck {user.name}.")
        await user.ban()
        
    @commands.command()
    async def serverinfo(self, ctx):
        """Displays Info About The Server!"""
        guild = ctx.guild 
        roles = [x.name for x in guild.roles] 
        role_length = len(roles)
        roles = ', '.join(roles)
        channels = len(guild.channels)
        time = str(guild.created_at.strftime("%b %m, %Y, %A, %I:%M %p")) 

        embed = discord.Embed(description="-", title='Server Info', colour=passcolor)
        if guild.icon_url:
            embed.set_thumbnail(url=guild.icon_url)
        else:
            embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.add_field(name='__Server __', value=str(guild.name))
        embed.add_field(name='__Server ID__', value=str(guild.id))
        embed.add_field(name='__Owner__', value=str(guild.owner))
        embed.add_field(name='__Owner ID__', value=guild.owner_id) 
        embed.add_field(name='__Member Count__', value=str(guild.member_count))
        embed.add_field(name='__Text/Voice Channels__', value=str(channels))
        embed.add_field(name='__Server Region__', value='%s' % str(guild.region))
        embed.add_field(name='__ Total Roles__', value='%s' % str(role_length))
        embed.add_field(name='__Roles__', value='%s' % str(roles))
        embed.set_footer(text='Created - %s' % time)

        await ctx.send(embed=embed)

            
            
def setup(bot): 
    bot.add_cog(mod(bot))
