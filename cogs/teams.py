import discord
import random
from discord.ext import commands
from collections import defaultdict
import os
import asyncio




# Sample data representing participants with their departments
participants = [
    {"name": "Alice", "department": "HR"},
    {"name": "Bob", "department": "IT"},
    {"name": "Charlie", "department": "HR"},
    {"name": "David", "department": "Sales"},
    {"name": "Eve", "department": "IT"},
    {"name": "Frank", "department": "IT"},
    {"name": "Grace", "department": "Sales"},
    {"name": "Henry", "department": "HR"},
    {"name": "Ivy", "department": "Sales"},
    {"name": "Jack", "department": "IT"},
    {"name": "Kim", "department": "HR"},
    {"name": "Liam", "department": "IT"}
]

intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)


# Function to create even teams with no participant repeats
def create_even_teams(participants, team_size):
    department_map = defaultdict(list)
    
    for participant in participants:
        department_map[participant['department']].append(participant['name'])
    
    # Shuffle participants within each department
    for department in department_map:
        random.shuffle(department_map[department])
    
    # Calculate the number of teams needed
    num_teams = len(participants) // team_size
    
    teams = []
    
    for i in range(num_teams):
        team_members = []
        used_participants = set()
        
        while len(team_members) < team_size:
            for department in department_map:
                if len(team_members) >= team_size:
                    break
                if department_map[department]:
                    participant = department_map[department].pop()
                    if participant not in used_participants:
                        team_members.append(participant)
                        used_participants.add(participant)
        
        # Generate a unique team ID
        team_id = f"Team-{i + 1}"
        teams.append({"team_id": team_id, "members": team_members})
    
    return teams

# Cog class for team commands
class TeamCog(commands.Cog, name="Team Commands"):
    def __init__(self, client):
        self.client = client

    @commands.command(name="create_teams", help="Creates teams with even distribution of participants from all departments.")
    async def create_teams(self, ctx, team_size: int = 4):
        teams = create_even_teams(participants, team_size)
        
        # Output teams in Discord channel
        for team in teams:
            members = ', '.join(team['members'])
            await ctx.send(f"Team ID: {team['team_id']}\nMembers: {members}")

# Add the cog to the bot
client.add_cog(TeamCog(client))

async def setup(client):
    await client.add_cog(TeamCog(client))