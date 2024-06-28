
import discord
from discord.ext import commands

class DeleteChannel(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Deletechannels is online.")


    @commands.command()
    async def delete_all_channels(self, ctx):
        try:
            # Delete voice channels
            for channel in ctx.guild.voice_channels:
                #await channel.delete()
                print(f"Deleted voice channel: {channel.name}")
                await ctx.send(f"Deleted voice channel: {channel.name}")

            # Delete text channels
            for channel in ctx.guild.text_channels:
                #await channel.delete()
                print(f"Deleted text channel: {channel.name}")
                await ctx.send(f"Deleted text channel: {channel.name}")

            # Delete categories and their child channels
            for category in ctx.guild.categories:
                for channel in category.channels:
                    await channel.delete()
                    print(f"Deleted {channel.type} channel: {channel.name}")
                    await ctx.send(f"Deleted {channel.type} channel: {channel.name}")
                await category.delete()
                print(f"Deleted category: {category.name}")
                await ctx.send(f"Deleted category: {category.name}")

            # Delete stage channels
            for channel in ctx.guild.stage_channels:
                await channel.delete()
                print(f"Deleted stage channel: {channel.name}")
                await ctx.send(f"Deleted stage channel: {channel.name}")

        except discord.Forbidden:
            await ctx.send("Missing permissions to delete a channel.")
        except discord.HTTPException as e:
            await ctx.send(f"Failed to delete a channel. Error: {e}")

    @commands.command(name='delete')
    async def delete_all_channels_command(self, ctx):
        await self.delete_all_channels(ctx)


async def setup(client):
    await client.add_cog(DeleteChannel(client))
