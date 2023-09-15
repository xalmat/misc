import random

smz3logic=["normal","hard"]
smz3race=["true","false"]
smz3keys=["true","false"]
smz3access=["defeatboth","fastganondefetamotherbrain","alldungeondefeatmotherbrain"]
smz3tower=[
    "0",
    "1","1",
    "2","2","2",
    "3","3","3","3",
    "4","4","4","4","4",
    "5","5","5","5","5","5",
    "6","6","6","6","6","6","6",
    "7","7","7","7","7","7","7","7",
    "random","random","random","random"    ]
smz3ganon=[
    "0",
    "1","1",
    "2","2","2",
    "3","3","3","3",
    "4","4","4","4","4",
    "5","5","5","5","5","5",
    "6","6","6","6","6","6","6",
    "7","7","7","7","7","7","7","7",
    "random","random","random","random"]
smz3tourian=[
    "0","0",
    "1","1","1","1",
    "2","2","2","2","2","2",
    "3","3","3","3","3","3","3","3",
    "4","4","4","4","4","4","4","4","4","4",
    "random","random","random","random","random"]


smz3startingitems=["","start:Boots","start:Boots,random:1","start:Charge,Hijump,Springball"]

logic = random.randint(0,len(smz3logic)-1)
race = random.randint(0,len(smz3race)-1)
keys = random.randint(0,len(smz3keys)-1)
access = random.randint(0,len(smz3access)-1)
tower= random.randint(0,len(smz3tower)-1)
ganon = random.randint(0,len(smz3ganon)-1)
tourian = random.randint(0,len(smz3tourian)-1)
items = random.randint(0,len(smz3startingitems)-1)
print("!smz3 beta:true logic:"+smz3logic[logic], "race:"+smz3race[race], "keysanity:"+smz3keys[keys], "goal:"+smz3access[access], "tower:"+smz3tower[tower], "ganon:"+smz3ganon[ganon], "tourian:"+smz3tourian[tourian],smz3startingitems[items])