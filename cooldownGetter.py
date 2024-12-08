import json
import requests

patchId = "14.3.1" #Update this whenever a new patch comes out


def getSpellKey(i):
    if i < 4:
        return ("Q","W","E","R")[i]
    else:
        raise ValueError("More than 4 abilities")
    

def getCooldowns(championId):
    response = requests.get("https://ddragon.leagueoflegends.com/cdn/"+ patchId +"/data/en_US/champion/"+championId+".json")
    data = response.json()["data"][championId]
    championName = data["name"]
    output = f"{championName}'s cooldowns : \n"
    i = 0
    for spell in data["spells"]:
        print(type(spell))
        output += f"[{getSpellKey(i)}] {spell["name"]} cooldown: {spell["cooldown"]}\n"
        i+=1
    return output
