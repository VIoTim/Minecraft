import os
import json

with open('UUID.json', mode='w', encoding='utf8') as uuidjson:
    uuid = {'players':[]}
    for filename in os.listdir('./playerdata'):
        if filename.endswith('.dat'):
            uuid['players'].append(f'{filename[:-4]}')
    json.dump(uuid,uuidjson)

with open('UUID.json', mode='r', encoding='utf8') as uuid:
    uuid = json.load(uuid)

player = {'players':[]}
for i in uuid['players']:
    j = str(i)
    
    num0 = int(j[0:8], 16)
    if 0 > (7 - int(j[0:1], 16)):
        out0 = str(num0 - 2**32)
    else:
        out0 = str(num0)
    
    str1 = str(j[9:13] + j[14:18])
    num1 = int(str1, 16)
    if 0 > (7 - int(j[9:10], 16)):
        out1 = str(num1 - 2**32)
    else:
        out1 = str(num1)

    str2 = str(j[19:23] + j[24:28])
    num2 = int(str2, 16)
    if 0 > (7 - int(j[19:20], 16)):
        out2 = str(num2 - 2**32)
    else:
        out2 = str(num2)

    num3 = int(j[28:36], 16)
    if 0 > (7 - int(j[28:29], 16)):
        out3 = str(num3 - 2**32)
    else:
        out3 = str(num3)

    f = [out0, out1, out2, out3]

    player['players'].append(f)

with open('data.json', mode='w', encoding='utf8') as data:
    json.dump(player, data)

with open('data.json', mode='r', encoding='utf8') as data:
    data = json.load(data)

m = open('./datapacks/wolf/data/uuid/functions/main.mcfunction', mode='w', encoding='utf8')
m.writelines(f'scoreboard objectives add Wolf dummy "Wolf"\nscoreboard objectives add Count dummy "Count"')
n = open('./datapacks/wolf/pack.mcmeta', mode= 'w', encoding='utf8')
n.writelines(f'{{"pack":{{"pack_format":7, "description":"Wolf"}}}}')
I = {'value':[]}
for i in data['players']:
    k = open(f'./datapacks/wolf/data/uuid/functions/{i[0]}.mcfunction', mode='w', encoding='utf8')
    k.writelines(f'execute as @e[type=minecraft:wolf, nbt={{Owner:[I;{i[0]},{i[1]},{i[2]},{i[3]}]}}] run scoreboard players add {i[0]} Count 1\nscoreboard players operation @a[nbt={{UUID:[I;{i[0]},{i[1]},{i[2]},{i[3]}]}}] Wolf = {i[0]} Count\nscoreboard players set {i[0]} Count 0')
    I['value'].append(i[0])

o = open('./datapacks/wolf/data/minecraft/tags/functions/tick.json', mode='w',encoding='utf8')
o.write("{\"values\":[")
for i in I['value']:
    o.write(f'\"uuid:{i}\"')
    if i == I["value"][-1]:
        break
    else:
        o.write(",")

o.write("]}")


p = open('./datapacks/wolf/data/minecraft/tags/functions/load.json', mode='w', encoding='utf8')
p.write('{"values":["uuid:main"]}')