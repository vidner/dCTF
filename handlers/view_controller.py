from databases import task_database, audit_database, team_database
from discord import Embed
from collections import Counter
from config import score

import discord

def challenges():
    challs = task_database.find_all_visible_task()
    categorys = [chall.category for chall in challs]
    groups = {}

    for category in categorys:
        groups[category] = []
    
    for chall in challs:
        groups[chall.category].append(chall)
    
    solves = Counter(audit_database.number_of_solves())
    data = '```py\n'
    
    for category in groups:
        data += f'├── [{category}]\n'
        count = 0
        length = len(groups[category])

        for chall in groups[category]:
            value = int((((score.minimal - score.maximal) / (score.decay * score.decay)) * (solves[chall.id] * solves[chall.id])) + score.maximal)
            data += f'│   ├── [{chall.name}][{value}]\n' if (count < length-1) else f'│   └── [{chall.name}][{value}]\n'
            count += 1

    data += '```'
    card = Embed(title='Challenges', description=data, color=discord.Color.blue())
    
    return card

def challenges_info(name):
    chall = task_database.find_visible_task(name)
    solve = Counter(audit_database.number_of_solves())[chall.id]
    value = int((((score.minimal - score.maximal) / (score.decay * score.decay)) * (solve * solve)) + score.maximal)

    data = f'```md\n {chall.description}```'
    card = Embed(title=chall.name, description=data, url=chall.files, color=discord.Color.blue())
    card.add_field(name='Category', value=chall.category, inline=True)
    card.add_field(name='Solves', value=solve , inline=True)
    card.add_field(name='Scores', value=value , inline=True)
    
    blood = audit_database.firstblood(chall.id)
    if blood != None:
        team = team_database.find_team_data (blood.team_id)
        card.add_field(name='Firstblood', value=f':drop_of_blood: {team.name}', inline=False)

    return card

        

